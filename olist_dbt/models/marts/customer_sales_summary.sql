select
    c.customer_id,
    c.customer_city,
    c.customer_state,
    count(distinct o.order_id) as total_orders,
    sum(p.total_payment) as total_spent,
    avg(p.total_payment) as average_order_value
from {{ ref('stg_dim_customers') }} c
join {{ ref('stg_fact_orders') }} o
    on c.customer_id = o.customer_id
join {{ ref('stg_fact_payments') }} p
    on o.order_id = p.order_id
group by
    c.customer_id,
    c.customer_city,
    c.customer_state