from dateutil import parser
import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv('dataset.csv')

# Ensure customer_id is treated as a string
if 'customer_id' in data.columns:
  data['customer_id'] = data['customer_id'].astype(str)

# Numeric columns: Fill missing values with the mean
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
  data[col].fillna(data[col].mean(), inplace=True)

# Categorical columns: Fill missing values with the mode
categorical_cols = data.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if data[col].isnull().any():
        data[col].fillna(data[col].mode()[0], inplace=True)

# Handle Outliers (IQR method)
def handle_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])

# Apply to numeric columns
for col in numeric_cols:
    handle_outliers_iqr(data, col)

# Standardize Date Formats
def standardize_date_format(date_series):
    return date_series.apply(lambda x: parser.parse(x, fuzzy=True) if pd.notnull(x) else pd.NaT)

if 'transaction_date' in data.columns:
    data['transaction_date'] = standardize_date_format(data['transaction_date'])

# Resolving Categorical Discrepancies
def clean_categorical_labels(column):
    # Ensure all values are strings and handle NaN values
    column = column.astype(str).fillna('missing')
    # Lowercase all labels and strip extra whitespace
    return column.str.lower().str.strip()


for col in categorical_cols:
    data[col] = clean_categorical_labels(data[col])

# Reduce Memory Usage
def reduce_memory_usage(df):
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type == 'float64':
            df[col] = df[col].astype('float32')
        elif col_type == 'int64':
            df[col] = df[col].astype('int32')
        elif col_type == 'object':
            df[col] = df[col].astype('category')
    return df

data = reduce_memory_usage(data)

# Save Data to Parquet Format
data.to_parquet('clean_dataset.parquet', index=False)

print("Data cleaning and optimization completed. File saved as 'clean_dataset.parquet'.")
