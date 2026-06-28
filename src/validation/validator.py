"""
Validation Framework

Performs data quality validation on Healthcare Claims data.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from config.logging_config import get_logger

logger = get_logger(__name__)


class Validator:
    """
    Validates Bronze Layer data before moving it to Silver.
    """

    @staticmethod
    def validate_claims(df: DataFrame):

        logger.info("Running Data Validation...")

        # Valid Records
        valid_df = df.filter(
            (col("claim_id").isNotNull()) &
            (col("patient_id").isNotNull()) &
            (col("claim_amount") > 0) &
            (col("claim_date").isNotNull())
        )

        # Invalid Records
        invalid_df = df.subtract(valid_df)

        valid_count = valid_df.count()
        invalid_count = invalid_df.count()

        logger.info(f"Valid Records   : {valid_count}")
        logger.info(f"Invalid Records : {invalid_count}")

        return valid_df, invalid_df