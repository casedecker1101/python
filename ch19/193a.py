# open and read csv file
# count the number of rows in the file
# split into three separate csv files
# each file includes same number of rows
# reassemble in different order

import os
import csv

# 1. ensure the 'data' exists
folder = 'data'
if not os.path.exists(folder):
    os.makedirs(folder)

file_path = os.path.join(folder, 'csv005.csv')

print("--- CSV Data Entry Tool ---")
print("Type 'exit' to top.\n")

while True:
    user_input = input("Please enter data to input into the database: ")

    if user_input.lower() == 'exit':
        break

       # 2. append mode ('a') works even  if the file is new
       # newline = '' prevents extra blank rows on Windows
    with open(file_path,'a', newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
        # writing input as a single row
        writer.writerow([user_input])
    
    with open('data/csv005.csv','a',newline='') as f:
        csv_file = csv.reader(f, delimiter = ',')
        row_count = 0
        for row in csv_file:
            row_count += 1 # increment by 1 for ever row found
            print({row_count})

    with open('data/csv006.csv','a',newline='') as fsix:
        writer = csv.writer(fsix,delimiter=',')
        for row in csv_file:
            writer.writerow([row[0:1]])
    
    with open('data/csv007.csv','a',newline='') as fseven:
        writer = csv.writer(csvfile,delimiter = ',')
        for row in csv_file:
            writer.writerow([row[2:3]])
        
    with open('data/csv008.csv)','a',newline='') as feight:
        writer = csv.writer(csvfile,delimiter = ',')
        for row in csv_file:
            writer.writerow([row[4:5]])

    with open('data/csv009.csv)','a',newline='') as fnine:
        writer = csv.writer(csvfile,delimiter  = ',')
        for row in csv_file:
            writer.writerow(feight)
            writer.writerow(fseven)
            writer.writerow(fsix)b