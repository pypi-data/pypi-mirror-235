"""Contains a thermostat parameters structure decoder."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

from pyplumio import util
from pyplumio.const import ATTR_INDEX, ATTR_OFFSET, ATTR_SIZE, ATTR_VALUE
from pyplumio.frames import Request
from pyplumio.helpers.factory import factory
from pyplumio.helpers.parameter import BinaryParameter, Parameter, ParameterDescription
from pyplumio.helpers.typing import EventDataType, ParameterDataType, ParameterValueType
from pyplumio.structures import StructureDecoder, ensure_device_data
from pyplumio.structures.thermostat_sensors import ATTR_THERMOSTAT_COUNT

if TYPE_CHECKING:
    from pyplumio.devices.thermostat import Thermostat


ATTR_THERMOSTAT_PROFILE: Final = "thermostat_profile"
ATTR_THERMOSTAT_PARAMETERS: Final = "thermostat_parameters"
ATTR_THERMOSTAT_PARAMETERS_DECODER: Final = "thermostat_parameters_decoder"

THERMOSTAT_PARAMETER_SIZE: Final = 3


class ThermostatParameter(Parameter):
    """Represents a thermostat parameter."""

    device: Thermostat
    description: ThermostatParameterDescription
    offset: int

    def __init__(self, offset: int, *args, **kwargs):
        """Initialize a new thermostat parameter."""
        self.offset = offset
        super().__init__(*args, **kwargs)

    async def set(self, value: ParameterValueType, retries: int = 5) -> bool:
        """Set a parameter value."""
        if isinstance(value, (int, float)):
            value *= self.description.multiplier

        return await super().set(int(value), retries)

    @property
    def value(self) -> ParameterValueType:
        """A parameter value."""
        return self._value / self.description.multiplier

    @property
    def min_value(self) -> ParameterValueType:
        """Minimum allowed value."""
        return self._min_value / self.description.multiplier

    @property
    def max_value(self) -> ParameterValueType:
        """Maximum allowed value."""
        return self._max_value / self.description.multiplier

    @property
    def request(self) -> Request:
        """A request to change the parameter."""
        return factory(
            "frames.requests.SetThermostatParameterRequest",
            recipient=self.device.parent.address,
            data={
                # Increase the index by one to account for thermostat
                # profile, which is being set at ecoMAX device level.
                ATTR_INDEX: self._index + 1,
                ATTR_VALUE: self._value,
                ATTR_OFFSET: self.offset,
                ATTR_SIZE: self.description.size,
            },
        )


class ThermostatBinaryParameter(BinaryParameter, ThermostatParameter):
    """Represents a thermostat binary parameter."""


@dataclass
class ThermostatParameterDescription(ParameterDescription):
    """Represents a thermostat parameter description."""

    cls: type[ThermostatParameter] = ThermostatParameter
    multiplier: int = 1
    size: int = 1


THERMOSTAT_PARAMETERS: tuple[ThermostatParameterDescription, ...] = (
    ThermostatParameterDescription(name="mode"),
    ThermostatParameterDescription(name="party_target_temp", size=2, multiplier=10),
    ThermostatParameterDescription(name="holidays_target_temp", size=2, multiplier=10),
    ThermostatParameterDescription(name="correction"),
    ThermostatParameterDescription(name="away_timer"),
    ThermostatParameterDescription(name="airing_timer"),
    ThermostatParameterDescription(name="party_timer"),
    ThermostatParameterDescription(name="holidays_timer"),
    ThermostatParameterDescription(name="hysteresis", multiplier=10),
    ThermostatParameterDescription(name="day_target_temp", size=2, multiplier=10),
    ThermostatParameterDescription(name="night_target_temp", size=2, multiplier=10),
    ThermostatParameterDescription(
        name="antifreeze_target_temp", size=2, multiplier=10
    ),
    ThermostatParameterDescription(name="heating_target_temp", size=2, multiplier=10),
    ThermostatParameterDescription(name="heating_timer"),
    ThermostatParameterDescription(name="off_timer"),
)


def _empty_response(
    offset: int, data: EventDataType | None = None
) -> tuple[EventDataType, int]:
    """Return an empty response."""
    return (
        ensure_device_data(
            data,
            {ATTR_THERMOSTAT_PARAMETERS: None, ATTR_THERMOSTAT_PROFILE: None},
        ),
        offset,
    )


class ThermostatParametersStructure(StructureDecoder):
    """Represents a thermostat parameters data structure."""

    _offset: int

    def _unpack_thermostat_parameter(
        self, message: bytearray, index: int
    ) -> ParameterDataType | None:
        """Unpack a single thermostat parameter."""
        description = THERMOSTAT_PARAMETERS[index]
        try:
            return util.unpack_parameter(message, self._offset, size=description.size)
        finally:
            self._offset += THERMOSTAT_PARAMETER_SIZE * description.size

    def _unpack_thermostat_parameters(
        self, message: bytearray, thermostats: int, start: int, end: int
    ) -> list[tuple[int, ParameterDataType]]:
        """Unpack thermostat parameters."""
        return [
            (index, thermostat_parameter)
            for index, thermostat_parameter in [
                (index, self._unpack_thermostat_parameter(message, index))
                for index in range(start, (start + end) // thermostats)
            ]
            if thermostat_parameter is not None
        ]

    def decode(
        self, message: bytearray, offset: int = 0, data: EventDataType | None = None
    ) -> tuple[EventDataType, int]:
        """Decode bytes and return message data and offset."""
        data = ensure_device_data(data)
        thermostats = data.get(ATTR_THERMOSTAT_COUNT, 0)
        if thermostats == 0:
            return _empty_response(offset, data)

        start = message[offset + 1]
        end = message[offset + 2]
        thermostat_profile = util.unpack_parameter(message, offset + 3)
        self._offset = offset + 6
        return (
            ensure_device_data(
                data,
                {
                    ATTR_THERMOSTAT_PROFILE: thermostat_profile,
                    ATTR_THERMOSTAT_PARAMETERS: {
                        index: thermostat_parameters
                        for index, thermostat_parameters in [
                            (
                                index,
                                self._unpack_thermostat_parameters(
                                    message, thermostats, start, end
                                ),
                            )
                            for index in range(thermostats)
                        ]
                        if thermostat_parameters
                    },
                },
            ),
            self._offset,
        )
