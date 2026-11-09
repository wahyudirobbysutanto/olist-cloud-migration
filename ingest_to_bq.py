import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Retrieve from .env
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
# The Google Cloud library automatically reads GOOGLE_APPLICATION_CREDENTIALS from the environment

def upload_csv_to_bq(csv_file_path, dataset_id, table_name):
    """Reads a local CSV and uploads it to BigQuery."""
    print(f"⏳ Reading {csv_file_path}...")
    
    try:
        # Using utf-8 to prevent encoding errors on Olist data
        df = pd.read_csv(csv_file_path, encoding='utf-8')
        
        client = bigquery.Client(project=PROJECT_ID)
        table_id = f"{PROJECT_ID}.{dataset_id}.{table_name}"
        
        print(f"⬆️ Uploading {len(df)} rows to {table_id}...")
        
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE", 
            autodetect=True
        )
        
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result() # Wait for the job to complete
        
        print(f"✅ Success: {table_name} loaded into BigQuery!\n")
    except Exception as e:
        print(f"❌ Failed to upload {table_name}: {e}\n")

if __name__ == "__main__":
    files_to_upload = {
        "olist_orders_dataset.csv": "orders",
        "olist_customers_dataset.csv": "customers",
        "olist_order_items_dataset.csv": "order_items",
        "olist_products_dataset.csv": "products",
        "olist_sellers_dataset.csv": "sellers",
        "olist_order_payments_dataset.csv": "payments",
        "olist_order_reviews_dataset.csv": "reviews",
        "olist_geolocation_dataset.csv": "geolocation", 
        "product_category_name_translation.csv": "category_translation"
    }

    for csv_filename, table_name in files_to_upload.items():
        path = f"data/{csv_filename}"
        if os.path.exists(path):
            upload_csv_to_bq(path, "raw", table_name)
        else:
            print(f"❌ File not found: {path}")