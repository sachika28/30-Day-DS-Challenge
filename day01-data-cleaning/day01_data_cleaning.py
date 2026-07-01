import pandas as pd
import numpy as np

# ── Step 1: Load ──────────────────────────────────────────────
df = pd.read_csv('messy_factory_data.csv')
print('Original shape:', df.shape)
print('\nMissing values:\n', df.isnull().sum())
print('\nDuplicates:', df.duplicated().sum())
print('\nFactory name variants:\n', df['Factory'].value_counts())

# ── Step 2: Remove duplicates ─────────────────────────────────
df = df.drop_duplicates().reset_index(drop=True)
print('\nAfter removing duplicates:', df.shape)

# ── Step 3: Fix dtypes ────────────────────────────────────────
for col in ['Cp', 'Cpk', 'Dosing_Accuracy_%']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ── Step 4: Impute missing values with median ─────────────────
for col in ['Cp', 'Cpk', 'Pp', 'Ppk', 'Dosing_Accuracy_%']:
    df[col] = df[col].fillna(df[col].median())

print('\nMissing after imputation:\n', df.isnull().sum())

# ── Step 5: Standardize factory names ────────────────────────
factory_map = {
    'pondicherry pc': 'Pondicherry PC', 'pondichery pc': 'Pondicherry PC',
    'pondicherry':    'Pondicherry PC', 'llpl': 'LLPL',
    'l.l.p.l':        'LLPL', 'llpl ': 'LLPL',
    'nepal pc':       'Nepal PC', 'nepal': 'Nepal PC',
    'haridwar pc':    'Haridwar PC', 'haridwar': 'Haridwar PC',
    'khamgaon':       'Khamgaon', 'khamagon': 'Khamgaon',
    'khamgoan':       'Khamgaon', 'sumerpur pc': 'Sumerpur PC',
    'sumerpur':       'Sumerpur PC',
}
df['Factory'] = df['Factory'].str.strip().str.lower().map(
    lambda x: factory_map.get(x, x.title())
)

# ── Step 6: Standardize dates ─────────────────────────────────
df['Date'] = pd.to_datetime(df['Date'], dayfirst=False, infer_datetime_format=True, errors='coerce')

# ── Step 7: Flag outliers (IQR) ───────────────────────────────
for col in ['Cpk', 'Dosing_Accuracy_%']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df[f'{col}_outlier'] = (df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)

# ── Step 8: Save ──────────────────────────────────────────────
df.to_csv('clean_factory_data.csv', index=False)
print('\nFinal shape:', df.shape)
print('Saved clean_factory_data.csv ✓')
