import glob
import importlib
import io
import logging
import os
import platform
import sys
import tarfile
import time
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Callable
from typing import List
from typing import Optional
from typing import Tuple

import click
import click.shell_completion
import pytest
import requests
import yaspin.spinners
from google.protobuf import empty_pb2

import tecton
from tecton import tecton_context
from tecton._internals import metadata_service
from tecton._internals import sdk_decorators
from tecton._internals.analytics import StateUpdateResult
from tecton._internals.display import Displayable
from tecton._internals.utils import format_freshness_table
from tecton._internals.utils import format_materialization_attempts
from tecton._internals.utils import get_all_freshness
from tecton._internals.utils import plural
from tecton.cli import access_control
from tecton.cli import api_key
from tecton.cli import cli_utils
from tecton.cli import common
from tecton.cli import environment
from tecton.cli import printer
from tecton.cli import service_account
from tecton.cli import user
from tecton.cli import workspace
from tecton.cli import workspace_utils
from tecton.cli.command import TectonCommand
from tecton.cli.command import TectonGroup
from tecton.cli.command import _cluster_url
from tecton.cli.engine import dump_local_state
from tecton.cli.engine import update_tecton_state
from tecton.cli.error_utils import pretty_error
from tecton.cli.workspace import WorkspaceType
from tecton.framework import base_tecton_object
from tecton.identities import credentials
from tecton.identities import okta
from tecton_core import repo_file_handler
from tecton_core.errors import TectonAPIInaccessibleError
from tecton_core.errors import TectonValidationError
from tecton_core.fco_container import FcoContainer
from tecton_core.id_helper import IdHelper
from tecton_proto.metadataservice import metadata_service_pb2


CONTEXT_SETTINGS = {
    "max_content_width": 160,
    "help_option_names": ["-h", "--help"],
}

_CLIENT_VERSION_INFO_RESPONSE_HEADER = "x-tecton-client-version-info"
_CLIENT_VERSION_WARNING_RESPONSE_HEADER = "x-tecton-client-version-warning"


@click.group(name="tecton", context_settings=CONTEXT_SETTINGS, cls=TectonGroup)
@click.option("--verbose/--no-verbose", default=False, help="Be verbose")
@click.option("--debug/--no-debug", default=False, help="Enable debug info.")
@click.pass_context
def cli(ctx, verbose, debug):
    "Tecton command-line tool."
    sdk_decorators.disable_sdk_public_method_decorator()

    logging_level = logging.DEBUG if debug else logging.WARNING
    logging.basicConfig(
        level=logging_level,
        stream=sys.stderr,
        format="%(levelname)s(%(name)s): %(message)s",
    )

    # add cwd to path
    sys.path.append("")


@cli.command(requires_auth=False)
def version():
    """Print version."""
    tecton.version.summary()


@cli.command(requires_auth=False)
@click.option("--zsh", default=False, is_flag=True, help="Generate a zsh tab completion script.")
@click.option("--bash", default=False, is_flag=True, help="Generate a bash tab completion script.")
@click.option("--fish", default=False, is_flag=True, help="Generate a fish tab completion script.")
def completion(zsh, bash, fish):
    """Generates a shell script to set up tab completion for Tecton. Zsh, bash, and fish shells are supported.

    See typical usage examples below:

    zsh:

        # Generate and save the Tecton auto-complete script.

        tecton completion --zsh > ~/.tecton-complete.zsh

        # Enable zsh auto-completion. (Not needed if you already have auto-complete enabled, e.g. are using oh-my-zsh.)

        echo 'autoload -Uz compinit && compinit' >> ~/.zshrc

        # Add sourcing the script into your .zshrc.

        echo '. ~/.tecton-complete.zsh' >> ~/.zshrc

    bash:

        # Generate and save the Tecton auto-complete script.

        tecton completion --bash > ~/.tecton-complete.bash

        # Add sourcing the script into your .bashrc.

        echo '. ~/.tecton-complete.bash' >> ~/.bashrc

    fish:

        # Generate and save the Tecton auto-complete script to your fish configs.

        tecton completion --fish > ~/.config/fish/completions/tecton.fish
    """
    true_count = sum([zsh, bash, fish])
    if true_count != 1:
        msg = "Please set exactly one of --zsh, --bash, or --fish to generate a script for your shell environment."
        raise SystemExit(msg)

    if zsh:
        instruction = "zsh_source"
    elif bash:
        instruction = "bash_source"
    elif fish:
        instruction = "fish_source"

    status_code = click.shell_completion.shell_complete(
        cli, ctx_args={}, prog_name="tecton", complete_var="_TECTON_COMPLETE", instruction=instruction
    )
    sys.exit(status_code)


