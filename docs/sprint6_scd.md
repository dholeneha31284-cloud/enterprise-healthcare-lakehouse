<<<<<<< HEAD
# Sprint 6 – Slowly Changing Dimensions (SCD)

## Objective

Implement Slowly Changing Dimensions (SCD) using Delta Lake to manage changes in dimension tables while supporting both overwrite and historical tracking strategies.

---

# What is a Slowly Changing Dimension?

A Slowly Changing Dimension (SCD) is a data warehousing technique used to manage changes in dimension data over time.

Example:

Customer Address

```
Customer ID : 101

Old City : Pune

New City : Hyderabad
```

Business must decide whether to:

- Overwrite the old value
- Preserve the history

This leads to different SCD implementations.

---

# SCD Type 1

## Definition

SCD Type 1 overwrites the existing record.

Historical information is **not preserved**.

### Example

Before

| Customer ID | Name | City |
|-------------|------|------|
|101|Neha|Pune|

After

| Customer ID | Name | City |
|-------------|------|------|
|101|Neha|Hyderabad|

Notice that **Pune no longer exists**.

---

## Enterprise Use Cases

- Typographical corrections
- Incorrect customer details
- Data cleansing
- Non-historical master data

---

## Databricks Implementation

Implemented using Delta Lake MERGE.

```sql
MERGE INTO dim_customer_type1 target
USING customer_updates source
ON target.customer_id = source.customer_id

WHEN MATCHED THEN
UPDATE SET *

WHEN NOT MATCHED THEN
INSERT *
```

---

# SCD Type 2

## Definition

SCD Type 2 preserves complete history.

Instead of updating the existing row:

- Old row becomes inactive
- New row is inserted

---

## Table Structure

| Column | Description |
|---------|-------------|
|customer_id|Business Key|
|customer_name|Customer Name|
|city|Current City|
|effective_date|Record Start Date|
|end_date|Record End Date|
|is_current|Current Record Flag|

---

## Example

Before Update

|ID|Name|City|Effective|End|Current|
|--|----|----|---------|---|-------|
|101|Neha|Pune|2026-01-01|NULL|TRUE|

Customer moves to Hyderabad.

After Update

|ID|Name|City|Effective|End|Current|
|--|----|----|---------|---|-------|
|101|Neha|Pune|2026-01-01|2026-06-30|FALSE|
|101|Neha|Hyderabad|2026-07-01|NULL|TRUE|

History is preserved.

---

## Enterprise Use Cases

- Customer Address History
- Insurance Plans
- Hospital Assignment
- Employee Department
- Product Pricing
- Regulatory Audit
- Healthcare Patient Master

---

# Implementation Steps

## Step 1

Create Dimension Table

```
dim_customer_type2
```

---

## Step 2

Insert Initial Records

```
Current = TRUE
```

---

## Step 3

Receive Incremental Updates

```
customer_updates
```

---

## Step 4

Expire Existing Records

```
Current = FALSE

End Date = Current Date
```

---

## Step 5

Insert New Current Records

```
Current = TRUE

Effective Date = Current Date
```

---

# Delta Lake Features Used

- Delta Tables
- MERGE
- UPDATE
- INSERT
- Transaction History
- ACID Transactions

---

# Difference Between SCD Type 1 and Type 2

| Feature | Type 1 | Type 2 |
|----------|--------|--------|
|History Preserved|❌ No|✅ Yes|
|Overwrite Existing Record|✅ Yes|❌ No|
|Multiple Versions|❌ No|✅ Yes|
|Effective Date|❌|✅|
|End Date|❌|✅|
|Current Flag|❌|✅|

---

# Healthcare Example

Patient changes hospital location.

## Type 1

```
Old Hospital

↓

New Hospital
```

Previous information is lost.

---

## Type 2

```
Hospital A

↓

Expired

↓

Hospital B
```

Complete history remains available for reporting and auditing.

---

# Interview Questions

### What is SCD?

A technique used to manage changes in dimension tables over time.

---

### When should SCD Type 1 be used?

When historical data is not required.

Examples:

- Typo corrections
- Incorrect customer information

---

### When should SCD Type 2 be used?

When complete history must be preserved.

Examples:

- Customer Address
- Insurance Plan
- Employee Department
- Product Pricing

---

### Why is Delta Lake useful for SCD?

Delta Lake provides:

- ACID Transactions
- MERGE
- UPDATE
- DELETE
- Time Travel
- Version History

which makes implementing SCD efficient and reliable.

---

# Technologies Used

- Databricks
- Apache Spark
- PySpark
- Delta Lake
- Spark SQL

---

# Sprint Outcome

Successfully implemented:

- SCD Type 1
- SCD Type 2
- Delta MERGE
- Historical Tracking
- Enterprise Customer Dimension

These are core concepts frequently evaluated in Data Engineering and Databricks interviews.
=======

>>>>>>> 00e3d0aeaf041ea298c332a671f20f541405ec6d
