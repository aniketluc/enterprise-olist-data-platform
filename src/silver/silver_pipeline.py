# from pathlib import Path
# from pyspark.sql import SparkSession

# from src.bronze.config import BRONZE_DATA_PATH
# from src.silver.reader import read_bronze_table
# from src.silver.transformer import (
#     transform_customers,
#     transform_orders,
#     transform_products,
#     transform_sellers,
#     transform_payments,
# )
# from src.silver.validator import validate_dataframe
# from src.silver.writer import write_silver_table


# BRONZE_PATH = "data/bronze"
# SILVER_PATH = "data/silver"


# def main():

#     spark = (
#         SparkSession.builder
#         .appName("Silver Layer")
#         .getOrCreate()
#     )

#     datasets = [
#         ("customers", transform_customers, "customer_id"),
#         ("orders", transform_orders, "order_id"),
#         ("products", transform_products, "product_id"),
#         ("sellers", transform_sellers, "seller_id"),
#         ("payments", transform_payments, "order_id"),
#     ]

#     for name, transformer, primary_key in datasets:

#         print(f"\nProcessing {name}...")

#         # df = read_bronze_table(
#         #     spark,
#         #     f"{BRONZE_PATH}/{name}"
#         # )
        
#         df = read_delta(
#         spark,
#         Path(BRONZE_DATA_PATH / BRONZE_TABLES[name])
#         )

#         df = transformer(df)

#         validate_dataframe(df, primary_key)

#         write_silver_table(
#             df,
#             f"{SILVER_PATH}/{name}"
#         )

#     spark.stop()


# if __name__ == "__main__":
#     main()

from pathlib import Path

from src.bronze.config import (
    BRONZE_DATA_PATH,
    SILVER_DATA_PATH,
    BRONZE_TABLES,
)

from src.silver.reader import (
    get_spark_session,
    read_delta,
)

from src.silver.transformer import (
    transform_customers,
    transform_orders,
    transform_products,
    transform_sellers,
    transform_payments,
    transform_order_items,
)

from src.silver.validator import validate_dataframe

from src.silver.writer import write_silver


def main():

    spark = get_spark_session("Silver Layer")

    datasets = [
        ("customers", transform_customers, "customer_id"),
        ("orders", transform_orders, "order_id"),
        ("products", transform_products, "product_id"),
        ("sellers", transform_sellers, "seller_id"),
        ("payments", transform_payments, "order_id"),
        ("order_items", transform_order_items, "order_id"),
    ]   

    for name, transformer, primary_key in datasets:

        print(f"\nProcessing {name}...")

        df = read_delta(
            spark,
            Path(BRONZE_DATA_PATH / BRONZE_TABLES[name]),
        )

        df = transformer(df)

        validate_dataframe(df, primary_key)

        write_silver(
            df,
            Path(SILVER_DATA_PATH / name),
        )

    spark.stop()


if __name__ == "__main__":
    main()