"""Sensor platform for Trannergy PV Inverter integration."""

from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    CONF_INVERTER_SERIAL,
    CONF_SENSORS,
    DEFAULT_SENSORS,
    DOMAIN,
)
from .coordinator import TrannergyDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

# Sensor definitions: key -> [name, unit, icon, device_class, state_class]
SENSOR_TYPES: dict[str, list] = {
    "status": ["Status", None, "mdi:weather-sunny", None, None],
    "actualpower": [
        "Actual Power",
        "W",
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "energytoday": [
        "Energy Today",
        "kWh",
        "mdi:chart-bell-curve-cumulative",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "energytotal": [
        "Energy Total",
        "kWh",
        "mdi:meter-electric-outline",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "hourstotal": [
        "Hours Total",
        "h",
        "mdi:timer-outline",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL_INCREASING,
    ],
    "invertersn": [
        "Inverter Serial Number",
        None,
        "mdi:information-outline",
        None,
        None,
    ],
    "temperature": [
        "Temperature",
        "°C",
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
    ],
    "dcinputvoltage1": [
        "DC Input Voltage 1",
        "V",
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ],
    "dcinputcurrent1": [
        "DC Input Current 1",
        "A",
        "mdi:current-dc",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "dcinputvoltage2": [
        "DC Input Voltage 2",
        "V",
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ],
    "dcinputcurrent2": [
        "DC Input Current 2",
        "A",
        "mdi:current-dc",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "dcinputvoltage3": [
        "DC Input Voltage 3",
        "V",
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ],
    "dcinputcurrent3": [
        "DC Input Current 3",
        "A",
        "mdi:current-dc",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputvoltage1": [
        "AC Output Voltage 1",
        "V",
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputcurrent1": [
        "AC Output Current 1",
        "A",
        "mdi:current-ac",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputfrequency1": [
        "AC Output Frequency 1",
        "Hz",
        "mdi:sine-wave",
        SensorDeviceClass.FREQUENCY,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputpower1": [
        "AC Output Power 1",
        "W",
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputvoltage2": [
        "AC Output Voltage 2",
        "V",
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputcurrent2": [
        "AC Output Current 2",
        "A",
        "mdi:current-ac",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputfrequency2": [
        "AC Output Frequency 2",
        "Hz",
        "mdi:sine-wave",
        SensorDeviceClass.FREQUENCY,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputpower2": [
        "AC Output Power 2",
        "W",
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputvoltage3": [
        "AC Output Voltage 3",
        "V",
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputcurrent3": [
        "AC Output Current 3",
        "A",
        "mdi:current-ac",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputfrequency3": [
        "AC Output Frequency 3",
        "Hz",
        "mdi:sine-wave",
        SensorDeviceClass.FREQUENCY,
        SensorStateClass.MEASUREMENT,
    ],
    "acoutputpower3": [
        "AC Output Power 3",
        "W",
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ],
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Trannergy sensors based on a config entry.

    Args:
        hass: Home Assistant instance.
        entry: Config entry.
        async_add_entities: Callback to add entities.
    """
    coordinator: TrannergyDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    # Get configured sensors from options or data
    configured_sensors = entry.options.get(
        CONF_SENSORS, entry.data.get(CONF_SENSORS, DEFAULT_SENSORS)
    )

    name = entry.data.get(CONF_NAME, "Trannergy")
    serial = entry.data[CONF_INVERTER_SERIAL]

    entities: list[TrannergySensor] = []

    for sensor_key in configured_sensors:
        if sensor_key in SENSOR_TYPES:
            sensor_info = SENSOR_TYPES[sensor_key]
            entities.append(
                TrannergySensor(
                    coordinator=coordinator,
                    entry=entry,
                    sensor_key=sensor_key,
                    sensor_name=sensor_info[0],
                    sensor_unit=sensor_info[1],
                    sensor_icon=sensor_info[2],
                    sensor_device_class=sensor_info[3],
                    sensor_state_class=sensor_info[4],
                    inverter_name=name,
                    inverter_serial=serial,
                )
            )

    async_add_entities(entities)


class TrannergySensor(CoordinatorEntity[TrannergyDataUpdateCoordinator], SensorEntity):
    """Representation of a Trannergy sensor."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: TrannergyDataUpdateCoordinator,
        entry: ConfigEntry,
        sensor_key: str,
        sensor_name: str,
        sensor_unit: str | None,
        sensor_icon: str,
        sensor_device_class: SensorDeviceClass | None,
        sensor_state_class: SensorStateClass | None,
        inverter_name: str,
        inverter_serial: int,
    ) -> None:
        """Initialize the sensor.

        Args:
            coordinator: Data update coordinator.
            entry: Config entry.
            sensor_key: Key of the sensor in the data dictionary.
            sensor_name: Human-readable name of the sensor.
            sensor_unit: Unit of measurement.
            sensor_icon: Icon for the sensor.
            sensor_device_class: Device class of the sensor.
            sensor_state_class: State class of the sensor.
            inverter_name: Name of the inverter.
            inverter_serial: Serial number of the inverter.
        """
        super().__init__(coordinator)

        self._sensor_key = sensor_key
        self._inverter_serial = inverter_serial

        # Entity attributes
        self._attr_name = sensor_name
        self._attr_unique_id = f"{inverter_serial}_{sensor_key}"
        self._attr_native_unit_of_measurement = sensor_unit
        self._attr_icon = sensor_icon
        self._attr_device_class = sensor_device_class
        self._attr_state_class = sensor_state_class

        # Device info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(inverter_serial))},
            name=inverter_name,
            manufacturer="Trannergy",
            model="PV Inverter",
        )

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor.

        Returns:
            Current value of the sensor.
        """
        if self.coordinator.data is None:
            return 0.0 if self._sensor_key != "status" else "Offline"

        value = self.coordinator.data.get(self._sensor_key)

        # Handle None/missing values
        if value is None:
            if self._sensor_key == "status":
                return "Offline"
            if self._sensor_key == "invertersn":
                return ""
            return 0.0

        # Convert to proper type
        if self._sensor_key in ("status", "invertersn"):
            return str(value)

        # For numeric values, ensure we return a float
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0

    @property
    def available(self) -> bool:
        """Return True if entity is available.

        Returns:
            True if the coordinator has data.
        """
        return self.coordinator.last_update_success

