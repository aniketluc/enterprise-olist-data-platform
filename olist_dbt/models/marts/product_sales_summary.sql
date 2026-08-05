select
    p.product_id,
    p.product_category_name,
    count(distinct oi.order_id) as total_orders,
    sum(oi.price) as total_sales,
    avg(oi.price) as average_price
from {{ ref('stg_dim_products') }} p
join {{ ref('stg_fact_order_items') }} oi
    on p.product_id = oi.product_id
group by
    p.product_id,
    p.product_category_name