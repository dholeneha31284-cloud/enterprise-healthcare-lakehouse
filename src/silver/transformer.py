"""
File: src/silver/transformer.py

Enterprise Healthcare Lakehouse
Silver Layer Transformer



Description
-----------
Transforms Bronze data into clean, standardized Silver data.

Responsibilities
----------------
✔ Remove duplicates
✔ Standardize strings
✔ Convert data types
✔ Process dates
✔ Handle missing values
✔ Apply business rules
✔ Add derived columns
✔ Select final schema

Compatible with:
- Local PySpark
- Databricks Runtime
"""

from typing import List

from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    trim,
    upper,
    lower,
    when,
    lit,
    to_date,
    year,
    month,
    dayofmonth,
    current_timestamp
)
from pyspark.sql.types import (
    IntegerType,
    DoubleType
)

import logging


logger = logging.getLogger(__name__)


class SilverTransformer:
    """
    Silver Layer Transformer

    Converts raw Bronze data into
    analytics-ready Silver data.
    """

    def __init__(self):

        self.required_columns = [
            "patient_id",
            "patient_name",
            "gender",
            "age",
            "hospital",
            "diagnosis",
            "cost",
            "admission_date"
        ]

    ##################################################################
    # Main Pipeline
    ##################################################################

    def transform(self, df: DataFrame) -> DataFrame:
        """
        Execute complete Silver transformation pipeline.
        """

        logger.info("Starting Silver Layer Transformation")

        self.validate_schema(df)

        df = self.remove_duplicates(df)

        df = self.standardize_strings(df)

        df = self.convert_data_types(df)

        df = self.process_dates(df)

        df = self.handle_missing_values(df)

        df = self.validate_business_rules(df)

        df = self.add_derived_columns(df)

        df = self.select_final_columns(df)

        logger.info("Silver Transformation Completed")

        return df

    ##################################################################
    # Schema Validation
    ##################################################################

    def validate_schema(self, df: DataFrame):

        logger.info("Validating schema")

        missing = [
            column
            for column in self.required_columns
            if column not in df.columns
        ]

        if missing:

            raise ValueError(
                f"Missing required columns : {missing}"
            )

    ##################################################################
    # Remove Duplicate Records
    ##################################################################

    def remove_duplicates(
        self,
        df: DataFrame
    ) -> DataFrame:

        logger.info("Removing duplicate records")

        before = df.count()

        df = df.dropDuplicates()

        after = df.count()

        logger.info(
            f"Removed {before-after} duplicate rows"
        )

        return df

    ##################################################################
    # String Standardization
    ##################################################################

    def standardize_strings(
        self,
        df: DataFrame
    ) -> DataFrame:

        logger.info("Standardizing string columns")

        string_columns = [
            "patient_name",
            "hospital",
            "gender",
            "diagnosis"
        ]

        for column in string_columns:

            if column in df.columns:

                df = df.withColumn(
                    column,
                    upper(
                        trim(
                            col(column)
                        )
                    )
                )

        return df

    ##################################################################
    # Data Type Conversion
    ##################################################################

    def convert_data_types(
        self,
        df: DataFrame
    ) -> DataFrame:

        logger.info("Casting columns")

        df = (
            df

            .withColumn(
                "age",
                col("age").cast(IntegerType())
            )

            .withColumn(
                "cost",
                col("cost").cast(DoubleType())
            )
        )

        return df

    ##################################################################
    # Date Processing
    ##################################################################

    def process_dates(
        self,
        df: DataFrame
    ) -> DataFrame:

        logger.info("Processing dates")

        df = df.withColumn(
            "admission_date",
            to_date(
                col("admission_date"),
                "yyyy-MM-dd"
            )
        )

        return df

    ##################################################################
    # Missing Values
    ##################################################################

    def handle_missing_values(
        self,
        df: DataFrame
    ) -> DataFrame:

        logger.info("Handling missing values")

        df = (

            df

            .fillna(
                {
                    "hospital": "UNKNOWN",
                    "diagnosis": "UNKNOWN",
                    "gender": "UNKNOWN"
                }
            )

            .fillna(
                {
                    "cost": 0.0
                }
            )
        )

        return df
    ##################################################################
    # Business Rule Validation
    ##################################################################

    def validate_business_rules(
        self,
        df: DataFrame
    ) -> DataFrame:

        """
        Apply business validation rules.

        Rules
        -----
        1. Age must be between 0 and 120.
        2. Cost cannot be negative.
        """

        logger.info("Applying business rules")

        df = (

            df

            .withColumn(

                "age",

                when(
                    (col("age") < 0) |
                    (col("age") > 120),
                    None
                ).otherwise(col("age"))

            )

            .withColumn(

                "cost",

                when(
                    col("cost") < 0,
                    0.0
                ).otherwise(col("cost"))

            )

        )

        return df

    ##################################################################
    # Derived Columns
    ##################################################################

    def add_derived_columns(
        self,
        df: DataFrame
    ) -> DataFrame:

        """
        Create derived business columns.
        """

        logger.info("Creating derived columns")

        df = (

            df

            .withColumn(

                "age_group",

                when(col("age") < 18, "CHILD")
                .when(col("age") < 60, "ADULT")
                .otherwise("SENIOR")

            )

            .withColumn(
                "admission_year",
                year(col("admission_date"))
            )

            .withColumn(
                "admission_month",
                month(col("admission_date"))
            )

            .withColumn(
                "admission_day",
                dayofmonth(col("admission_date"))
            )

            .withColumn(
                "processed_timestamp",
                current_timestamp()
            )

        )

        return df

    ##################################################################
    # Final Schema
    ##################################################################

    def select_final_columns(
        self,
        df: DataFrame
    ) -> DataFrame:

        """
        Select final Silver schema.

        Keeps column order consistent.
        """

        logger.info("Selecting final schema")

        final_columns = [

            "patient_id",

            "patient_name",

            "gender",

            "age",

            "age_group",

            "hospital",

            "diagnosis",

            "cost",

            "admission_date",

            "admission_year",

            "admission_month",

            "admission_day",

            "processed_timestamp"

        ]

        existing_columns = [

            column

            for column in final_columns

            if column in df.columns

        ]

        return df.select(existing_columns)

    ##################################################################
    # Utility Methods
    ##################################################################

    def get_required_columns(
        self
    ) -> List[str]:

        """
        Return required Bronze columns.
        """

        return self.required_columns

    def print_schema(
        self,
        df: DataFrame
    ) -> None:

        """
        Print DataFrame schema.
        """

        logger.info("Printing schema")

        df.printSchema()

    def preview(
        self,
        df: DataFrame,
        rows: int = 10
    ) -> None:

        """
        Display sample records.
        """

        logger.info(f"Showing first {rows} rows")

        df.show(rows, truncate=False)    