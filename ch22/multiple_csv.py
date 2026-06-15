import pandas as pd
import glob


# 1. Extracting Data from Multiple CSV Files
# Get a list of all csv files in the current directory
csv_files = glob.glob('JobReadyPython/data/*.csv')
dfs = [pd.read_csv(f) for f in csv_files]

# 2 Transforming Data
df = pd.concat(dfs, ignore_index = True)
df = df.drop_duplicates()

# 3. Loading merged data into a new CSV File
df.to_csv('merged_data.csv', index = False)