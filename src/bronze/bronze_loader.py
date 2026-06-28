"""
Bronze Layer Loader

Reads raw claims data and enriches it with audit metadata.
"""

from datetime import datetime

from pyspark.sql.functions import input_file_name, lit

from config.logging_config import get_logger
from config.settings import settings
from src.ingestion.file_reader import FileReader
from src.spark.spark_session import SparkManager

logger = get_logger(__name__)


class BronzeLoader:

    def load_claims(self):

        logger.info("Starting Bronze Layer Ingestion")

        spark = SparkManager.create_session()

        df = FileReader.read_csv(
            spark,
            str(settings.RAW_DATA / "claims.csv")
        )

        bronze_df = (
            df
            .withColumn("source_file", input_file_name())
            .withColumn(
                "ingestion_time",
                lit(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )
        )

        logger.info("Bronze Data Preview")

        bronze_df.show(truncate=False)

        return bronze_df