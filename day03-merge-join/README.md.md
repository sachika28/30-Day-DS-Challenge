# Day 03 — Merge & Join Practice

**30-Day Data Science Challenge**

## Problem

Real-world data rarely lives in one table. This project works with 3 separate CSVs — orders, customers, and products — and combines them using different join types to derive business insights that aren't possible from any single table alone.

## Dataset

Three related tables representing a retail operation.

| Table | Rows | Description |
|---|---|---|
| customers.csv | 100 | Customer profiles — city, segment, tenure |
| products.csv | 16 | Product catalogue — category, unit price |
| orders.csv | 400 | Transactional data — customer, product, quantity, revenue |

## What This Covers

- Cleaning dirty data before joining (trailing characters in order_id)
- INNER JOIN — orders matched with product details
- LEFT JOIN — retaining all orders even when customer data is missing
- Detecting orphan records (orders with no matching customer)
- Multi-table aggregations for business insights

## Insights Derived

| # | Insight | Method |
|---|---|---|
| 1 | Revenue breakdown by customer segment (Retail / Wholesale / Online) | LEFT JOIN + groupby |
| 2 | Top 5 highest-value customers with city | LEFT JOIN + groupby + sort |
| 3 | Best-performing product category per city | LEFT JOIN + groupby + first |

## JOIN Types Used

| Join | Behaviour | Used For |
|---|---|---|
| INNER JOIN | Only matching rows from both tables | Orders with valid product data |
| LEFT JOIN | All rows from left table, NaN for unmatched right | Keep all orders, flag missing customers |

## Files

- `customers.csv` — customer profiles
- `products.csv` — product catalogue
- `orders.csv` — raw transactional data
- `day03_merge_join.py` — analysis script
- `orders_merged.csv` — fully joined output table

## Tools

Python · Pandas
