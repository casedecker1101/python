# Removing an attribute
# Prompts the user for the path of an existing csv file and attribute in that file
# Reads the data from the file
# removes the specified attribute
# saves transformed data to a new csv file

import csv
dataset = list()

def toCSV(input_file, attribute):
    with open(input_file) as inputCSV:
        reader = csv.DictReader(inputCSV)
        dataset.append(reader)
    return dataset

def transform_row(row, attribute):
    # your custom logic here
    row[attribute] = row[attribute].strip().title()
    return row

def write_csv(path, rows):
    if not rows:
        return
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

# Orchestrator
src = input("Enter CSV path: ")
attr = input("Enter attribute to clean: ")

rows = toCSV(src)
cleaned = [transform_row(r, attr) for r in rows]
write_csv("cleaned.csv", cleaned)