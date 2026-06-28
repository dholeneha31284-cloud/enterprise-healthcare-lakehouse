"""
Reusable Spark Session Factory.
"""

from pyspark.sql import SparkSession

from config.logging_config import get_logger
from config.settings import settings

logger = get_logger(__name__)


class SparkManager:
    """
    Creates and manages Spark Sessions.
    """

    @staticmethod
    def create_session() -> SparkSession:

        logger.info("Creating Spark Session...")

        spark = (
            SparkSession.builder
            .master("local[*]")
            .appName(settings.APP_NAME)
            .config("spark.sql.shuffle.partitions", "4")
            .config("spark.driver.memory", "2g")
            .getOrCreate()
        )

        logger.info("Spark Session Created Successfully")

        return spark