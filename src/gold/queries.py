"""
Gold Layer SQL Queries

Contains all business SQL used to create
Gold Layer datasets.
"""

TOTAL_PATIENTS = """
SELECT
    COUNT(*) AS total_patients
FROM silver_patient
"""

PATIENTS_BY_HOSPITAL = """
SELECT
    hospital,
    COUNT(*) AS total_patients
FROM silver_patient
GROUP BY hospital
ORDER BY total_patients DESC
"""

PATIENTS_BY_GENDER = """
SELECT
    gender,
    COUNT(*) AS total_patients
FROM silver_patient
GROUP BY gender
ORDER BY total_patients DESC
"""

PATIENTS_BY_AGE_GROUP = """
SELECT
    age_group,
    COUNT(*) AS total_patients
FROM silver_patient
GROUP BY age_group
ORDER BY total_patients DESC
"""

FINANCIAL_SUMMARY = """
SELECT
    SUM(cost) AS total_cost,
    AVG(cost) AS average_cost,
    MAX(cost) AS maximum_cost,
    MIN(cost) AS minimum_cost
FROM silver_patient
"""

MONTHLY_ADMISSIONS = """
SELECT
    admission_year,
    admission_month,
    COUNT(*) AS total_admissions
FROM silver_patient
GROUP BY
    admission_year,
    admission_month
ORDER BY
    admission_year,
    admission_month
"""

DIAGNOSIS_SUMMARY = """
SELECT
    diagnosis,
    COUNT(*) AS total_patients
FROM silver_patient
GROUP BY diagnosis
ORDER BY total_patients DESC
"""