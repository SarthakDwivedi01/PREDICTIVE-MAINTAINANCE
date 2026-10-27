"""
logger.py

Central logging configuration for the Predictive Maintenance Project.
"""

import logging
from logging.handlers import RotatingFileHandler

from src.config import LOGS_PATH, APP_LOG, ERROR_LOG, PREDICTION_LOG


# Make sure logs folder exists
LOGS_PATH.mkdir(parents=True, exist_ok=True)


def _create_logger():
    logger = logging.getLogger("PredictiveMaintenance")

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # General application log
    app_handler = RotatingFileHandler(
        APP_LOG,
        maxBytes=2 * 1024 * 1024,
        backupCount=5
    )
    app_handler.setFormatter(formatter)

    # Error log
    error_handler = RotatingFileHandler(
        ERROR_LOG,
        maxBytes=2 * 1024 * 1024,
        backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # Prediction log
    prediction_handler = RotatingFileHandler(
        PREDICTION_LOG,
        maxBytes=2 * 1024 * 1024,
        backupCount=5
    )
    prediction_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(prediction_handler)

    return logger


logger = _create_logger()