# Sprint 7 – Incremental Processing

## Objective

The objective of Sprint 7 was to design and implement an enterprise-style incremental ETL pipeline in Databricks using Delta Lake.

Instead of processing the complete dataset during every execution, the pipeline processes only newly added or modified records by using a High Watermark strategy.

---

# Architecture

```
                Source Data
                     │
                     ▼
              Bronze Delta Table
                     │
                     ▼
           Read Watermark Metadata
                     │
                     ▼
      Filter New/Updated Records
                     │
                     ▼
          Delta MERGE (UPSERT)
                     │
                     ▼
              Silver Delta Table
                     │
                     ▼
          Update Watermark Table
```

---

# Components

## Source Table

**Table**

```
default.sales_source
```

Stores incoming sales transactions.

Columns

- customer_id
- customer_name
- city
- amount
- updated_at

---

## Bronze Layer

**Table**

```
default.bronze_sales
```

Purpose

- Store raw source data
- Preserve original records
- Support replay and auditing

---

## Watermark Table

**Table**

```
default.watermark
```

Purpose

Store metadata required for incremental processing.

Schema

| Column | Description |
|----------|-------------|
| pipeline_name | Name of pipeline |
| last_processed_timestamp | Last successful execution timestamp |

Example

| pipeline_name | last_processed_timestamp |
|----------------|-------------------------|
| sales_pipeline | 2026-06-30 09:20:00 |

---

## Incremental Processing Logic

Read the latest watermark.

```
last_processed_timestamp
```

Read Bronze table.

Filter records.

```sql
updated_at > last_processed_timestamp
```

Only new records are processed.

---

## Delta MERGE

Incremental records are merged into the Silver table.

Logic

Matched records

→ UPDATE

New records

→ INSERT

This ensures efficient UPSERT operations without reloading the complete dataset.

---

## Watermark Update

After successful processing

```
MAX(updated_at)
```

is written back to

```
default.watermark
```

This value becomes the starting point for the next execution.

---

# Workflow

```
Source

↓

Bronze

↓

Read Watermark

↓

Incremental Read

↓

Delta MERGE

↓

Silver

↓

Update Watermark
```

---

# Enterprise Concepts Covered

- Incremental Processing
- High Watermark Strategy
- Metadata Driven ETL
- Delta Lake
- Delta MERGE
- UPSERT
- Idempotent Pipelines
- Bronze Layer
- Silver Layer
- Delta Transaction History

---

# Benefits

- Processes only changed records
- Faster execution
- Lower compute cost
- Scalable architecture
- Suitable for enterprise ETL pipelines

---

# Key Databricks Features Used

- Delta Tables
- Spark SQL
- DataFrame API
- Delta MERGE
- DESCRIBE HISTORY
- DESCRIBE DETAIL

---

# Learning Outcome

Successfully implemented an enterprise-style incremental data processing pipeline using Delta Lake and Databricks.

The solution demonstrates metadata-driven ETL, incremental loading, watermark management, and Delta MERGE operations commonly used in production data engineering projects.