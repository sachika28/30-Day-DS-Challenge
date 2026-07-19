import pandas as pd
import numpy as np

# ── Load data ─────────────────────────────────────────────────
df_wide = pd.read_csv('monthly_sales_wide.csv')

print("=" * 55)
print("PIVOT TABLES & RESHAPING — MONTHLY SALES ANALYSIS")
print("=" * 55)
print(f"\nDataset shape (wide): {df_wide.shape}")
print("\nFirst 3 rows (wide format):")
print(df_wide.head(3).to_string(index=False))

# ── Step 1: melt — wide to long ───────────────────────────────
# Wide: each month is a column (14 columns)
# Long: each row is one region-category-month combination
months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

df_long = df_wide.melt(
    id_vars=["region", "category"],
    value_vars=months,
    var_name="month",
    value_name="revenue"
)
df_long["month"] = pd.Categorical(df_long["month"], categories=months, ordered=True)
df_long = df_long.sort_values(["region", "category", "month"]).reset_index(drop=True)

print(f"\nAfter melt (long format): {df_long.shape}")
print("Each row = one region + category + month combination")
print(df_long.head(6).to_string(index=False))

# ── Step 2: pivot_table — region vs month ────────────────────
print("\n── Pivot: Total Revenue by Region x Month ─────────────")
pivot_region_month = pd.pivot_table(
    df_long,
    values="revenue",
    index="region",
    columns="month",
    aggfunc="sum"
).round(0).astype(int)
print(pivot_region_month.to_string())

# ── Step 3: pivot_table — category vs region ─────────────────
print("\n── Pivot: Total Revenue by Category x Region ──────────")
pivot_cat_region = pd.pivot_table(
    df_long,
    values="revenue",
    index="category",
    columns="region",
    aggfunc="sum",
    margins=True,
    margins_name="Total"
).round(0).astype(int)
print(pivot_cat_region.to_string())

# ── Step 4: pivot_table — monthly trend per category ─────────
print("\n── Pivot: Avg Monthly Revenue per Category ─────────────")
pivot_cat_month = pd.pivot_table(
    df_long,
    values="revenue",
    index="category",
    columns="month",
    aggfunc="mean"
).round(0).astype(int)
print(pivot_cat_month.to_string())

# ── Step 5: long back to wide (pivot) ────────────────────────
print("\n── Long back to Wide using pivot ───────────────────────")
df_back_wide = df_long.pivot(
    index=["region", "category"],
    columns="month",
    values="revenue"
).reset_index()
df_back_wide.columns.name = None
print(f"Shape restored: {df_back_wide.shape}")
print(df_back_wide.head(3).to_string(index=False))

# ── Step 6: Insight — best month per region ──────────────────
print("\n── Insight: Peak Revenue Month per Region ──────────────")
region_monthly = df_long.groupby(["region", "month"])["revenue"].sum().reset_index()
peak = region_monthly.loc[region_monthly.groupby("region")["revenue"].idxmax()]
print(peak.to_string(index=False))

# ── Step 7: Insight — worst month per category ───────────────
print("\n── Insight: Lowest Revenue Month per Category ──────────")
cat_monthly = df_long.groupby(["category", "month"])["revenue"].sum().reset_index()
worst = cat_monthly.loc[cat_monthly.groupby("category")["revenue"].idxmin()]
print(worst.to_string(index=False))

# ── Save outputs ──────────────────────────────────────────────
df_long.to_csv("monthly_sales_long.csv", index=False)
pivot_region_month.to_csv("pivot_region_month.csv")
print("\nSaved monthly_sales_long.csv and pivot_region_month.csv")
