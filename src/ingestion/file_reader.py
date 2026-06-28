"""
Generic File Reader
"""

from pyspark.sql import DataFrame

from config.logging_config import get_logger

logger = get_logger(__name__)


class FileReader:

    @staticmethod
    def read_csv(spark, path: str) -> DataFrame:

        logger.info(f"Reading CSV: {path}")

        df = (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(path)
        )

        logger.info(f"Rows Loaded: {df.count()}")

        return df