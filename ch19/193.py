# open and read csv file
# count the number of rows in the file
# split into three separate csv files
# each file includes same number of rows
# reassemble in different order

import os 
import csv
 
# ensure the 'data' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

file_path = 'data/csv003.csv'

while True:
    if not os.path.exists(file_path):
        print("File does not exist, creating new file.")
        with open(file_path,'w',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter = ",")
    elif print("File exists, opening in append mode."):
        # open the file in 'a' (append mode)
        # newline = '' prevents extra blank rows in some OS environments
        with open(file_path,'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter = ",")
            user_input = input("Please enter data to input into the database:   ")

            # writing the input as a single row
            writer.writerow([user_input])