import os
from pathlib import Path
from snowflake.connector.pandas_tools import write_pandas

import snowflake.connector
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

load_dotenv()

builder = (
    SparkSession.builder
    .appName("Load Gold To Snowflake")
    .master("local[*]")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension",
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()

conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
)

cursor = conn.cursor()

print("✅ Connected to Snowflake")
GOLD_PATH = Path("data/gold")

TABLES = {
    "dim_customers": "DIM_CUSTOMERS",
    "dim_products": "DIM_PRODUCTS",
    "dim_sellers": "DIM_SELLERS",
    "fact_orders": "FACT_ORDERS",
    "fact_payments": "FACT_PAYMENTS",
    "fact_order_items": "FACT_ORDER_ITEMS",
}

for folder_name, snowflake_table in TABLES.items():

    print(f"\nLoading {folder_name}...")

    df = (
        spark.read
        .format("delta")
        .load(str(GOLD_PATH / folder_name))
    )

    pandas_df = df.toPandas()

    success, nchunks, nrows, _ = write_pandas(
        conn,
        pandas_df,
        snowflake_table,
        auto_create_table=True,
        overwrite=True,
    )

    if success:
        print(f"✅ {snowflake_table}: {nrows} rows loaded.")
    else:
        print(f"❌ Failed to load {snowflake_table}")
        
cursor.close()
conn.close()
spark.stop()

print("\n🎉 Gold Layer successfully loaded into Snowflake!") 