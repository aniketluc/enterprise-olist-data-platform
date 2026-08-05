select
    s.seller_id,
    s.seller_city,
    s.seller_state,
    count(distinct oi.order_id) as total_orders,
    sum(oi.price) as total_sales,
    avg(oi.price) as average_sale
from {{ ref('stg_dim_sellers') }} s
join {{ ref('stg_fact_order_items') }} oi
    on s.seller_id = oi.seller_id
group by
    s.seller_id,
    s.seller_city,
    s.seller_state