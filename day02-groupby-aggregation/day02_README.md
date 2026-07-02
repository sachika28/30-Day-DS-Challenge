# Day 02 — GroupBy & Aggregation

**30-Day Data Science Challenge**

## Problem

Retail sales data sits in a single flat table — not very useful on its own. This project slices it by region and category to surface revenue patterns, top products, and monthly trends using pandas `groupby`, `agg`, `pivot_table`, and `transform`.

## Dataset

Synthetic retail sales data — 500 orders across 4 regions and 4 product categories for the year 2024.

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| date | Order date |
| region | North / South / East / West |
| category | Electronics / Clothing / Food & Beverage / Home & Kitchen |
| product | Product name |
| quantity | Units ordered |
| unit_price | Price per unit (INR) |
| discount_% | Discount applied |
| revenue | Final revenue after discount |

## Questions Answered

| # | Question | Method |
|---|---|---|
| 1 | Total revenue, order count, and average order value by category | `groupby` + `agg` |
| 2 | Revenue, average discount, and order count by region | `groupby` + `agg` |
| 3 | Top-selling product per category by revenue | `groupby` + `first` |
| 4 | Monthly revenue trend across 2024 | `groupby` on month period |
| 5 | Each category's % share of total revenue | `groupby` + `apply` |
| 6 | Region vs. category revenue matrix | `pivot_table` |
| 7 | Each order's % contribution to its region's total | `transform` |

## Key Findings

- Run the script to see results — findings vary with the dataset.
- `transform` is particularly useful in Q7: it adds a column without collapsing rows, unlike `agg`.

## Files

- `retail_sales_data.csv` — raw input
- `day02_groupby_aggregation.py` — analysis script
- `retail_sales_analysed.csv` — output with added columns

## Tools

Python · Pandas · NumPy
