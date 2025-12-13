"""Constants for the Trannergy PV Inverter integration."""

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)

DOMAIN = "trannergy"

# Configuration
CONF_INVERTER_HOST = "inverter_host"
CONF_INVERTER_PORT = "inverter_port"
CONF_INVERTER_SERIAL = "inverter_serial"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_SENSORS = "sensors"

# Defaults
DEFAULT_NAME = "Trannergy"
DEFAULT_PORT = 8899
DEFAULT_SCAN_INTERVAL = 30

# Sensor definitions: key -> [name, unit, icon, device_class, state_class]
SENSOR_TYPES = {
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

# Default sensors to enable
DEFAULT_SENSORS = [
    "energytoday",
    "energytotal",
    "hourstotal",
    "invertersn",
    "temperature",
    "dcinputvoltage1",
    "dcinputcurrent1",
    "dcinputvoltage2",
    "dcinputcurrent2",
    "acoutputvoltage1",
    "acoutputcurrent1",
    "acoutputfrequency1",
    "acoutputpower1",
]

