select
    "seller_id" as seller_id,
    "seller_city" as seller_city,
    "seller_state" as seller_state
from {{ source('gold', 'DIM_SELLERS') }}