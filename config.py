from typing import Dict

class Config:
    LOG_DIR: str = "./log"
    RESULTS_DIR: str = "./results"
    TEST_RESULTS_DIR: str = "./test-results"
    DECIMAL_SEPARATOR: str = ","
    UNIT: str = "km"
    UNITS: Dict[str, int] = {"cm": 100000, "m": 1000, "km": 1}
