import pandas as pd

# ── Load the 3 tables ─────────────────────────────────────────
customers = pd.read_csv('customers.csv')
products  = pd.read_csv('products.csv')
orders    = pd.read_csv('orders.csv')

print("=" * 55)
print("MERGE & JOIN ANALYSIS — ORDERS / CUSTOMERS / PRODUCTS")
print("=" * 55)
print(f"\ncustomers : {customers.shape}")
print(f"products  : {products.shape}")
print(f"orders    : {orders.shape}")

# ── Step 1: Clean order_id (trailing comma) ───────────────────
orders['order_id'] = orders['order_id'].str.strip().str.rstrip(',')

# ── Step 2: INNER JOIN — orders + products ────────────────────
# Only keeps orders where product_id exists in products table
orders_products = orders.merge(products, on='product_id', how='inner')
print(f"\nAfter orders INNER JOIN products: {orders_products.shape}")

# ── Step 3: LEFT JOIN — add customer info ─────────────────────
# Keeps all orders; customer info is NULL for unmatched customer_ids
full = orders_products.merge(customers, on='customer_id', how='left')
print(f"After LEFT JOIN customers: {full.shape}")

# ── Step 4: Orphan orders — orders with no matching customer ──
orphan_orders = full[full['customer_name'].isna()]
print(f"\nOrphan orders (no matching customer): {len(orphan_orders)}")
print(orphan_orders[['order_id', 'customer_id', 'revenue']].head())

# ── Step 5: INSIGHT 1 — Revenue by customer segment ──────────
print("\n── Insight 1: Revenue by Customer Segment ─────────────")
seg_revenue = (
    full.dropna(subset=['segment'])
    .groupby('segment')['revenue']
    .agg(total_revenue='sum', order_count='count', avg_order='mean')
    .sort_values('total_revenue', ascending=False)
    .round(2)
)
print(seg_revenue)

# ── Step 6: INSIGHT 2 — Top 5 customers by revenue ───────────
print("\n── Insight 2: Top 5 Customers by Revenue ──────────────")
top_customers = (
    full.dropna(subset=['customer_name'])
    .groupby(['customer_id', 'customer_name', 'city'])['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .round(2)
    .reset_index()
)
print(top_customers.to_string(index=False))

# ── Step 7: INSIGHT 3 — Best category per city ───────────────
print("\n── Insight 3: Top Category by Revenue per City ────────")
city_cat = (
    full.dropna(subset=['city'])
    .groupby(['city', 'category'])['revenue']
    .sum()
    .reset_index()
    .sort_values('revenue', ascending=False)
    .groupby('city')
    .first()
    .reset_index()
    .rename(columns={'revenue': 'top_category_revenue'})
)
print(city_cat.to_string(index=False))

# ── Step 8: INNER vs LEFT JOIN comparison ────────────────────
print("\n── JOIN Comparison ─────────────────────────────────────")
inner = orders.merge(customers, on='customer_id', how='inner')
left  = orders.merge(customers, on='customer_id', how='left')
print(f"INNER JOIN rows: {len(inner)}  (drops unmatched customer_ids)")
print(f"LEFT JOIN rows : {len(left)}   (keeps all orders, NaN for missing customers)")

# ── Save final merged table ───────────────────────────────────
full.to_csv('orders_merged.csv', index=False)
print("\nSaved orders_merged.csv")
