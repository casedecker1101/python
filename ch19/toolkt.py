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
