"""Contains schedule decoder."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from functools import lru_cache
from itertools import chain
from typing import TYPE_CHECKING, Final

from pyplumio.const import ATTR_PARAMETER, ATTR_SCHEDULE, ATTR_SWITCH, ATTR_TYPE
from pyplumio.devices import Addressable, Device
from pyplumio.exceptions import FrameDataError
from pyplumio.helpers.factory import factory
from pyplumio.helpers.parameter import BinaryParameter, Parameter, ParameterDescription
from pyplumio.helpers.typing import EventDataType, ParameterDataType
from pyplumio.structures import Structure, ensure_device_data
from pyplumio.util import unpack_parameter

if TYPE_CHECKING:
    from pyplumio.frames import Request
else:
    Request = object

ATTR_SCHEDULES: Final = "schedules"
ATTR_SCHEDULE_PARAMETERS: Final = "schedule_parameters"
ATTR_SCHEDULE_SWITCH: Final = "schedule_switch"
ATTR_SCHEDULE_PARAMETER: Final = "schedule_parameter"

SCHEDULE_SIZE: Final = 42  # 6 bytes per day, 7 days total

SCHEDULES: tuple[str, ...] = (
    "heating",
    "water_heater",
    "circulation_pump",
    "boiler_work",
    "boiler_clean",
    "hear_exchanger_clean",
    "mixer_1",
    "mixer_2",
    "mixer_3",
    "mixer_4",
    "mixer_5",
    "mixer_6",
    "mixer_7",
    "mixer_8",
    "mixer_9",
    "mixer_10",
    "thermostat_1",
    "thermostat_2",
    "thermostat_3",
    "circuit_1",
    "circuit_2",
    "circuit_3",
    "circuit_4",
    "circuit_5",
    "circuit_6",
    "circuit_7",
    "panel_1",
    "panel_2",
    "panel_3",
    "panel_4",
    "panel_5",
    "panel_6",
    "panel_7",
    "main_heater_solar",
    "heating_circulation",
    "internal_thermostat",
    "heater",
    "water_heater_2",
    "intake",
    "intake_summer",
)


class ScheduleParameter(Parameter):
    """Represents a schedule parameter."""

    device: Addressable

    @property
    def request(self) -> Request:
        """A request to change the parameter."""
        schedule_name, _ = self.description.name.split("_", 1)
        return factory(
            "frames.requests.SetScheduleRequest",
            recipient=self.device.address,
            data=collect_schedule_data(schedule_name, self.device),
        )


class ScheduleBinaryParameter(ScheduleParameter, BinaryParameter):
    """Represents a schedule binary parameter."""


@dataclass
class ScheduleParameterDescription(ParameterDescription):
    """Represents a schedule parameter description."""

    cls: type[ScheduleParameter] = ScheduleParameter


SCHEDULE_PARAMETERS: list[ScheduleParameterDescription] = list(
    chain.from_iterable(
        [
            [
                ScheduleParameterDescription(
                    name=f"{name}_{ATTR_SCHEDULE_SWITCH}",
                    cls=ScheduleBinaryParameter,
                ),
                ScheduleParameterDescription(name=f"{name}_{ATTR_SCHEDULE_PARAMETER}"),
            ]
            for name in SCHEDULES
        ]
    )
)


def collect_schedule_data(name: str, device: Device) -> EventDataType:
    """Return a schedule data collected from the device."""
    return {
        ATTR_TYPE: name,
        ATTR_SWITCH: device.data[f"{name}_{ATTR_SCHEDULE_SWITCH}"],
        ATTR_PARAMETER: device.data[f"{name}_{ATTR_SCHEDULE_PARAMETER}"],
        ATTR_SCHEDULE: device.data[ATTR_SCHEDULES][name],
    }


@lru_cache(maxsize=16)
def _split_byte(byte: int) -> list[bool]:
    """Split single byte into an eight bits."""
    bits = []
    for bit in reversed(range(8)):
        bits.append(bool(byte & (1 << bit)))

    return bits


def _join_byte(bits: Sequence[int | bool]) -> int:
    """Join eight bits into a single byte."""
    result = 0
    for bit in bits:
        result = (result << 1) | bit

    return result


def _decode_schedule(message: bytearray, offset: int) -> tuple[list[list[bool]], int]:
    """Return schedule data and offset."""
    schedule: list[list[bool]] = []
    day: list[bool] = []

    last_offset = offset + SCHEDULE_SIZE
    while offset < last_offset:
        if len(day) == 48:
            schedule.append(day)
            day = []

        day.extend(_split_byte(message[offset]))
        offset += 1

    schedule.append(day)

    return schedule, offset


class SchedulesStructure(Structure):
    """Represents a schedule data structure."""

    def encode(self, data: EventDataType) -> bytearray:
        """Encode data to the bytearray message."""
        message = bytearray()
        message.append(1)
        try:
            message.append(SCHEDULES.index(data[ATTR_TYPE]))
            message.append(int(data[ATTR_SWITCH]))
            message.append(int(data[ATTR_PARAMETER]))
            schedule = data[ATTR_SCHEDULE]
        except (KeyError, ValueError) as e:
            raise FrameDataError from e

        schedule_bytes = []
        for day in list(schedule):
            schedule_bytes += [
                _join_byte(day[i : i + 8]) for i in range(0, len(day), 8)
            ]

        message += bytearray(schedule_bytes)

        return message

    def decode(
        self, message: bytearray, offset: int = 0, data: EventDataType | None = None
    ) -> tuple[EventDataType, int]:
        """Decode bytes and return message data and offset."""
        start = message[offset + 1]
        end = message[offset + 2]
        offset += 3
        parameters: list[tuple[int, ParameterDataType]] = []
        schedules: list[tuple[int, list[list[bool]]]] = []
        for _ in range(start, start + end):
            index = message[offset]
            switch = (message[offset + 1], 0, 1)
            parameter = unpack_parameter(message, offset + 2)
            schedule, offset = _decode_schedule(message, offset + 5)
            schedules.append((index, schedule))
            parameters.append((index * 2, switch))
            parameters.append(((index * 2) + 1, parameter))

        return (
            ensure_device_data(
                data, {ATTR_SCHEDULES: schedules, ATTR_SCHEDULE_PARAMETERS: parameters}
            ),
            offset,
        )
