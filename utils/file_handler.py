import os
from config import Config

def create_directories():
    os.makedirs(Config.LOG_DIR, exist_ok=True)
    os.makedirs(Config.RESULTS_DIR, exist_ok=True)
    os.makedirs(Config.TEST_RESULTS_DIR, exist_ok=True)
