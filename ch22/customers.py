import pandas as pd
import json

# 1. Extracting data from a JSON file
with open('data/customers.json') as f:
    data = json.load(f)

df = pd.json_normalize(data['customers'])

# 2. Transforming data
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 3. Load transformed data into a new CSV file
df.to_csv('cleaned_customers.csv', index = False)
print("Cleaned data saved. Summary: ")
print(df.describe())