class EngineCommand(TectonCommand):
    def __init__(
        self,
        *args,
        apply: bool,
        upgrade_all: bool = False,
        destroy: bool = False,
        allows_suppress_recreates: bool = False,
        has_plan_id: bool = False,
        **kwargs,
    ):
        @click.pass_context
        def callback(
            ctx,
            yes,
            safety_checks,
            no_safety_checks,
            json_out,
            suppress_warnings,
            workspace,  # Not used but it needs to be here to match params list.
            suppress_recreates=False,
            plan_id=None,
            skip_tests=None,
        ):
            args = EngineArgs(
                skip_tests=skip_tests,
                json_out=json_out,
                no_safety_checks=yes or no_safety_checks,
                suppress_warnings=suppress_warnings,
                debug=common.get_debug(ctx),
            )

            assert not (plan_id and suppress_recreates), (
                "The flag --suppress-recreates is only used when computing a new plan. If the plan passed "
                "in using --plan-id was already computed using --suppress-recreates, that behavior persists "
                "as part of the plan."
            )

            if yes and safety_checks:
                msg = "The flag --yes is an alias for --no-safety-checks, and so the flags --yes and --safety-checks cannot be used together"
                raise TectonValidationError(msg)

            if safety_checks or no_safety_checks:
                cli_utils.print_version_msg(
                    "The flags --safety-checks and --no-safety-checks are deprecated and will be removed "
                    "in 0.8. Remove --safety-checks or use --yes instead of --no-safety-checks.",
                    True,
                )

            if plan_id:
                args.plan_id = plan_id
            if suppress_recreates:
                args.suppress_recreates = suppress_recreates

            return run_engine(args, apply=apply, upgrade_all=upgrade_all, destroy=destroy)

        params = [
            # TODO(Add help)
            click.Option(
                ["--yes", "-y"],
                is_flag=True,
                default=False,
                help="Disable interactive safety checks.",
            ),
            # TODO(deprecate_after=0.8) --no-safety-checks will be replaced with --yes
            # --safety-checks and --no-safety-checks is split up so we can know when a user has explicitly set these
            # flags in order to issue a warning
            click.Option(
                ["--safety-checks"],
                is_flag=True,
                default=False,
                help="Enable interactive safety checks.",
            ),
            click.Option(
                ["--no-safety-checks"],
                is_flag=True,
                default=False,
                help="Disable interactive safety checks.",
            ),
            click.Option(
                ["--json-out"],
                default="",
                help="Output the tecton state update diff (as JSON) to the file path provided.",
            ),
            click.Option(
                ["--suppress-warnings"],
                is_flag=True,
                default=False,
                help="Disable tecton plan linting warnings.",
            ),
            click.Option(
                ["--workspace"],
                default=None,
                type=WorkspaceType(),
                help="Name of the target workspace that tecton state update request applies to.",
            ),
        ]
        if not destroy:
            params.append(
                click.Option(
                    ["--skip-tests/--no-skip-tests"],
                    default=False,
                    help="Disable running tests.",
                )
            )
        if has_plan_id:
            params.append(
                click.Option(["--plan-id"], default=None, type=str, help="Id of a previously computed plan to apply.")
            )
        if allows_suppress_recreates:
            params.append(
                click.Option(
                    ["--suppress-recreates"],
                    is_flag=True,
                    default=False,
                    help="Force suppression of all recreates into in-place updates.",
                ),
            )

        super().__init__(*args, callback=callback, params=params, uses_workspace=True, **kwargs)


cli.add_command(api_key.api_key)
cli.add_command(service_account.service_account)
cli.add_command(access_control.access_control)
cli.add_command(user.user)
cli.add_command(workspace.workspace)
cli.add_command(environment.environment)
cli.add_command(
    EngineCommand(
        name="plan",
        apply=False,
        allows_suppress_recreates=True,
        help="Compare your local feature definitions with remote state and *show* the plan to bring them in sync.",
    )
)
cli.add_command(
    EngineCommand(
        name="apply",
        apply=True,
        allows_suppress_recreates=True,
        has_plan_id=True,
        help="Compare your local feature definitions with remote state and *apply* local changes to the remote.",
    )
)
cli.add_command(
    EngineCommand(
        name="upgrade",
        apply=True,
        upgrade_all=True,
        help="Upgrade remote feature definitions.",
        hidden=True,
    )
)
cli.add_command(
    EngineCommand(
        name="destroy",
        destroy=True,
        apply=True,
        help="Destroy all registered objects in this workspace.",
    )
)


