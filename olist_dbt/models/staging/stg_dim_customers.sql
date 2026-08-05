select
    "customer_id" as customer_id,
    "customer_unique_id" as customer_unique_id,
    "customer_city" as customer_city,
    "customer_state" as customer_state
from {{ source('gold', 'DIM_CUSTOMERS') }}