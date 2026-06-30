from pyspark.sql import SparkSession

from src.gold.transformer import GoldTransformer

# Create Spark Session
spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("Gold Layer Test")
    .getOrCreate()
)

# Sample Silver Layer Data
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

df = spark.createDataFrame(data, columns)

gold = GoldTransformer(spark)

results = gold.transform(df)

for name, dataframe in results.items():

    print("\n" + "=" * 60)
    print(name.upper())
    print("=" * 60)

    dataframe.show(truncate=False)

spark.stop()