@cli.command(uses_workspace=True, requires_auth=False)
@click.argument("pytest_extra_args", nargs=-1)
@click.pass_context
def test(ctx, pytest_extra_args: Tuple[str, ...]):
    """Run Tecton tests.

    USAGE:

    `tecton test`: run all tests (using PyTest) in a file that matches glob("TECTON_REPO_ROOT/**/tests/**/*.py")

    `tecton test -- -k "test_name"`: same as above, but passes the `-k "test_name"` args to the PyTest command.
    """
    # NOTE: if a user wanted to do the equivalent of a `pytest -k "test_name"`
    # they could do `tecton test -- -k "test_name"`.
    run_tests(debug=common.get_debug(ctx), pytest_extra_args=pytest_extra_args)


def py_path_to_module(path: Path, repo_root: Path) -> str:
    return str(path.relative_to(repo_root))[: -len(".py")].replace("./", "").replace("/", ".").replace("\\", ".")


def import_module_with_pretty_errors(
    file_path: Path,
    module_path: str,
    py_files: List[Path],
    repo_root: Path,
    debug: bool,
    before_error: Callable[[], None],
) -> ModuleType:
    from pyspark.sql.utils import AnalysisException

    try:
        module = importlib.import_module(module_path)
        if Path(module.__file__) != file_path:
            before_error()
            relpath = file_path.relative_to(repo_root)
            printer.safe_print(
                f"Python module name {cli_utils.bold(module_path)} ({relpath}) conflicts with module {module_path} from {module.__file__}. Please use a different name.",
                file=sys.stderr,
            )
            sys.exit(1)

        return module
    except AnalysisException as e:
        before_error()
        pretty_error(
            Path(file_path),
            py_files,
            exception=e,
            repo_root=repo_root,
            error_message="Analysis error",
            error_details=e.desc,
            debug=debug,
        )
        sys.exit(1)
    except TectonValidationError as e:
        before_error()
        pretty_error(Path(file_path), py_files, exception=e, repo_root=repo_root, error_message=e.args[0], debug=debug)
        sys.exit(1)
    except SyntaxError as e:
        before_error()
        details = None
        if e.text and e.offset:
            details = e.text + (" " * e.offset) + "^^^"
        pretty_error(
            Path(file_path),
            py_files,
            exception=e,
            repo_root=repo_root,
            error_message=e.args[0],
            error_details=details,
            debug=debug,
        )
        sys.exit(1)
    except TectonAPIInaccessibleError as e:
        before_error()
        printer.safe_print("Failed to connect to Tecton server at", e.args[1], ":", e.args[0])
        sys.exit(1)
    except Exception as e:
        before_error()
        pretty_error(Path(file_path), py_files, exception=e, repo_root=repo_root, error_message=e.args[0], debug=debug)
        sys.exit(1)


def collect_top_level_objects(
    py_files: List[Path], repo_root: Path, debug: bool, pretty_errors: bool
) -> List[base_tecton_object.BaseTectonObject]:
    modules = [py_path_to_module(p, repo_root) for p in py_files]

    with printer.safe_yaspin(yaspin.spinners.Spinners.earth, text="Importing feature repository modules") as sp:
        for file_path, module_path in zip(py_files, modules):
            sp.text = f"Processing feature repository module {module_path}"

            if pretty_errors:
                module = import_module_with_pretty_errors(
                    file_path=file_path,
                    module_path=module_path,
                    py_files=py_files,
                    repo_root=repo_root,
                    debug=debug,
                    before_error=lambda: sp.fail(printer.safe_string("⛔")),
                )
            else:
                module = importlib.import_module(module_path)

        num_modules = len(modules)
        sp.text = (
            f"Imported {num_modules} Python {plural(num_modules, 'module', 'modules')} from the feature repository"
        )
        sp.ok(printer.safe_string("✅"))

        return list(base_tecton_object._LOCAL_TECTON_OBJECTS)


