import datetime

import attrs
from google.protobuf.duration_pb2 import Duration

from tecton_core.time_utils import to_human_readable_str
from tecton_proto.args.feature_view_pb2 import TimeWindow as TimeWindowArgs
from tecton_proto.common.time_window_pb2 import TimeWindow


# TODO(sanika): Refactor TimeWindowWrapper to TimeWindowSpec and move it under the specs module
@attrs.frozen(order=True)
class TimeWindowWrapper:
    # window_start and window_end are both negative timedeltas as window_end represents the offset and window_start
    # represents the offset - window_duration
    window_start: datetime.timedelta
    window_end: datetime.timedelta

    @classmethod
    def from_data(cls, time_window: TimeWindow) -> "TimeWindowWrapper":
        return cls(
            window_start=time_window.window_start.ToTimedelta(),
            window_end=time_window.window_end.ToTimedelta(),
        )

    @classmethod
    def from_args(cls, time_window: TimeWindowArgs) -> "TimeWindowWrapper":
        return cls(
            window_start=Duration(
                seconds=time_window.offset.seconds - time_window.window_duration.seconds,
                nanos=time_window.offset.nanos - time_window.window_duration.nanos,
            ).ToTimedelta(),
            window_end=Duration(seconds=time_window.offset.seconds, nanos=time_window.offset.nanos).ToTimedelta(),
        )

    @property
    def window_duration(self) -> datetime.timedelta:
        return self.window_end - self.window_start

    @property
    def offset(self) -> datetime.timedelta:
        return self.window_end

    def to_tuple(self) -> tuple:
        return (self.window_start, self.window_end)

    def to_string(self) -> str:
        offset_name = "_offset_" + to_human_readable_str(-self.offset) if self.offset.total_seconds() < 0 else ""
        return f"{to_human_readable_str(self.window_duration)}{offset_name}"
