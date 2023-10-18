import math
import shutil
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from dataclasses import dataclass
from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import List
from typing import Optional

import click
import requests
from google.protobuf import timestamp_pb2
from tqdm import tqdm

from tecton._internals import metadata_service
from tecton.cli import printer
from tecton.cli.cli_utils import display_table
from tecton.cli.command import TectonGroup
from tecton.cli.environment_utils import download_dependencies
from tecton.cli.environment_utils import resolve_dependencies
from tecton_core import id_helper
from tecton_proto.common.container_image_pb2 import ContainerImage
from tecton_proto.data.remote_compute_environment_pb2 import ObjectStoreUploadPart
from tecton_proto.data.remote_compute_environment_pb2 import RemoteEnvironmentStatus
from tecton_proto.data.remote_compute_environment_pb2 import RemoteEnvironmentUploadInfo
from tecton_proto.data.remote_compute_environment_pb2 import S3UploadInfo
from tecton_proto.data.remote_compute_environment_pb2 import S3UploadPart
from tecton_proto.remoteenvironmentservice.remote_environment_service_pb2 import CompletePackagesUploadRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service_pb2 import CreateRemoteEnvironmentRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service_pb2 import DeleteRemoteEnvironmentsRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service_pb2 import GetPackagesUploadUrlRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service_pb2 import ListRemoteEnvironmentsRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service_pb2 import StartPackagesUploadRequest


DEFAULT_PYTHON_VERSION = "3.8"
RESOLVED_REQUIREMENTS_FILENAME = "resolved_requirements.txt"
ERROR_MESSAGE_PREFIX = "⛔ ERROR: "
DEBUG_MESSAGE_PREFIX = "🔎 "
DEPENDENCY_RESOLUTION_TIMEOUT_SECONDS = 60

# boto3 defaults to 8MB for multi-part uploads using upload_file.
DEFAULT_UPLOAD_PART_SIZE_MB = 16

# 5 was arbitrarily selected. We want to be conservative as this will run in customer's environments
DEFAULT_MAX_WORKERS_THREADS = 5

# The maximum size of all dependencies allowed for upload
MAX_ALLOWED_DEPENDENCIES_SIZE_GB = 2

MEGABYTE = 1024 * 1024
GIGABYTE = 1024 * MEGABYTE


@dataclass
class UploadPart:
    """
    Represents an individual part of a file that needs to be uploaded in chunks or parts.
    :param part_number (int): The 1-indexed number of the part to be uploaded.
    :param offset (int): The starting byte offset of this part in the file.
    :param part_size (int): The size of this part in bytes.
    """

    part_number: int
    offset: int
    part_size: int


@click.command("environment", cls=TectonGroup)
def environment():
    """Manage Environments for ODFV Execution"""


@environment.command("list-all")
def list_all():
    """List all available Python Environments"""
    remote_environments = _list_environments()
    _display_environments(remote_environments)


@environment.command("list")
@click.option("--id", help="Environment Id", required=False, type=str)
@click.option("--name", help="Environment Name", required=False, type=str)
def list(id: Optional[str] = None, name: Optional[str] = None):
    """List Python Environment(s) matching a name or an ID"""
    if not id and not name:
        remote_environments = _list_environments()
        _display_environments(remote_environments)
    else:
        identifier = name if name is not None else id
        by_name = name is not None
        remote_environments = _list_environments(identifier=identifier, by_name=by_name)
        _display_environments(remote_environments)


@environment.command("create")
@click.option("-n", "--name", help="Environment name", required=True, type=str)
@click.option("-d", "--description", help="Environment description", required=True, type=str)
@click.option(
    "-r", "--requirements", help="Path to requirements.txt file", required=False, type=click.Path(exists=True)
)
@click.option("-p", "--python-version", help="Python Version for the environment")
@click.option(
    "-i", "--image-uri", help="Image URI. This functionality is in Private Preview.", required=False, type=str
)
@click.option("--debug", help="Activate debug mode", is_flag=True)
def create(
    name: str,
    description: str,
    requirements: Optional[str] = None,
    python_version: Optional[str] = None,
    image_uri: Optional[str] = None,
    debug: Optional[bool] = False,
):
    """Create a custom Python Environment
    Parameters:
       name (str): The name of the environment.
       description (str): The description of the environment.
       requirements (str, optional): The path to the requirements.txt file containing all dependencies for the environment
       python_version (str, optional): The Python version to use, defaults to "3.8"
       image_uri (str, optional): The URI of the image to use for the environment. This functionality is in Private Preview.
       debug (bool, optional): Activates debug mode. When set to True, the command provides detailed output, including subcommands and diagnostic information, to assist in troubleshooting.
    """
    if image_uri is not None and requirements is not None:
        printer.safe_print(
            f"{ERROR_MESSAGE_PREFIX} Exactly one of parameters `requirements` and `image_uri` must be specified.",
            file=sys.stderr,
        )
        sys.exit(1)
    if image_uri is not None:
        resp = _create_environment_with_image(name, description, image_uri)
        _display_environments([resp.remote_environment])
    elif requirements is not None:
        _python_version = python_version or DEFAULT_PYTHON_VERSION
        requirements_path = Path(requirements)
        resp = _create_environment_with_requirements(name, description, requirements_path, _python_version, debug=debug)
        if resp:
            _display_environments([resp.remote_environment])
            printer.safe_print(
                f"\n🎉 Successfully created environment {name} with Status=PENDING. Please run `tecton environment list <environment-name>` to monitor the status of the environment"
            )
    else:
        printer.safe_print(
            f"{ERROR_MESSAGE_PREFIX} Please specify the path to a `requirements.txt` file via the `requirements` parameter to create an environment",
            file=sys.stderr,
        )
        sys.exit(1)


