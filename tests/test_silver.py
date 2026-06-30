import pytest

from pyspark.sql import SparkSession

from src.silver.transformer import SilverTransformer


@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder
        .master("local[*]")
        .appName("silver-test")
        .getOrCreate()
    )


def test_remove_duplicates(spark):

    data = [
        ("P001", "John", "Male", "35", "Apollo", "Flu", "1000", "2026-01-01"),
        ("P001", "John", "Male", "35", "Apollo", "Flu", "1000", "2026-01-01"),
    ]

    columns = [
        "patient_id",
        "patient_name",
        "gender",
        "age",
        "hospital",
        "diagnosis",
        "cost",
        "admission_date"
    ]

    df = spark.createDataFrame(data, columns)

    transformer = SilverTransformer()

    result = transformer.remove_duplicates(df)

    assert result.count() == 1


def test_standardize_strings(spark):

    data = [
        ("P001", " john ", "male", "35",
         " apollo ", " flu ", "1000", "2026-01-01")
    ]

    columns = [
        "patient_id",
        "patient_name",
        "gender",
        "age",
        "hospital",
        "diagnosis",
        "cost",
        "admission_date"
    ]

    df = spark.createDataFrame(data, columns)

    transformer = SilverTransformer()

    result = transformer.standardize_strings(df)

    row = result.first()

    assert row.patient_name == "JOHN"
    assert row.gender == "MALE"
    assert row.hospital == "APOLLO"


def test_convert_data_types(spark):

    data = [
        ("P001", "John", "Male", "35",
         "Apollo", "Flu", "1000.5", "2026-01-01")
    ]

    columns = [
        "patient_id",
        "patient_name",
        "gender",
        "age",
        "hospital",
        "diagnosis",
        "cost",
        "admission_date"
    ]

    df = spark.createDataFrame(data, columns)

    transformer = SilverTransformer()

    result = transformer.convert_data_types(df)

    assert str(result.schema["age"].dataType) == "IntegerType()"
    assert str(result.schema["cost"].dataType) == "DoubleType()"


def test_process_dates(spark):

    data = [
        ("P001", "John", "Male", "35",
         "Apollo", "Flu", "1000", "2026-01-01")
    ]

    columns = [
        "patient_id",
        "patient_name",
        "gender",
        "age",
        "hospital",
        "diagnosis",
        "cost",
        "admission_date"
    ]

    df = spark.createDataFrame(data, columns)

    transformer = SilverTransformer()

    result = transformer.process_dates(df)

    assert result.schema["admission_date"].dataType.typeName() == "date"