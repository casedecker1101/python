# prompt the user for company name, purchase date and number of shares for five 
# add each companys information to a list 
# add each list to a collection of list
# append the new data to company_stocks.csv
# display the contents

import os, csv

dataset = []

while True:
    if os.path.exists("data/company-stocks.csv"):
        print("Enter Stock name, purchase date and price.")
        print("Use Quotes for Names and separate with commas.")
        cinWrite = input("The file exists and is now open in append mode. [quit to exit] ")
        if cinWrite.lower() == 'quit':
            with open("data/company-stocks.csv","r") as stocks:
                csv_read = csv.reader(stocks,delimiter = ',')
                stocks.readline()
                print(csv_read)
                for read in csv_read:
                    print(read)
            break
        else:
            with open("data/company-stocks.csv","a") as comp:
                writer = csv.writer(comp, delimiter = ',')
                writer.writerow([cinWrite])
                dataset.append(cinWrite)
                csv_read = csv.reader(comp,delimiter = ',')           
                print(csv_read)