from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def transform_orders(df: DataFrame) -> DataFrame:
    """
    Apply Silver transformations to Orders data.
    """

    return (
        df.dropDuplicates(["order_id"])
          .filter(col("order_purchase_timestamp").isNotNull())
    )


def transform_customers(df: DataFrame) -> DataFrame:
    """
    Apply Silver transformations to Customers data.
    """

    return (
        df.dropDuplicates(["customer_id"])
          .filter(col("customer_unique_id").isNotNull())
    )


def transform_products(df: DataFrame) -> DataFrame:
    """
    Apply Silver transformations to Products data.
    """

    return (
        df.dropDuplicates(["product_id"])
    )


def transform_sellers(df: DataFrame) -> DataFrame:
    """
    Apply Silver transformations to Sellers data.
    """

    return (
        df.dropDuplicates(["seller_id"])
    )


def transform_payments(df: DataFrame) -> DataFrame:
    """
    Apply Silver transformations to Payments data.
    """

    return (
        df.dropDuplicates()
    )