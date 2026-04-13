# open and read csv file
# count the number of rows in the file
# split into three separate csv files
# each file includes same number of rows
# reassemble in different order

import os
import csv

# 0. Ensure the 'data' exists
folder = 'data'
if not os.path.exists(folder):
    os.makedirs(folder)

file_path = os.path.join(folder,'csv005.csv')

print("--- CSV Data Entry Tool ---")
print("Type 'exit' to top.\n")

while True:
    user_input = input("Please enter data to input into the database: ")

    if user_input.lower() == 'exit':
        break

    # 2. append mode ('a') works even if the file is new
    # newline = '' prevents extra blank rows on windows

    with open(file_path,'a', newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter = ',')
        # writing input as a single row
        writer.writerow([user_input])
        
# 1. Read all data in a list first

data_rows = []
with open('data/csv005.csv','r', newline = '') as f:
    reader = csv.reader(f)
    data_rows = list(reader)

# 2 Open all output files at once using a ExitStack or nested 'with'
with (open('data/csv006.csv', 'a', newline = '') as f6, \
    open('data/csv007.csv','a', newline =  '') as f7, \
    open('data/csv008.csv','a', newline = '') as f8):

    w6 = csv.writer(f6)
    w7 = csv.writer(f7)
    w8 = csv.writer(f8)
    
    for row in data_rows:
        # Using slicing you did in your code
        w6.writerow(row[0:1])
        w7.writerow(row[0:1])
        w8.writerow(row[0:1])

with open('data/csv009.csv','a',newline='') as f9:
    w9 = csv.writer(f9)

    for row in data_rows:
        w9.writerow(row[-1:0])
