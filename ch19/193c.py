# open and read csv file
# count the number of rows in the file
# split into three separate csv files
# each file includes same number of rows
# reassemble in different order

import os
import csv

# 0. Ensure the 'data' folder exists
folder = 'data'
if not os.path.exists(folder):
    os.makedirs(folder)

file_path = os.path.join(folder,'csv005.csv')

print("--- CSV Data Entry Tool ---")
print("Type 'exit' to top. \n")

while True:
    user_input = input("Please input database set: ")
    if user_input.lower() == 'exit':
        break
    
    # 1. append mode ('a') works even if the file is new
    # newline = '' prevents extra blanks rows on windows

    with open(file_path,'a',newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
        # writing input as a single row
        writer.writerow([user_input])

# 1a. Read all data into a list
with open('data/csv005.csv','r',newline='') as f:
    reader = csv.reader(f)
    data_rows = list(reader)


# 2. Calculate the slice size (total rows divided by 3)
total_rows = len(data_rows)
chunk_size = total_rows // 3

# 3. Define the slices
slice1 = data_rows[:chunk_size]
slice2 = data_rows[chunk_size:chunk_size * 2]
slice3 = data_rows[chunk_size * 2:]

# 4 Write each slice to its respective file
files_and_slices = [
    ('data/csv006.csv',slice1),
    ('data/csv007.csv',slice2),
    ('data/csv008.csv',slice3)
]

for filename, data_slice in files_and_slices:
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_slice) # writerows handles the whole list at once

# 5. Write each slice in reverse to one file
output = 'data/csv009.csv'
with open(output,'a',newline='') as f9:
    w9 = csv.writer(f9)
    w9.writerow(slice3)
    w9.writerow(slice2) 
    w9.writerow(slice1)