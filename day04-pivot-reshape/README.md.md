# Day 04 — Pivot Tables & Reshaping

**30-Day Data Science Challenge**

## Problem

Raw data often comes in wide format — especially exports from Excel or ERP systems where each time period is a separate column. This project takes a wide-format monthly sales dataset and reshapes it using `melt`, `pivot_table`, and `pivot` to answer questions that are difficult or impossible to answer from the original structure.

## Dataset

Monthly sales data for 4 regions × 4 product categories across 12 months of 2024 — initially in wide format (one column per month).

| Column | Description |
|---|---|
| region | North / South / East / West |
| category | Electronics / Clothing / Food & Beverage / Home & Kitchen |
| Jan–Dec | Monthly revenue figures (wide format) |

## What This Covers

| Operation | Method | Purpose |
|---|---|---|
| Wide → Long | `pd.melt()` | Converts month columns into rows for analysis |
| Region × Month summary | `pd.pivot_table()` | Total revenue per region per month |
| Category × Region summary | `pd.pivot_table(margins=True)` | Cross-tab with row/column totals |
| Monthly average per category | `pd.pivot_table(aggfunc='mean')` | Smoothed trend by category |
| Long → Wide (restore) | `df.pivot()` | Reconstruct original structure from long format |

## Insights Derived

- Peak revenue month per region
- Lowest revenue month per category
- Category and regional performance across the full year

## When to Use Each

- **`melt`** — when you need to go from wide to long (multiple columns → one column + one label column)
- **`pivot_table`** — when you need to summarise and aggregate (like a GroupBy but in 2D grid form)
- **`pivot`** — when you need to go from long to wide without aggregating (one value per row)

## Files

- `monthly_sales_wide.csv` — raw input (wide format)
- `day04_pivot_reshape.py` — analysis script
- `monthly_sales_long.csv` — melted long format output
- `pivot_region_month.csv` — region × month pivot table

## Tools

Python · Pandas