# Enable environment deletion in 0.8
'''
@environment.command("delete")
@click.option("--id", help="Environment ID", required=False, type=str)
@click.option("--name", help="Environment Name", required=False, type=str)
def delete(id: Optional[str] = None, name: Optional[str] = None):
    """Delete an existing custom Python Environment by name or an ID"""
    if id is None and name is None:
        printer.safe_print("At least one of `id` or `name` must be provided", file=sys.stderr)
        sys.exit(1)

    identifier = name if name is not None else id
    by_name = name is not None
    environments = _list_environments(identifier=identifier, by_name=by_name)
    if not environments:
        printer.safe_print(
            f"No matching environments found for: {identifier}. Please verify available environments using the `list_all` command",  file=sys.stderr
        )
    elif len(environments) > 1:
        printer.safe_print(
            f"No matching environment found for: {identifier}. Did you mean one of the following environment(s)? \n\n", file=sys.stderr
        )
        _display_environments(environments)
    else:
        environment_to_delete = environments[0]
        confirmation_text = f"Are you sure you want to delete environment {environment_to_delete.name}? (y/n) :"
        confirmation = input(confirmation_text).lower().strip()
        if confirmation == "y":
            try:
                _delete_environment(env_id=environment_to_delete.id)
                printer.safe_print(f"Successfully deleted environment: {identifier}")
            except Exception as e:
                printer.safe_print(f"Failed to delete. error = {str(e)}, type= {type(e).__name__}")
        else:
            printer.safe_print(f"Cancelled deletion for environment: {identifier}")
'''


def _display_environments(environments: list):
    headings = ["Id", "Name", "Status", "Created At", "Updated At"]
    display_table(
        headings,
        [
            (
                i.id,
                i.name,
                RemoteEnvironmentStatus.Name(i.status),
                _timestamp_to_string(i.created_at),
                _timestamp_to_string(i.updated_at),
            )
            for i in environments
        ],
    )


