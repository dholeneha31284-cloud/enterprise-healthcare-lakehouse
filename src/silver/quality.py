"""
File: src/silver/quality.py

Silver Layer Data Quality Checks
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class DataQuality:

    """
    Performs data quality validation on
    Silver Layer data.
    """

    def total_records(self, df: DataFrame) -> int:
        """Return total record count."""
        return df.count()

    def duplicate_records(self, df: DataFrame) -> int:
        """
        Return number of duplicate records.
        """
        return df.count() - df.dropDuplicates().count()

    def null_summary(self, df: DataFrame) -> dict:
        """
        Count null values for each column.
        """
        result = {}

        for column in df.columns:
            result[column] = df.filter(
                col(column).isNull()
            ).count()

        return result

    def invalid_age(self, df: DataFrame) -> int:
        """
        Count invalid age values.
        """
        return df.filter(
            (col("age") < 0) |
            (col("age") > 120)
        ).count()

    def invalid_cost(self, df: DataFrame) -> int:
        """
        Count negative costs.
        """
        return df.filter(
            col("cost") < 0
        ).count()

    def quality_report(self, df: DataFrame) -> dict:
        """
        Generate complete quality report.
        """

        return {

            "total_records":
                self.total_records(df),

            "duplicate_records":
                self.duplicate_records(df),

            "null_summary":
                self.null_summary(df),

            "invalid_age":
                self.invalid_age(df),

            "invalid_cost":
                self.invalid_cost(df)

        }