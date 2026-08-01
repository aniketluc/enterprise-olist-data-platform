# Olist Data Dictionary

## customers

PRows:
99441

**Business Purpose:**
Stores customer information for each order.

**Source File:**
olist_customers_dataset.csv

**Row Count:**
<Fill after profiling>

**Column Count:**
<Fill after profiling>

**Primary Key:**
customer_id

**Candidate Foreign Keys:**
customer_id → orders.customer_id

**Columns:**

| Column Name | Data Type | Nullable | Description |
|-------------|----------|----------|-------------|
| customer_id | string | No | Unique customer identifier |
| customer_unique_id | string | No | Unique customer across multiple orders |
| customer_zip_code_prefix | integer | No | ZIP code prefix |
| customer_city | string | No | Customer city |
| customer_state | string | No | Customer state |

**Nullable Columns:**
- None (update after profiling if needed)

**Important Observations:**
- No duplicate customer_id (verify from profiling)
- customer_unique_id can appear multiple times because one customer may place multiple orders

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