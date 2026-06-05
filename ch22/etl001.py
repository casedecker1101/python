import pandas as pd  # type: ignore

# 1. Extract data from a CSV file
df = pd.read_csv('JobReadyPython/data/got_chars.csv')

# 2. Transform the data
df.columns = df.columns.str.strip() # Remove leading/trailing whitespace from column names
df.columns = df.columns.str.lower() # Convert column names to lowercase
df.columns = df.columns.str.replace(' ', '_') # Replace spaces with underscores in column names
df.columns = df.columns.str.replace("", " ") # Replace empty strings with space in column names
df.columns = df.columns.str.replace("\" \"", " ") # Replace double quotes with space in column names


df['actor'] = df['actor'].str.strip() # Remove leading/trailing whitespace from the 'name' column
df['character'] = df['character'].str.title() # Conver the 'character' column to title case
df['first_appearance'] = pd.to_numeric(df['first_appearance'], errors = 'coerce') # Convert the 'first_appearance' column to numeric, coercing errors to NaN

# Remove duplicates
df = df.drop_duplicates()

# 3. Load the transformed data into a new CSV file
df.to_csv('JobReadyPython/data/got_chars_cleaned.csv', index = False)