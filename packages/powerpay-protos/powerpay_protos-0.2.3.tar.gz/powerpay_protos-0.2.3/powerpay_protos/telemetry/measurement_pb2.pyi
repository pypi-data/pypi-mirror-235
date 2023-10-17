from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnergyMeasurementUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ENERGY_UNIT_NOT_SET: _ClassVar[EnergyMeasurementUnit]
    WATT_HOUR: _ClassVar[EnergyMeasurementUnit]
    KILO_WATT_HOUR: _ClassVar[EnergyMeasurementUnit]
    MEGA_WATT_HOUR: _ClassVar[EnergyMeasurementUnit]

class PowerMeasurementUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    POWER_UNIT_NOT_SET: _ClassVar[PowerMeasurementUnit]
    WATT: _ClassVar[PowerMeasurementUnit]
    KILO_WATT: _ClassVar[PowerMeasurementUnit]
    MEGA_WATT: _ClassVar[PowerMeasurementUnit]
ENERGY_UNIT_NOT_SET: EnergyMeasurementUnit
WATT_HOUR: EnergyMeasurementUnit
KILO_WATT_HOUR: EnergyMeasurementUnit
MEGA_WATT_HOUR: EnergyMeasurementUnit
POWER_UNIT_NOT_SET: PowerMeasurementUnit
WATT: PowerMeasurementUnit
KILO_WATT: PowerMeasurementUnit
MEGA_WATT: PowerMeasurementUnit

class Measurement(_message.Message):
    __slots__ = ["energy_measurement", "power_measurement", "energized_measurement", "session_measurement", "signal_strength"]
    ENERGY_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    POWER_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    ENERGIZED_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    energy_measurement: EnergyMeasurement
    power_measurement: PowerMeasurement
    energized_measurement: EnergizedMeasurement
    session_measurement: SessionMeasurement
    signal_strength: SignalStrength
    def __init__(self, energy_measurement: _Optional[_Union[EnergyMeasurement, _Mapping]] = ..., power_measurement: _Optional[_Union[PowerMeasurement, _Mapping]] = ..., energized_measurement: _Optional[_Union[EnergizedMeasurement, _Mapping]] = ..., session_measurement: _Optional[_Union[SessionMeasurement, _Mapping]] = ..., signal_strength: _Optional[_Union[SignalStrength, _Mapping]] = ...) -> None: ...

class EnergyMeasurement(_message.Message):
    __slots__ = ["value", "unit", "type"]
    class EnergyMeasurementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ENERGY_MEASUREMENT_TYPE_NOT_SET: _ClassVar[EnergyMeasurement.EnergyMeasurementType]
        LIFETIME: _ClassVar[EnergyMeasurement.EnergyMeasurementType]
        SESSION: _ClassVar[EnergyMeasurement.EnergyMeasurementType]
    ENERGY_MEASUREMENT_TYPE_NOT_SET: EnergyMeasurement.EnergyMeasurementType
    LIFETIME: EnergyMeasurement.EnergyMeasurementType
    SESSION: EnergyMeasurement.EnergyMeasurementType
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: EnergyMeasurementUnit
    type: EnergyMeasurement.EnergyMeasurementType
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[EnergyMeasurementUnit, str]] = ..., type: _Optional[_Union[EnergyMeasurement.EnergyMeasurementType, str]] = ...) -> None: ...

class PowerMeasurement(_message.Message):
    __slots__ = ["value", "unit"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: PowerMeasurementUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[PowerMeasurementUnit, str]] = ...) -> None: ...

class EnergizedMeasurement(_message.Message):
    __slots__ = ["value"]
    class EnergizedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ENERGIZED_STATE_UNDEFINED: _ClassVar[EnergizedMeasurement.EnergizedState]
        ENERGIZED: _ClassVar[EnergizedMeasurement.EnergizedState]
        DE_ENERGIZED: _ClassVar[EnergizedMeasurement.EnergizedState]
    ENERGIZED_STATE_UNDEFINED: EnergizedMeasurement.EnergizedState
    ENERGIZED: EnergizedMeasurement.EnergizedState
    DE_ENERGIZED: EnergizedMeasurement.EnergizedState
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: EnergizedMeasurement.EnergizedState
    def __init__(self, value: _Optional[_Union[EnergizedMeasurement.EnergizedState, str]] = ...) -> None: ...

class SessionMeasurement(_message.Message):
    __slots__ = ["start", "end", "session_consumed_energy", "meter_start", "meter_end"]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    SESSION_CONSUMED_ENERGY_FIELD_NUMBER: _ClassVar[int]
    METER_START_FIELD_NUMBER: _ClassVar[int]
    METER_END_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    session_consumed_energy: EnergyMeasurement
    meter_start: EnergyMeasurement
    meter_end: EnergyMeasurement
    def __init__(self, start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., session_consumed_energy: _Optional[_Union[EnergyMeasurement, _Mapping]] = ..., meter_start: _Optional[_Union[EnergyMeasurement, _Mapping]] = ..., meter_end: _Optional[_Union[EnergyMeasurement, _Mapping]] = ...) -> None: ...

class SignalStrength(_message.Message):
    __slots__ = ["value", "unit", "radio_type"]
    class SignalStrengthUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SIGNAL_STRENGTH_UNIT_NOT_SET: _ClassVar[SignalStrength.SignalStrengthUnit]
        DECIBEL_MILLIWATT: _ClassVar[SignalStrength.SignalStrengthUnit]
        RECEIVED_SIGNAL_STRENGTH_INDICATOR: _ClassVar[SignalStrength.SignalStrengthUnit]
        SIGNAL_NOISE_RATIO: _ClassVar[SignalStrength.SignalStrengthUnit]
    SIGNAL_STRENGTH_UNIT_NOT_SET: SignalStrength.SignalStrengthUnit
    DECIBEL_MILLIWATT: SignalStrength.SignalStrengthUnit
    RECEIVED_SIGNAL_STRENGTH_INDICATOR: SignalStrength.SignalStrengthUnit
    SIGNAL_NOISE_RATIO: SignalStrength.SignalStrengthUnit
    class RadioType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        RADIO_TYPE_NOT_SET: _ClassVar[SignalStrength.RadioType]
        CELLULAR: _ClassVar[SignalStrength.RadioType]
        WIFI: _ClassVar[SignalStrength.RadioType]
        LORA: _ClassVar[SignalStrength.RadioType]
    RADIO_TYPE_NOT_SET: SignalStrength.RadioType
    CELLULAR: SignalStrength.RadioType
    WIFI: SignalStrength.RadioType
    LORA: SignalStrength.RadioType
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    RADIO_TYPE_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: SignalStrength.SignalStrengthUnit
    radio_type: SignalStrength.RadioType
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[SignalStrength.SignalStrengthUnit, str]] = ..., radio_type: _Optional[_Union[SignalStrength.RadioType, str]] = ...) -> None: ...
