# Olist Cloud Migration (PostgreSQL → Google BigQuery)

This repository documents the cloud migration of the Olist E-Commerce data pipeline from a local PostgreSQL database to **Google BigQuery**. 

## Why This Project?
Moving from local to cloud requires more than just changing connection strings. This project focuses on production-grade cloud data engineering:
- **Cloud Storage & Ingestion:** Loading large CSVs securely into BigQuery.
- **Cost Optimization:** Implementing Table Partitioning and Clustering in BigQuery to reduce query costs.
- **dbt-bigquery:** Adapting transformation logic to BigQuery's SQL dialect.
- **Infrastructure as Code:** Managing GCP credentials securely.

## Stack
- **Cloud Provider:** Google Cloud Platform (GCP)
- **Data Warehouse:** Google BigQuery
- **Storage:** Local CSV (for this demo) / GCS (future)
- **Transformation:** dbt-core + dbt-bigquery

## Project Structure
*(Will be updated as the project progresses)*

## How to Run
*(Will be updated after Phase 6 completion)*