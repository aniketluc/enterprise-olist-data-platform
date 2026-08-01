# Table Relationships

## customers

Primary Key:
customer_id

Referenced By:
orders.customer_id

---

## orders

Primary Key:
order_id

Foreign Key:
customer_id

Referenced By:
order_items
payments
reviews

---

## order_items

Primary Key:
(order_id, order_item_id)

Foreign Keys:
product_id
seller_id