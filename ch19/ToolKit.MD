# Toolkit file of commands and functions for later use

# JSON Files Specifically Top Nested
# Normalizing input and looping into the first value, traversing root
full_names = [
    f"{nameNormal(laureate['firstname'])} {nameNormal(laureate['surname'])}"
    for prize in read_json["prizes"]
    for laureate in prize["laureates"]

# Reusable patterns

- `max(..., key=lambda x: ...)` — find the biggest thing by some rule
- `int(value.strip())` — clean then convert
- `json.load()` → navigate the structure → iterate the list
- `for item in data["key"]` — drill into nested data

# Each one is a reusable block. The real skill isn't memorizing syntax, it's recognizing *which pattern fits the problem* — which is exactly what you just did on line 20 when you knew you needed `max()` but had to figure out how to aim it correctly.

# That `key=` pattern alone will show up constantly: sorting, filtering, grouping. You've got it in the toolbox now.

# Checking for column names prior to working
head -1 car_data.csv | tr ',' '\n'

# Normalizing input
def normalize_text(value):
    """Return lowercase text for consistent searching."""
    return value.strip().lower().replace(" ", "")

# quick use of lambda to find max value
top_era = max(era_to_songs, key=lambda era: len(era_to_songs[era]["so
top_count = len(era_to_songs[top_era]["songs"])
    
results = [f"Era with the most songs: {top_era} ({top_count} songs)"]

# Simple CSV reader and header row search
def search_artist(term):
    matches = []
    with open(file_path, newline="", encoding='utf-8') as artist_list:
        reader = csv.DictReader(artist_list)
        for row in reader:
            artist_name = row["artist_name"]
            if term.lower() in artist_name.lower():
                matches.append(f"{artist_name} = {row['track_name']} ({row['year']})")
    return matches


# Simple CSV Row Writer

# prompt the user for company name, purchase date and number of shares for five 
# add each companys information to a list 
# add each list to a collection of lists
# append the new data to company_stocks.csv
# display the contents

import os, csv

dataset = []

while True:

    if os.path.exists("data/company-stocks.csv"): # will lock if no explicit break
        cinWrite = input("The file exists and is now open in append mode. [quit to exit]")
        if cinWrite.lower() == 'quit':
            break
        elif with open("data/company-stocks.csv","a") as comp:
                writer = csv.writer(comp, delimiter = ',')
                writer.writerow([cinWrite])
                dataset.append(cinWrite)                     
        elif os.path.exists("data/company-stocks.csv"):
            cinWrite = input("The file did not exist and has been created.")
            with open("data/company-stocks.csv","w"):
                writer = csv.writer(comp,delimiter = ',') as comp:
                writer.writerow([cinWrite])
                dataset.append(cinWrite)
    else:
        break
print(comp)



#==========================================================================
# checks for directory and creates the file
# ensure the 'data' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

file_path = 'data/csv002.csv'

while True:
     if os.path.exists(file_path):
          print("File exists, opening in append mode.")

     # open the file in 'a' (append mode)
     # newline = '' prevents extra blank rows in some OS environments
     with open(file_path,'a', newline = '') as csvfile:
          writer = csv.writer(csvfile,delimiter=',')

# comprehensions are really just set-builder notation wearing Python clothes
# reading them left-to-right naturally: "what I want" → "where it comes from" → "filtered by what condition"
[x * 2  for x in numbers  if x > 0]
#  ↑ output   ↑ source       ↑ filter (optional)