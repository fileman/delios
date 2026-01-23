"""Module constants."""

DOMAIN = "delios"

MODELS: list[str] = [
    "IBRIDO DLS",
    "IBRIDO DLS-C",
]

CONF_NAME = "name"
CONF_MODEL = "model"
CONF_HOST = "host"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_SCAN_INTERVAL = "scan_interval"

DEFAULT_USERNAME = "user"
DEFAULT_SCAN_INTERVAL = 10

SYSTEM_UPDATE_INTERVAL = 60 * 60

ERRORS: dict[str, str] = {
    "E001": "DSP A",
    "E002": "DSP B",
    "E003": "Inverter not configured",
    "E004": "High current C",
    "E005": "GFI test",
    "E006": "Interlock test",
    "E007": "Temperature out of range",
    "E008": "RCMU",
    "E009": "Wrong N line connection",
    "E010": "Self test failed",
    "E011": "High AC voltage A",
    "E012": "High AC voltage B",
    "E013": "Low AC voltage A",
    "E014": "Low AC voltage B",
    "E015": "High AC frequency A",
    "E016": "Low AC frequency A",
    "E017": "High AC frequency B",
    "E018": "Low AC frequency B",
    "E019": "Remote disconnection",
    "E020": "Dc current injected",
    "E021": "Max Dc current injected",
    "E022": "DSP C",
    "E023": "High current B1",
    "E024": "High current B2",
    "E025": "Insulation R",
    "E026": "DC Voltage out of range",
    "E027": "High current A",
    "E028": "Battery not recognized",
    "E029": "Termal braker protection",
    "E030": "Overload protection",
    "E031": "Wrong AC wiring",
    "E032": "Internal control error (E032)",
    "E033": "Internal control error (E033)",
    "E034": "Internal control error (E034)",
    "E035": "Internal control error (E035)",
    "E036": "Battery temperature out of range",
    "E037": "Battery error",
    "E038": "Internal control error (E038)",
    "E999": "Unknown error",
}
