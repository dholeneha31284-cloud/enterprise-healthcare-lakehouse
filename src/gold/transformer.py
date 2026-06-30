"""
File: src/gold/transformer.py

Enterprise Healthcare Lakehouse
Gold Layer Transformer

Executes Spark SQL queries to generate
business-ready Gold datasets.
"""

from pyspark.sql import DataFrame, SparkSession

from src.gold import queries


class GoldTransformer:
    """
    Executes Gold Layer SQL transformations.
    """

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def register_views(self, df: DataFrame) -> None:
        """
        Register Silver DataFrame as a temporary SQL view.
        """

        df.createOrReplaceTempView("silver_patient")

    def total_patients(self) -> DataFrame:
        """
        Returns total patient count.
        """

        return self.spark.sql(
            queries.TOTAL_PATIENTS
        )

    def patients_by_hospital(self) -> DataFrame:
        """
        Returns patients grouped by hospital.
        """

        return self.spark.sql(
            queries.PATIENTS_BY_HOSPITAL
        )

    def patients_by_gender(self) -> DataFrame:
        """
        Returns patients grouped by gender.
        """

        return self.spark.sql(
            queries.PATIENTS_BY_GENDER
        )

    def patients_by_age_group(self) -> DataFrame:
        """
        Returns patients grouped by age group.
        """

        return self.spark.sql(
            queries.PATIENTS_BY_AGE_GROUP
        )

    def financial_summary(self) -> DataFrame:
        """
        Returns financial KPIs.
        """

        return self.spark.sql(
            queries.FINANCIAL_SUMMARY
        )

    def monthly_admissions(self) -> DataFrame:
        """
        Returns monthly admissions.
        """

        return self.spark.sql(
            queries.MONTHLY_ADMISSIONS
        )

    def diagnosis_summary(self) -> DataFrame:
        """
        Returns diagnosis statistics.
        """

        return self.spark.sql(
            queries.DIAGNOSIS_SUMMARY
        )

    def transform(self, df: DataFrame) -> dict:
        """
        Execute complete Gold Layer pipeline.

        Returns
        -------
        Dictionary containing all Gold datasets.
        """

        self.register_views(df)

        return {

            "total_patients":
                self.total_patients(),

            "patients_by_hospital":
                self.patients_by_hospital(),

            "patients_by_gender":
                self.patients_by_gender(),

            "patients_by_age_group":
                self.patients_by_age_group(),

            "financial_summary":
                self.financial_summary(),

            "monthly_admissions":
                self.monthly_admissions(),

            "diagnosis_summary":
                self.diagnosis_summary()

        }