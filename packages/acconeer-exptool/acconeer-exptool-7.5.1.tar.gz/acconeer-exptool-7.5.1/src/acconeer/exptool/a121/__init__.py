# Copyright (c) Acconeer AB, 2022-2023
# All rights reserved

SDK_VERSION = "1.3.0"

# Make these visible under the a121 package to not break api
from acconeer.exptool._core.entities import ClientInfo, MockInfo, SerialInfo, SocketInfo, USBInfo

from ._cli import ExampleArgumentParser, get_client_args
from ._core import (
    _H5PY_STR_DTYPE,
    PRF,
    Client,
    ClientError,
    H5Record,
    H5Recorder,
    IdleState,
    InMemoryRecord,
    Metadata,
    PersistentRecord,
    Profile,
    Record,
    Recorder,
    RecordError,
    Result,
    SensorCalibration,
    SensorConfig,
    SensorInfo,
    ServerError,
    ServerInfo,
    SessionConfig,
    StackedResults,
    SubsweepConfig,
    ValidationError,
    ValidationResult,
    ValidationWarning,
    complex_array_to_int16_complex,
    int16_complex_array_to_complex,
    iterate_extended_structure,
    iterate_extended_structure_values,
    load_record,
    open_record,
    save_record,
    save_record_to_h5,
    zip3_extended_structures,
    zip_extended_structures,
)
from ._core_ext import _ReplayingClient, _StopReplay
from ._perf_calc import (
    _SensorPerformanceCalc,
    _SessionPerformanceCalc,
    get_point_overhead_duration,
    get_sample_duration,
)
from ._rate_calc import _RateCalculator, _RateStats
