select
    "product_id" as product_id,
    "product_category_name" as product_category_name,
    "product_weight_g" as product_weight_g,
    "product_length_cm" as product_length_cm,
    "product_height_cm" as product_height_cm,
    "product_width_cm" as product_width_cm
from {{ source('gold', 'DIM_PRODUCTS') }}