def prepare_args(debug: bool) -> Tuple[List[base_tecton_object.BaseTectonObject], str, List[Path]]:
    repo_file_handler.ensure_prepare_repo()
    repo_files = repo_file_handler.repo_files()
    repo_root = repo_file_handler.repo_root()

    py_files = [p for p in repo_files if p.suffix == ".py"]
    os.chdir(repo_root)

    top_level_objects = collect_top_level_objects(py_files, repo_root=Path(repo_root), debug=debug, pretty_errors=True)

    return top_level_objects, repo_root, repo_files


def check_version():
    try:
        response = metadata_service.instance().Nop(request=empty_pb2.Empty())
        client_version_msg_info = response._headers().get(_CLIENT_VERSION_INFO_RESPONSE_HEADER)
        client_version_msg_warning = response._headers().get(_CLIENT_VERSION_WARNING_RESPONSE_HEADER)

        # Currently, only _CLIENT_VERSION_INFO_RESPONSE_HEADER and _CLIENT_VERSION_WARNING_RESPONSE_HEADER
        # metadata is used in the response, whose values have str type.
        # The returned types have 3 cases as of PR #3696:
        # - Metadata value type is List[str] if it's returned from go proxy if direct http is used.
        # - Metadata value is first str in List[str] returned from go proxy if grpc gateway is used.
        # - Metadata value type is str if direct grpc is used.
        # The default values of keys that don't exist are empty strings in any of the 3 cases.
        if client_version_msg_info:
            cli_utils.print_version_msg(client_version_msg_info)
        if client_version_msg_warning:
            cli_utils.print_version_msg(client_version_msg_warning, is_warning=True)
    except Exception as e:
        printer.safe_print("Error connecting to tecton server: ", e, file=sys.stderr)
        sys.exit(1)


@cli.command(hidden=True)
@click.pass_context
def dump(ctx) -> None:
    """Print debug info."""
    top_level_objects, _, _ = prepare_args(common.get_debug(ctx))
    dump_local_state(top_level_objects)


def get_test_paths(repo_root) -> List[str]:
    # Be _very_ careful updating this:
    #    `glob.glob` does bash-style globbing (ignores hidden files)
    #    `pathlib.Path.glob` does _not_ do bash-style glob (it shows hidden)
    #
    # Ignoring hidden files is a very important expectation for our usage of
    # pytest. Otherwise, we may test files that user does not intend us to
    # (like in their .git or .tox directories).
    #
    # NOTE: This won't filter out hidden files for Windows. Potentially:
    #    `bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)`
    # would filter hidden files for Windows, but this would need some testing.
    candidate_test_files = glob.iglob(f"{repo_root}/**/tests/**/*.py", recursive=True)

    VIRTUAL_ENV = os.getenv("VIRTUAL_ENV")
    if VIRTUAL_ENV:
        return list(filter(lambda f: not f.startswith(VIRTUAL_ENV), candidate_test_files))

    return list(candidate_test_files)


def run_tests(debug: bool, pytest_extra_args: Tuple[str, ...] = ()):
    repo_root = repo_file_handler._maybe_get_repo_root()
    if repo_root is None:
        printer.safe_print("Tecton tests must be run from a feature repo initialized using 'tecton init'!")
        sys.exit(1)

    prepare_args(debug)

    tests = get_test_paths(repo_root)
    if len(tests) == 0:
        printer.safe_print("⚠️  Running Tests: No tests found.")
        return

    os.chdir(repo_root)
    args = ["--disable-pytest-warnings", "-s", *tests]

    if pytest_extra_args:
        args.extend(pytest_extra_args)

    printer.safe_print("🏃 Running Tests")
    exitcode = pytest.main(args)

    if exitcode == 5:
        # https://docs.pytest.org/en/stable/usage.html#possible-exit-codes
        printer.safe_print("⚠️  Running Tests: No tests found.")
        return None
    elif exitcode != 0:
        printer.safe_print("⛔ Running Tests: Tests failed :(")
        sys.exit(1)
    else:
        printer.safe_print("✅ Running Tests: Tests passed!")


# TODO: This class was created to match the old style arg parse struct when we were migrating to click to avoid having
# do a deep refactoring of the code that depends on it. It should be replaced.
@dataclass
class EngineArgs:
    skip_tests: bool
    no_safety_checks: bool
    json_out: str
    suppress_warnings: bool

    debug: bool


