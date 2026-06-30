# 🏥 Enterprise Healthcare Lakehouse

A production-inspired Data Engineering project demonstrating the design and implementation of a modern Healthcare Lakehouse using **PySpark**, **Python**, and enterprise ETL best practices.

---

## 📖 Project Overview

This project simulates a real-world healthcare data platform where raw patient data is ingested, cleaned, transformed, validated, and prepared for analytics using a multi-layer Lakehouse architecture.

The goal is to demonstrate production-style Data Engineering practices including:

- ETL Pipeline Development
- Data Validation
- Data Quality Checks
- PySpark Transformations
- Unit Testing with Pytest
- Modular Project Structure
- Git & GitHub Version Control

---

# 🏗️ Architecture

```text
                Raw Healthcare Data
                        │
                        ▼
                Bronze Layer
          (Raw Data Ingestion)
                        │
                        ▼
                Silver Layer
     (Cleaning & Standardization)
                        │
                        ▼
                 Gold Layer
        (Business Analytics) 🚧
                        │
                        ▼
           Dashboards / Reporting
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| PySpark | Distributed Data Processing |
| Pytest | Unit Testing |
| Git | Version Control |
| GitHub | Source Code Management |
| VS Code | Development Environment |

---

# 📂 Project Structure

```text
enterprise-healthcare-lakehouse/

├── config/
├── data/
├── docs/
├── logs/
├── src/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── utils/
├── tests/
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

# ✨ Features

### ✅ Bronze Layer
- Raw data ingestion
- Schema validation
- Logging
- Data validation

### ✅ Silver Layer
- Duplicate removal
- String standardization
- Data type conversion
- Date processing
- Missing value handling
- Business rule validation
- Derived columns
- Data quality checks

### 🚧 Gold Layer (Coming Soon)
- Business KPIs
- Aggregations
- Window Functions
- Fact & Dimension Tables

---

# 🧪 Running Tests

Run all tests:

```bash
pytest -v
```

Run Silver Layer tests:

```bash
pytest tests/test_silver.py -v
```

---



# 📈 Sprint Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 – Project Setup | ✅ Completed |
| Sprint 2 – Bronze Layer | ✅ Completed |
| Sprint 3 – Silver Layer | ✅ Completed |
| Sprint 4 – Gold Layer | 🚧 In Progress |
| Sprint 5 – Delta Lake | ⏳ Planned |
| Sprint 6 – Databricks Deployment | ⏳ Planned |
| Sprint 7 – Streaming Pipeline | ⏳ Planned |

---

# 🎯 Future Enhancements

- Delta Lake
- Slowly Changing Dimensions (SCD)
- Window Functions
- Incremental Processing
- Databricks Workflows
- CI/CD with GitHub Actions
- Docker
- Airflow Integration
- AWS Deployment

---

# 👩‍💻 Author

**Dr. Neha Pankaj Dhole**

- Data Engineer
- AI/ML Engineer
- Cloud & Databricks Enthusiast

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.