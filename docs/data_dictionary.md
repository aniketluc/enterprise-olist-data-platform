# Olist Data Dictionary

## customers

Primary Key:
- customer_id

Important Columns:
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

---

## orders

Primary Key:
- order_id

Foreign Key:
- customer_id

Important Columns:
- order_status
- order_purchase_timestamp
- order_delivered_customer_date
- order_estimated_delivery_date

---

## order_items

Primary Key:
- order_id + order_item_id

Foreign Keys:
- product_id
- seller_id

...