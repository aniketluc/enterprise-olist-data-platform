from pathlib import Path

# -----------------------------------------------------------------------------
# Project Paths
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_PATH = DATA_DIR / "raw"

BRONZE_DATA_PATH = DATA_DIR / "bronze"

SILVER_DATA_PATH = DATA_DIR / "silver"

GOLD_DATA_PATH = DATA_DIR / "gold"

# -----------------------------------------------------------------------------
# Olist Dataset Mapping
# -----------------------------------------------------------------------------

TABLES = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

# -----------------------------------------------------------------------------
# Bronze Table Names
# -----------------------------------------------------------------------------

BRONZE_TABLES = {
    table: f"bronze_{table}"
    for table in TABLES
}