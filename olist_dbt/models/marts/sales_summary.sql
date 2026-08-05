select
    count(distinct order_id) as total_orders,
    sum(price) as gross_sales,
    sum(freight_value) as total_freight,
    avg(price) as average_item_price
from {{ ref('stg_fact_order_items') }}