# Day 01 — Data Cleaning Challenge

**30-Day Data Science Challenge**

## Problem
Real-world manufacturing quality data is rarely clean. This project takes a messy factory dataset — with duplicate rows, inconsistent factory name spellings, mixed date formats, string junk in numeric columns, and missing values — and produces a clean, analysis-ready CSV.

## Dataset
Synthetic manufacturing quality data styled after soap/personal care production metrics.

| Column | Description |
|---|---|
| Batch_ID | Production batch identifier |
| Date | Batch date (inconsistent formats) |
| Factory | Plant name (multiple spelling variants) |
| Ingredient | Noodles / PAS / Perfume / Frisis |
| Cp, Cpk | Process capability indices |
| Pp, Ppk | Performance indices |
| Dosing_Accuracy_% | Ingredient dosing accuracy |

## Issues Found & Fixed

| Issue | Fix |
|---|---|
| 15 duplicate rows | `drop_duplicates()` |
| String junk in numeric cols (`N/A`, `-`, `error`) | `pd.to_numeric(errors='coerce')` |
| Missing values across all numeric columns | Median imputation |
| 30+ factory name variants (inconsistent case/spelling) | Standardized via lowercase + mapping dict |
| 4 different date formats | `pd.to_datetime(infer_datetime_format=True)` |
| Outliers in Cpk and Dosing | IQR method — flagged, not dropped |

## Before vs After

| | Rows | Issues |
|---|---|---|
| Before | 315 | Duplicates, nulls, mixed types, dirty text |
| After | 300 | Clean, fully typed, standardized |

## Files
- `messy_factory_data.csv` — raw input
- `day01_data_cleaning.ipynb` — full cleaning notebook
- `clean_factory_data.csv` — output

## Tools
Python · Pandas · NumPy
