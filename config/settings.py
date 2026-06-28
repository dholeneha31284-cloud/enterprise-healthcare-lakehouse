"""
Application configuration settings.
"""

from pathlib import Path


class Settings:
    """Centralized application settings."""

    PROJECT_NAME = "Enterprise Healthcare Data Platform"

    APP_NAME = "HealthcareETLPipeline"

    ROOT_DIR = Path(__file__).resolve().parent.parent

    DATA_DIR = ROOT_DIR / "data"

    RAW_DATA = DATA_DIR / "raw"

    BRONZE = DATA_DIR / "bronze"

    SILVER = DATA_DIR / "silver"

    GOLD = DATA_DIR / "gold"

    QUARANTINE = DATA_DIR / "quarantine"

    LOG_LEVEL = "INFO"


settings = Settings()