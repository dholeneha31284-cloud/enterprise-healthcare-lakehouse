# Enterprise Healthcare Lakehouse Platform

## Overview

This project demonstrates an end-to-end Enterprise Data Engineering Platform built using modern Data Engineering best practices.

The platform is designed around the Medallion Architecture (Bronze → Silver → Gold) and is capable of processing healthcare claims data using Apache Spark, Databricks, AWS, Delta Lake, and modern DevOps practices.

---

# Architecture

                    Healthcare Files
             CSV / JSON / Parquet / APIs
                         │
                         ▼
                 Data Ingestion Layer
                         │
                         ▼
               Bronze (Raw Data Layer)
                         │
                         ▼
               Data Validation Layer
               ├──────────────┐
               ▼              ▼
          Silver Layer   Quarantine
               │
               ▼
          Gold Layer
               │
               ▼
       Analytics / Power BI
               │
        ┌──────┴─────────┐
        ▼                ▼
     REST APIs       RAG Assistant

---

# Technology Stack

Python

Apache Spark

Databricks

AWS

Delta Lake

GitHub Actions

Docker

Kubernetes

MongoDB Vector Search

FastAPI

Splunk

Grafana

---

# Medallion Architecture

Bronze

Stores raw source data exactly as received.

Silver

Stores cleaned and validated datasets.

Gold

Stores business-ready analytical datasets.

---

# Current Progress

✅ Environment

✅ Spark

✅ Logging

✅ Configuration

✅ Bronze Layer

✅ Validation

🚧 Silver Layer

⬜ Gold Layer

⬜ Delta Lake

⬜ Auto Loader

⬜ AWS

⬜ Kubernetes

⬜ RAG