def _no_color_convention() -> bool:
    """Follow convention for ANSI coloring of CLI tools. See no-color.org."""
    for key, value in os.environ.items():
        if key == "NO_COLOR" and value != "":
            return True
    return False


def run_engine(args: EngineArgs, apply: bool = False, destroy=False, upgrade_all=False) -> StateUpdateResult:
    check_version()

    # Resolve the json_out_filename prior to running `prepare_args(...)` so
    # that relative directories in the file name are supported (`prepare_args`
    # changes the working directory).
    json_out_path = None
    if args.json_out:
        json_out_path = Path(args.json_out).resolve()

    # Must use hasattr instead of args.plan_id, because only `apply` has the plan_id arg, but this
    # code path is also used by `plan`, `destroy`, and `upgrade`, which will fail on args.plan_id
    plan_id = None
    if hasattr(args, "plan_id"):
        plan_id = args.plan_id
    suppress_recreates = False
    if hasattr(args, "suppress_recreates") and args.suppress_recreates:
        suppress_recreates = True

    if destroy or plan_id:
        # There is no need to run tests when destroying a repo or when a plan_id is provided.
        top_level_objects: List[base_tecton_object.BaseTectonObject] = []
        repo_root = None
        repo_files: List[Path] = []
    else:
        top_level_objects, repo_root, repo_files = prepare_args(args.debug)

        if args.skip_tests == False:
            run_tests(args.debug)

    # When using server-side plan rendering, use no colors on Windows
    # or if NO_COLOR is set
    no_color = platform.system() == "Windows" or _no_color_convention()

    return update_tecton_state(
        objects=top_level_objects,
        apply=apply,
        debug=args.debug,
        interactive=not args.no_safety_checks,
        repo_files=repo_files,
        repo_root=repo_root,
        upgrade_all=upgrade_all,
        suppress_warnings=args.suppress_warnings,
        suppress_recreates=suppress_recreates,
        json_out_path=json_out_path,
        plan_id=plan_id,
        workspace_name=tecton_context.get_current_workspace(),
        no_color=no_color,
    )


@cli.command(requires_auth=False)
def init() -> None:
    """Initialize feature repo."""
    init_feature_repo()


def init_feature_repo() -> None:
    if Path().resolve() == Path.home():
        printer.safe_print("You cannot set feature repository root to the home directory", file=sys.stderr)
        sys.exit(1)

    # If .tecton exists in a parent or child directory, error out.
    repo_root = repo_file_handler._maybe_get_repo_root()
    if repo_root not in [Path().resolve(), None]:
        printer.safe_print(".tecton already exists in a parent directory:", repo_root)
        sys.exit(1)

    child_dir_matches = list(Path().rglob("*/.tecton"))
    if len(child_dir_matches) > 0:
        dirs_str = "\n\t".join((str(c.parent.resolve()) for c in child_dir_matches))
        printer.safe_print(f".tecton already exists in child directories:\n\t{dirs_str}")
        sys.exit(1)

    dot_tecton = Path(".tecton")
    if not dot_tecton.exists():
        dot_tecton.touch()
        printer.safe_print("Local feature repository root set to", Path().resolve(), "\n", file=sys.stderr)
        printer.safe_print("💡 We recommend tracking this file in git:", Path(".tecton").resolve(), file=sys.stderr)
        printer.safe_print(
            "💡 Run `tecton apply` to apply the feature repository to the Tecton cluster.", file=sys.stderr
        )
    else:
        printer.safe_print("Feature repository is already set to", Path().resolve(), file=sys.stderr)


