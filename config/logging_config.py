"""
Centralized logging configuration.
"""

import logging
from pathlib import Path

from config.settings import settings


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.
    """

    log_directory = settings.ROOT_DIR / "logs"
    log_directory.mkdir(exist_ok=True)

    log_file = log_directory / "pipeline.log"

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger