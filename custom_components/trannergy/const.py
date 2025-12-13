"""Constants for the Trannergy PV Inverter integration."""

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

# Sensor keys (without device class info - that's in sensor.py)
SENSOR_KEYS = [
    "status",
    "actualpower",
    "energytoday",
    "energytotal",
    "hourstotal",
    "invertersn",
    "temperature",
    "dcinputvoltage1",
    "dcinputcurrent1",
    "dcinputvoltage2",
    "dcinputcurrent2",
    "dcinputvoltage3",
    "dcinputcurrent3",
    "acoutputvoltage1",
    "acoutputcurrent1",
    "acoutputfrequency1",
    "acoutputpower1",
    "acoutputvoltage2",
    "acoutputcurrent2",
    "acoutputfrequency2",
    "acoutputpower2",
    "acoutputvoltage3",
    "acoutputcurrent3",
    "acoutputfrequency3",
    "acoutputpower3",
]

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
