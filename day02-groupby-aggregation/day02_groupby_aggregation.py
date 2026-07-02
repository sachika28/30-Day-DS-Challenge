import pandas as pd
import numpy as np

df = pd.read_csv('retail_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

print("=" * 55)
print("RETAIL SALES — GROUPBY & AGGREGATION ANALYSIS")
print("=" * 55)
print(f"\nDataset: {df.shape[0]} orders | {df['date'].dt.year.unique()[0]}")
print(f"Regions: {sorted(df['region'].unique())}")
print(f"Categories: {sorted(df['category'].unique())}")

# ── Q1: Total revenue and order count by category ────────────
print("\n── Q1: Revenue & Orders by Category ──────────────────")
q1 = (
    df.groupby('category')
    .agg(
        total_revenue=('revenue', 'sum'),
        total_orders=('order_id', 'count'),
        avg_order_value=('revenue', 'mean')
    )
    .sort_values('total_revenue', ascending=False)
    .round(2)
)
print(q1)

# ── Q2: Revenue by region ────────────────────────────────────
print("\n── Q2: Revenue by Region ──────────────────────────────")
q2 = (
    df.groupby('region')
    .agg(
        total_revenue=('revenue', 'sum'),
        avg_discount=('discount_%', 'mean'),
        total_orders=('order_id', 'count')
    )
    .sort_values('total_revenue', ascending=False)
    .round(2)
)
print(q2)

# ── Q3: Top product per category by revenue ──────────────────
print("\n── Q3: Top Product per Category ───────────────────────")
q3 = (
    df.groupby(['category', 'product'])['revenue']
    .sum()
    .reset_index()
    .sort_values('revenue', ascending=False)
    .groupby('category')
    .first()
    .round(2)
)
print(q3)

# ── Q4: Monthly revenue trend ────────────────────────────────
print("\n── Q4: Monthly Revenue Trend ──────────────────────────")
q4 = (
    df.groupby('month')['revenue']
    .sum()
    .round(2)
    .reset_index()
)
q4.columns = ['month', 'revenue']
print(q4.to_string(index=False))

# ── Q5: Category % share of total revenue ───────────────────
print("\n── Q5: Category Revenue Share ─────────────────────────")
total = df['revenue'].sum()
q5 = (
    df.groupby('category')['revenue']
    .sum()
    .apply(lambda x: round(x / total * 100, 2))
    .sort_values(ascending=False)
    .reset_index()
)
q5.columns = ['category', 'revenue_share_%']
print(q5.to_string(index=False))

# ── Q6: Region x Category revenue matrix ────────────────────
print("\n── Q6: Region x Category Revenue Matrix ───────────────")
q6 = df.pivot_table(
    values='revenue',
    index='region',
    columns='category',
    aggfunc='sum'
).round(0).astype(int)
print(q6)

# ── Q7: transform — add each order's % of its region total ──
print("\n── Q7: Each Order's Share of Region Revenue ───────────")
df['region_total'] = df.groupby('region')['revenue'].transform('sum')
df['pct_of_region'] = (df['revenue'] / df['region_total'] * 100).round(3)
print(df[['order_id', 'region', 'revenue', 'region_total', 'pct_of_region']].head(10).to_string(index=False))

# ── Save enriched dataset ────────────────────────────────────
df.to_csv('retail_sales_analysed.csv', index=False)
print("\nSaved retail_sales_analysed.csv")
