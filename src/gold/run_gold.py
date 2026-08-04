from pathlib import Path

from src.bronze.config import SILVER_DATA_PATH, GOLD_DATA_PATH
from src.silver.reader import get_spark_session, read_delta
from src.silver.writer import write_silver

from src.gold.gold_transformation import (
    create_dim_customers,
    create_dim_products,
    create_dim_sellers,
    create_fact_orders,
    create_fact_payments,
)


def main():

    spark = get_spark_session("Gold Transformation")

    customers = read_delta(spark, SILVER_DATA_PATH / "customers")
    products = read_delta(spark, SILVER_DATA_PATH / "products")
    sellers = read_delta(spark, SILVER_DATA_PATH / "sellers")
    orders = read_delta(spark, SILVER_DATA_PATH / "orders")
    payments = read_delta(spark, SILVER_DATA_PATH / "payments")

    write_silver(
        create_dim_customers(customers),
        GOLD_DATA_PATH / "dim_customers",
    )

    write_silver(
        create_dim_products(products),
        GOLD_DATA_PATH / "dim_products",
    )

    write_silver(
        create_dim_sellers(sellers),
        GOLD_DATA_PATH / "dim_sellers",
    )

    write_silver(
        create_fact_orders(orders),
        GOLD_DATA_PATH / "fact_orders",
    )

    write_silver(
        create_fact_payments(payments),
        GOLD_DATA_PATH / "fact_payments",
    )

    spark.stop()


if __name__ == "__main__":
    main()