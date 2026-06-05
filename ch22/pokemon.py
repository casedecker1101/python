import requests
import pandas as pd

# 1. Extracting data from the API
url = "https://pokeapi.co/api/v2/pokemon?limit=50"
response = requests.get(url)
data = response.json()["results"]

df = pd.DataFrame(data)

# 2. Transforming the data 
df["name"] = df["name"].str.title() # capitalize the first letter of each name

# 3. Load the data into a CSV file
df.to_csv("pokemon_list.csv", index=False)
print("Data has been saved.")