def _create_environment_with_image(name: str, description: str, image_uri):
    try:
        req = CreateRemoteEnvironmentRequest()
        req.name = name
        req.description = description

        image_info = ContainerImage()
        image_info.image_uri = image_uri

        req.image_info.CopyFrom(image_info)

        return metadata_service.instance().CreateRemoteEnvironment(req)
    except PermissionError as e:
        printer.safe_print(
            "The user is not authorized to create environment(s) in Tecton. Please reach out to your Admin to complete this "
            "action",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        printer.safe_print(f"Failed to create environment: {e}", file=sys.stderr)
        sys.exit(1)


def _create_environment_with_requirements(
    name: str,
    description: str,
    requirements_path: Path,
    python_version: str,
    debug: bool,
):
    """Create a custom environment by resolving dependencies, downloading wheels and updating MDS
    Parameters:
        name(str): Name of the custom environment
        description(str): Description of the custom environment
        requirements_path(str): Path to the `requirements.txt` file
        python_version(str): The Python version to resolve the dependencies for
        debug(bool): Activate debug mode
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        printer.safe_print("\n⏳ Resolving Dependencies. This may take a few seconds.....")
        resolved_requirements_path = Path(tmpdir) / RESOLVED_REQUIREMENTS_FILENAME
        try:
            resolve_dependencies(
                python_version=python_version,
                requirements_path=requirements_path,
                resolved_requirements_path=resolved_requirements_path,
                timeout_seconds=DEPENDENCY_RESOLUTION_TIMEOUT_SECONDS,
                debug=debug,
            )
        except ValueError as e:
            printer.safe_print(f"{ERROR_MESSAGE_PREFIX} {e}", file=sys.stderr)
            sys.exit(1)
        printer.safe_print("✅ Successfully resolved dependencies")

        download_wheels_dir = Path(tmpdir) / "wheels"
        download_wheels_dir.mkdir()
        printer.safe_print("\n⏳ Downloading wheels. This may take a few seconds.....\n")
        download_dependencies(
            requirements_path=resolved_requirements_path,
            target_directory=download_wheels_dir,
            python_version=python_version,
            debug=debug,
        )
        printer.safe_print("\n✅ Successfully downloaded dependencies")

        directory_size = _get_directory_size(download_wheels_dir)
        if directory_size > (MAX_ALLOWED_DEPENDENCIES_SIZE_GB * GIGABYTE):
            printer.safe_print(
                f"{ERROR_MESSAGE_PREFIX} The total size of the downloaded dependencies exceeds the max allowed limit of {MAX_ALLOWED_DEPENDENCIES_SIZE_GB}GB. Please reduce the total number / size of dependencies and try again!",
                file=sys.stderr,
            )
            sys.exit(1)

        printer.safe_print("\n⏳ Uploading compressed wheels in parts to S3. This may take a few seconds.....")
        environment_id = id_helper.IdHelper.generate_string_id()
        try:
            location = _upload_dependencies(source_path=download_wheels_dir, environment_id=environment_id, debug=debug)
        except ValueError as e:
            printer.safe_print(f"{ERROR_MESSAGE_PREFIX} Unable to upload dependencies - {e}", file=sys.stderr)
            return

        req = CreateRemoteEnvironmentRequest(
            name=name,
            id=environment_id,
            description=description,
            python_version=python_version,
            s3_wheels_location=location,
        )
        return metadata_service.instance().CreateRemoteEnvironment(req)


def _delete_environment(env_id: str):
    try:
        req = DeleteRemoteEnvironmentsRequest()
        req.ids.append(env_id)
        return metadata_service.instance().DeleteRemoteEnvironments(req)
    except PermissionError as e:
        printer.safe_print(
            "The user is not authorized to perform environment deletion. Please reach out to your Admin to complete this action",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        printer.safe_print(f"Failed to delete environment: {e}", file=sys.stderr)
        sys.exit(1)


def _list_environments(identifier: Optional[str] = None, by_name: bool = False):
    try:
        req = ListRemoteEnvironmentsRequest()
        response = metadata_service.instance().ListRemoteEnvironments(req)

        if identifier is None:
            return response.remote_environments

        if by_name:
            environments = [env for env in response.remote_environments if identifier in env.name]
            error_message = f"Unable to find environments with name: {identifier}"
        else:
            environments = [env for env in response.remote_environments if identifier in env.id]
            error_message = f"Unable to find environment with id: {identifier}"

        if len(environments) < 1:
            printer.safe_print(error_message, file=sys.stderr)
            sys.exit(1)

        return environments

    except Exception as e:
        printer.safe_print(f"Failed to fetch environments: {e}", file=sys.stderr)
        sys.exit(1)


def _timestamp_to_string(value: timestamp_pb2.Timestamp) -> str:
    t = datetime.fromtimestamp(value.ToSeconds())
    return t.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")


def _upload_dependencies(source_path: Path, environment_id: str, debug: bool) -> str:
    """Upload dependencies from the specified source path to S3.
    Args:
        source_path (str): The path to the dependencies to upload.
        environment_id (str): The ID of the environment.
        debug (bool): Print debug information
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        output_zip_file = Path(tmpdir) / "wheels.zip"
        if debug:
            printer.safe_print(f"{DEBUG_MESSAGE_PREFIX} Zipping dependencies at {output_zip_file}")

        shutil.make_archive(str(output_zip_file.with_suffix("")), "zip", str(source_path))
        file_size = output_zip_file.stat().st_size

        if debug:
            printer.safe_print(f"{DEBUG_MESSAGE_PREFIX} Initiating Multi-Part Upload")
        start_request = StartPackagesUploadRequest(environment_id=environment_id)
        start_response = metadata_service.instance().StartPackagesUpload(start_request)

        upload_id = start_response.upload_info.s3_upload_info.upload_id
        upload_parts = _upload_file_in_parts(
            file_size=file_size,
            upload_id=upload_id,
            environment_id=environment_id,
            output_zip_file=output_zip_file,
        )

        complete_request = CompletePackagesUploadRequest(
            upload_info=RemoteEnvironmentUploadInfo(
                environment_id=environment_id,
                s3_upload_info=S3UploadInfo(upload_id=upload_id, upload_parts=upload_parts),
            )
        )
        complete_response = metadata_service.instance().CompletePackagesUpload(complete_request)
        location = complete_response.storage_location
        printer.safe_print("✅ Successfully uploaded dependencies")
        return location


def _upload_file_in_parts(
    file_size: int, upload_id: str, environment_id: str, output_zip_file: Path
) -> List[S3UploadPart]:
    """Upload a file in parallel, dividing it into parts.
    Args:
        file_size (int): The size of the file in bytes.
        upload_id (str): A unique identifier for the file upload, returned by S3.
        environment_id (str): The ID of the environment.
        output_zip_file (str): The path to the file to upload.
    Returns:
        list: A list of upload part results.
    """
    # Calculate all parts for multi part upload
    part_data_list = get_upload_parts(file_size=file_size)
    with ThreadPoolExecutor(DEFAULT_MAX_WORKERS_THREADS) as executor:
        upload_futures = [
            executor.submit(
                _upload_part,
                upload_part=part_data,
                parent_upload_id=upload_id,
                environment_id=environment_id,
                dependency_file_path=output_zip_file,
            )
            for part_data in part_data_list
        ]
        with tqdm(total=len(part_data_list), desc="Upload progress", ncols=100) as pbar:
            for future in as_completed(upload_futures):
                # Increment the tqdm progress bar whenever a future is done
                if future.result():
                    pbar.update(1)

        return [future.result() for future in upload_futures]


def get_upload_parts(file_size: int) -> List[UploadPart]:
    """
    Calculate UploadPart for each part of a file to be uploaded, given total file size.
    It considers the DEFAULT_UPLOAD_PART_SIZE_MB as the maximum size of each part.
    Args:
        file_size (int): The total size of the file being uploaded in bytes.
    Returns:
        List[UploadPart]: An list of UploadPart representing all parts to be uploaded with its part number,
                    starting offset, and size in bytes.
    """
    total_parts = _calculate_part_count(file_size, DEFAULT_UPLOAD_PART_SIZE_MB)
    chunk_size = DEFAULT_UPLOAD_PART_SIZE_MB * MEGABYTE
    upload_parts = []
    for i in range(1, total_parts + 1):
        offset = chunk_size * (i - 1)
        bytes_remaining = file_size - offset
        # Adjust the size for the last part if the remaining bytes are less than the DEFAULT_UPLOAD_PART_SIZE_MB
        current_chunk_size = chunk_size if bytes_remaining > chunk_size else bytes_remaining
        upload_parts.append(UploadPart(part_number=i, offset=offset, part_size=current_chunk_size))
    return upload_parts


def _get_directory_size(directory: Path) -> int:
    """
    Compute the size of a directory in bytes.
    Args:
        directory (Path): The directory path for which to compute the size.
    Returns:
        int: The size of the directory in bytes.
    """
    return sum(f.stat().st_size for f in directory.rglob("*") if f.is_file())


def _calculate_part_count(file_size: int, part_size_mb: int) -> int:
    """Calculate the number of parts the file will be divided into for uploading.
    Args:
        file_path (str): The path to the file to upload.
        part_size_mb (int): The size of each part in megabytes.
    Returns:
        int: The total number of parts.
    """
    chunk_size = part_size_mb * 1024 * 1024
    return int(math.ceil(file_size / chunk_size))


def _upload_part(
    upload_part: UploadPart,
    parent_upload_id: str,
    environment_id: str,
    dependency_file_path: str,
):
    """Upload a part of a file.
    Args:
        upload_part (UploadPart): The part to upload.
        parent_upload_id (str): The ID of the parent upload.
        environment_id (str): The ID of the environment.
        dependency_file_path (str): The path to the file to upload.
    Returns:
        S3UploadPart: An object representing the uploaded part.
    """
    request = GetPackagesUploadUrlRequest(
        environment_id=environment_id,
        upload_part=ObjectStoreUploadPart(
            s3_upload_part=S3UploadPart(parent_upload_id=parent_upload_id, part_number=upload_part.part_number)
        ),
    )
    response = metadata_service.instance().GetPackagesUploadUrl(request)
    signed_url = response.upload_url

    with open(dependency_file_path, "rb") as fp:
        fp.seek(upload_part.offset)
        file_data = fp.read(upload_part.part_size)
        response = requests.put(signed_url, data=file_data)
        if response.ok:
            e_tag = response.headers["ETag"]
            return S3UploadPart(part_number=upload_part.part_number, e_tag=e_tag, parent_upload_id=parent_upload_id)
        else:
            msg = f"Upload failed with status {response.status_code} and error {response.text}"
            raise ValueError(msg)
