import pytest
from pyspark.sql import SparkSession

from src.gold.transformer import GoldTransformer


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("gold-test")
        .getOrCreate()
    )

    yield spark

    spark.stop()


@pytest.fixture
def sample_df(spark):

    data = [
        ("P001", "JOHN", "MALE", 35, "ADULT", "APOLLO", "FLU", 1200.0, "2026-01-01", 2026, 1, 1),
        ("P002", "ALICE", "FEMALE", 28, "ADULT", "FORTIS", "COVID", 3500.0, "2026-01-02", 2026, 1, 2),
        ("P003", "DAVID", "MALE", 65, "SENIOR", "APOLLO", "DIABETES", 2500.0, "2026-01-03", 2026, 1, 3),
        ("P004", "MARY", "FEMALE", 12, "CHILD", "FORTIS", "FEVER", 800.0, "2026-02-10", 2026, 2, 10),
        ("P005", "SMITH", "MALE", 42, "ADULT", "APOLLO", "COVID", 5000.0, "2026-02-15", 2026, 2, 15),
    ]

    columns = [
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
    ]

    return spark.createDataFrame(data, columns)


@pytest.fixture
def gold(spark):

    return GoldTransformer(spark)


def test_total_patients(gold, sample_df):

    gold.register_views(sample_df)

    result = gold.total_patients()

    assert result.first()["total_patients"] == 5


def test_patients_by_hospital(gold, sample_df):

    gold.register_views(sample_df)

    result = gold.patients_by_hospital()

    rows = result.collect()

    assert rows[0]["hospital"] == "APOLLO"
    assert rows[0]["total_patients"] == 3

    assert rows[1]["hospital"] == "FORTIS"
    assert rows[1]["total_patients"] == 2


def test_patients_by_gender(gold, sample_df):

    gold.register_views(sample_df)

    result = gold.patients_by_gender()

    rows = result.collect()

    assert rows[0]["gender"] == "MALE"
    assert rows[0]["total_patients"] == 3


def test_financial_summary(gold, sample_df):

    gold.register_views(sample_df)

    result = gold.financial_summary()

    row = result.first()

    assert row["total_cost"] == 13000.0
    assert row["maximum_cost"] == 5000.0
    assert row["minimum_cost"] == 800.0


def test_monthly_admissions(gold, sample_df):

    gold.register_views(sample_df)

    result = gold.monthly_admissions()

    rows = result.collect()

    assert rows[0]["total_admissions"] == 3
    assert rows[1]["total_admissions"] == 2


def test_diagnosis_summary(gold, sample_df):

    gold.register_views(sample_df)

    result = gold.diagnosis_summary()

    rows = result.collect()

    assert rows[0]["diagnosis"] == "COVID"
    assert rows[0]["total_patients"] == 2


def test_transform(gold, sample_df):

    result = gold.transform(sample_df)

    assert "total_patients" in result
    assert "patients_by_hospital" in result
    assert "patients_by_gender" in result
    assert "financial_summary" in result
    assert "monthly_admissions" in result
    assert "diagnosis_summary" in result