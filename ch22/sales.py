import pandas as pd

# 1. Extracting data from a CSV file
df = pd.read_csv('sales_data.csv')

# 2. Transforming data
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Trim whitespace in string columns
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# Convert types
df["sales_date"] = pd.to_datetime(df["sales_date"], errors = 'coerce')
df["price"] = pd.to_numeric(df["price"], errors = 'coerce')
df["quantity"] = pd.to_numeric(df["quantity"], errors = 'coerce')

# Drop rows with missing critical values
df = df.dropna(subset=["sales_date", "price", "quantity"])

# Remove invalid rows
df = df[(df["price"] > 0) & (df["quantity"] >= 0)]

# Remove duplicates
df = df.drop_duplicates()

# 3. Loading cleaned data into a new CSV file
df.to_csv('cleaned_sales_data.csv', index = False)
print("Cleaned data saved. Summary: ")
print(df.describe())
