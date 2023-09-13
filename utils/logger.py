import logging
import os
from datetime import datetime
from config import Config

def setup_logger(run_id: str):
    log_filename = f"{datetime.now().strftime('%Y-%m-%d')} {run_id}.log"
    logging.basicConfig(filename=os.path.join(Config.LOG_DIR, log_filename), level=logging.INFO)
