import pandas as pd

# 1. Extract data from a CSV file
df = pd.read_csv('employee_data.csv')

# 2. Transforming data

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert types
df['age'] = pd.to_numeric(df['age'], errors = 'coerce')
df['salary'] = pd.to_numeric(df['salary'], errors = 'coerce')

# Drop invalid rows
df = df[(df['age'] > 0) & (df['salary'] >= 0)]

df.to_csv('cleaned_employee_data.csv', index = False)
print("Cleaned data saved. Summary: ")
print(df.describe())