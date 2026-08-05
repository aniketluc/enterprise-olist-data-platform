from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    sum,
)


def create_dim_customers(customers_df: DataFrame) -> DataFrame:
    """
    Create Customer Dimension.
    """

    return (
        customers_df.select(
            "customer_id",
            "customer_unique_id",
            "customer_city",
            "customer_state",
        )
        .dropDuplicates()
    )


def create_dim_products(products_df: DataFrame) -> DataFrame:
    """
    Create Product Dimension.
    """

    return (
        products_df.select(
            "product_id",
            "product_category_name",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm",
        )
        .dropDuplicates()
    )


def create_dim_sellers(sellers_df: DataFrame) -> DataFrame:
    """
    Create Seller Dimension.
    """

    return (
        sellers_df.select(
            "seller_id",
            "seller_city",
            "seller_state",
        )
        .dropDuplicates()
    )


def create_fact_payments(payments_df: DataFrame) -> DataFrame:
    """
    Create Payment Fact Table.
    """

    return (
        payments_df.groupBy("order_id")
        .agg(
            sum("payment_value").alias("total_payment")
        )
    )


def create_fact_orders(orders_df: DataFrame) -> DataFrame:
    """
    Create Orders Fact Table.
    """

    return (
        orders_df.select(
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        )
    )
    
def create_fact_order_items(order_items_df: DataFrame) -> DataFrame:
    """
    Create Order Items Fact Table.
    """

    return (
        order_items_df.select(
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "shipping_limit_date",
            "price",
            "freight_value",
        )
    )