@cli.command(uses_workspace=True)
@click.argument("commit_id", required=False)
def restore(commit_id):
    """Restore feature repo state to that of past `tecton apply`.

    The commit to restore can either be passed as COMMIT_ID, or the latest will be used.
    """
    # Get the repo download URL from the metadata service.
    request = metadata_service_pb2.GetRestoreInfoRequest(workspace=tecton_context.get_current_workspace())
    if commit_id:
        request.commit_id = commit_id
    response = metadata_service.instance().GetRestoreInfo(request)

    # Download the repo.
    url = response.signed_url_for_repo_download
    commit_id = response.commit_id
    sdk_version = response.sdk_version
    # TODO: always print this message once enough customers are on new sdk versions
    sdk_version_msg = f"applied by SDK version {sdk_version}" if sdk_version else ""
    printer.safe_print(f"Restoring from commit {commit_id} {sdk_version_msg}")
    try:
        tar_response = requests.get(url)
        tar_response.raise_for_status()
    except requests.RequestException as e:
        raise SystemExit(e)

    # Find the repo root or initialize a default repot if not in a repo.
    root = repo_file_handler._maybe_get_repo_root()
    if not root:
        init_feature_repo()
        root = Path().resolve()
    repo_file_handler.ensure_prepare_repo()

    # Get user confirmation.
    repo_files = repo_file_handler.repo_files()
    if len(repo_files) > 0:
        for f in repo_files:
            printer.safe_print(f)
        cli_utils.confirm_or_exit("This operation may delete or modify the above files. Ok?")
        for f in repo_files:
            os.remove(f)

    # Extract the feature repo.
    with tarfile.open(fileobj=io.BytesIO(tar_response.content), mode="r|gz") as tar:
        for entry in tar:
            if os.path.isabs(entry.name) or ".." in entry.name:
                msg = "Illegal tar archive entry"
                raise ValueError(msg)
            elif os.path.exists(root / Path(entry.name)):
                msg = f"tecton restore would overwrite an unexpected file: {entry.name}"
                raise ValueError(msg)
            tar.extract(entry, path=root)
    printer.safe_print("Success")


@cli.command(uses_workspace=True)
@click.option("--limit", default=10, type=int, help="Number of log entries to return.")
def log(limit):
    """View log of past `tecton apply`."""
    request = metadata_service_pb2.GetStateUpdateLogRequest(
        workspace=tecton_context.get_current_workspace(), limit=limit
    )
    response = metadata_service.instance().GetStateUpdateLog(request)
    for entry in response.entries:
        # Use f-string left alignment for a better looking format
        printer.safe_print(f"{'Apply ID: ' : <15}{entry.commit_id}")
        printer.safe_print(
            f"{'Author: ' : <15}{cli_utils.display_principal(entry.applied_by_principal, entry.applied_by)}"
        )
        printer.safe_print(f"{'Date: ' : <15}{entry.applied_at.ToDatetime()}")
        if entry.sdk_version:
            printer.safe_print(f"{'SDK Version: ' : <15}{entry.sdk_version}")
        printer.safe_print()


@cli.command(requires_auth=False)
@click.argument("tecton_url", required=False)
@click.option(
    "--manual/--no-manual",
    default=False,
    help="Manually require user to open browser and paste login token. Needed when using the Tecton CLI in a headless environment.",
)
@click.option("--okta-session-token", default=None, hidden=True, required=False)
def login(tecton_url: Optional[str], manual: bool, okta_session_token: Optional[str]):
    """Log in and authenticate Tecton CLI.

    The Tecton URL may be optionally passed on the command line as TECTON_URL, otherwise you will be prompted."""

    host = _cluster_url()

    if tecton_url is None:
        printer.safe_print("Enter configuration. Press enter to use current value")
        prompt = "Tecton Cluster URL [%s]: " % (host or "no current value. example: https://yourco.tecton.ai")
        new_host = input(prompt).strip()
        if new_host:
            host = new_host
    else:
        host = tecton_url

    if okta_session_token:
        auth_flow_type = okta.AuthFlowType.SESSION_TOKEN
    elif manual:
        auth_flow_type = okta.AuthFlowType.BROWSER_MANUAL
    else:
        auth_flow_type = okta.AuthFlowType.BROWSER_HANDS_FREE
    credentials._login_helper(host=host, auth_flow_type=auth_flow_type, okta_session_token=okta_session_token)


@cli.command()
@click.option(
    "--workspace",
    default=None,
    type=WorkspaceType(),
    help="Name of the target workspace that tecton state update request applies to.",
)
def freshness(workspace):
    """Feature freshness for Feature Views in the current workspace."""
    # TODO: use GetAllFeatureFreshnessRequest once we implement Chronosphere based API.
    workspace_name = workspace if workspace else tecton_context.get_current_workspace()
    workspace_utils.check_workspace_exists(workspace_name)
    freshness_statuses = get_all_freshness(workspace_name)
    num_fvs = len(freshness_statuses)
    if num_fvs == 0:
        printer.safe_print("No Feature Views found in this workspace.")
        return

    printer.safe_print(format_freshness_table(freshness_statuses))


