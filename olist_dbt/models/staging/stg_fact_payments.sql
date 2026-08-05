select
    "order_id" as order_id,
    "total_payment" as total_payment
from {{ source('gold', 'FACT_PAYMENTS') }}