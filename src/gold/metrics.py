"""
File: src/gold/metrics.py

Enterprise Healthcare Lakehouse

Gold Layer KPI Metrics
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    count,
    countDistinct,
    sum,
    avg,
    max,
    min,
    col
)


class GoldMetrics:
    """
    Reusable KPI calculations for the Gold Layer.
    """

    def patient_metrics(self, df: DataFrame) -> DataFrame:
        """
        Patient KPIs.
        """

        return df.select(

            count("*").alias("total_patients"),

            countDistinct("patient_id").alias(
                "unique_patients"
            )

        )

    def financial_metrics(self, df: DataFrame) -> DataFrame:
        """
        Financial KPIs.
        """

        return df.select(

            sum("cost").alias("total_cost"),

            avg("cost").alias("average_cost"),

            max("cost").alias("maximum_cost"),

            min("cost").alias("minimum_cost")

        )

    def hospital_metrics(self, df: DataFrame) -> DataFrame:
        """
        Hospital KPIs.
        """

        return (

            df.groupBy("hospital")

            .agg(

                count("*").alias("total_patients"),

                sum("cost").alias("total_cost"),

                avg("cost").alias("average_cost")

            )

            .orderBy(
                col("total_patients").desc()
            )

        )

    def diagnosis_metrics(self, df: DataFrame) -> DataFrame:
        """
        Diagnosis KPIs.
        """

        return (

            df.groupBy("diagnosis")

            .agg(

                count("*").alias("patient_count")

            )

            .orderBy(
                col("patient_count").desc()
            )

        )

    def gender_metrics(self, df: DataFrame) -> DataFrame:
        """
        Gender KPIs.
        """

        return (

            df.groupBy("gender")

            .agg(

                count("*").alias("patient_count")

            )

            .orderBy(
                col("patient_count").desc()
            )

        )

    def age_group_metrics(self, df: DataFrame) -> DataFrame:
        """
        Age Group KPIs.
        """

        return (

            df.groupBy("age_group")

            .agg(

                count("*").alias("patient_count")

            )

            .orderBy(
                col("patient_count").desc()
            )

        )