@cli.command()
@click.option(
    "--workspace",
    default=None,
    type=WorkspaceType(),
    help="The workspace page that should be opened up to. Defaults to the current selected workspace.",
)
@click.option(
    "--print/--no-print", "-p", "print_", default=False, help="Print the URL instead of automatically opening it."
)
def web(workspace, print_) -> None:
    """Opens a browser window to your Tecton account and workspace."""
    workspace_name = workspace if workspace else tecton_context.get_current_workspace()
    if workspace_name:
        web_url = urllib.parse.urljoin(_cluster_url(), f"app/repo/{workspace_name}/")
    else:
        web_url = urllib.parse.urljoin(_cluster_url(), "app")

    if print_:
        printer.safe_print(f"Web URL: {web_url}")
    else:
        printer.safe_print(f"Opening {web_url}")
        # Sleep before opening the browser to improve the UX and make it less jarring.
        time.sleep(1)
        click.launch(web_url)


@cli.command()
def whoami():
    """Show the current User or API Key used to authenticate with Tecton"""

    profile = credentials.who_am_i()
    if profile and isinstance(profile, okta.UserProfile):
        cli_utils.pprint_dict({"Tecton Endpoint": _cluster_url()}, colwidth=16)
        key_map = {"id": "ID", "email": "Email", "name": "Name"}
        cli_utils.pprint_attr_obj(key_map, profile, colwidth=16)
    elif profile and isinstance(profile, credentials.ServiceAccountProfile):
        cli_utils.pprint_dict({"Tecton Endpoint": _cluster_url()}, colwidth=19)
        service_account = {
            "Service Account ID": profile.id,
            "Secret Key": profile.obscured_key,
            "Name": profile.name,
            "Description": profile.description,
            "Created by": profile.created_by,
        }
        cli_utils.pprint_dict(service_account, colwidth=19)
    else:
        cli_utils.pprint_dict({"Tecton Endpoint": _cluster_url()}, colwidth=16)
        printer.safe_print(
            "Tecton credentials are not configured or have expired. Run `tecton login` or set an "
            "API Key to authenticate"
        )


@cli.command()
@click.pass_context
@click.argument("feature_view_name")
@click.option("--limit", default=100, type=int, help="Set the maximum limit of results.")
@click.option("--errors-only/--no-errors-only", default=False, help="Only show errors.")
@click.option(
    "--workspace",
    default=None,
    type=WorkspaceType(),
    help="Name of the target workspace that tecton state update request applies to.",
)
def materialization_status(ctx, feature_view_name, limit, errors_only, workspace):
    """Show materialization status information for a FeatureView with FEATURE_VIEW_NAME in the current workspace.

    Prepend the --verbose flag for more information."""

    # Fetch FeatureView
    workspace_name = workspace if workspace else tecton_context.get_current_workspace()
    workspace_utils.check_workspace_exists(workspace_name)
    fv_request = metadata_service_pb2.GetFeatureViewRequest(
        version_specifier=feature_view_name, workspace=workspace_name
    )
    fv_response = metadata_service.instance().GetFeatureView(fv_request)
    fco_container = FcoContainer.from_proto(fv_response.fco_container)
    fv_spec = fco_container.get_single_root()
    if fv_spec is None:
        printer.safe_print(f"Feature view '{feature_view_name}' not found.")
        sys.exit(1)
    fv_id = IdHelper.from_string(fv_spec.id)

    # Fetch Materialization Status
    status_request = metadata_service_pb2.GetMaterializationStatusRequest(
        feature_package_id=fv_id, workspace=workspace_name
    )
    status_response = metadata_service.instance().GetMaterializationStatus(status_request)

    column_names, materialization_status_rows = format_materialization_attempts(
        status_response.materialization_status.materialization_attempts,
        verbose=common.get_verbose(ctx),
        limit=limit,
        errors_only=errors_only,
    )

    # Setting `max_width=0` creates a table with an unlimited width.
    table = Displayable.from_table(headings=column_names, rows=materialization_status_rows, max_width=0)
    # Align columns in the middle horizontally
    table._text_table.set_cols_align(["c" for _ in range(len(column_names))])
    printer.safe_print(table)


def main():
    try:
        cli()
    finally:
        metadata_service.close_instance()


if __name__ == "__main__":
    main()
