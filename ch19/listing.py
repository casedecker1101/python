# 19.1 reading a csv file

import csv, os

# use open function to read the csv file and create 
# a file object f:

with open('data/stocks_short.csv') as f: 

    # use the reader class under the csv module to 
    # read the file using commas as the delimeter

    csv_file = csv.reader(f, delimiter=',')
    row = f.readline() # read the first line of the .csv
    print(row)
    row = f.readline() # read the firstline of the .csv
    print(row)

# 19.2 Iterating through a csv file
with open('data/stocks_short.csv') as f:

    csv_file = csv.reader(f,delimiter=',')
    f.readline()

    # csv_file is an iterable object that we can iterate on using a for loop
    for row in csv_file:
        print(row) # print entire row

# 19.3 iterating through a csv file and printing individual items
with open('data/stocks_short.csv') as f:
    csv_file = csv.reader(f, delimiter = ',')

    for row in csv_file:
        print(row[0],  " - ", row[1])

# 19.4 Calculating the average opening price
with open('data/stocks_short.csv') as f:

    csv_file = csv.reader(f, delimiter = ',')
    f.readline()

    sum = 0
    count = 0

    for row in csv_file:
        sum += float(row[1])
        count += 1
    print(sum/count)

# 19.5 
with open ('data/stocks_short.csv') as f:

    csv_file = csv.DictReader(f, delimiter = ',')

    # csv_file is an iterable object that we can iterate on using a for loop 
    for row in csv_file:
        print(row)

# 19.6
with open('data/stocks.csv') as f:
    
    csv_file = csv.DictReader(f,delimiter=',')
    vol = None
    max_vol = None

    for row in csv_file:
        vol = int(row['Volume'])
        if max_vol == None or max_vol < vol:
            max_vol = vol
        print(max_vol)

# 19.7 creating a list from our dataset
def read_csv1(filepath, delimiter = ','):
    dataset = list()
    with open(filepath) as f:

        # use the DictReader function of the sv module to 
        # read the file using the same delimiter
        csv_file = csv.DictReader(f,delimiter = delimiter)

        # csv_file is an iterable objet, that we an iterate on using a for loop
        for row in csv_file:
            dataset.append(row)

    return dataset

dataset = read_csv1("data/stocks_short.csv")
print(len(dataset)) # number of rows in the dataset
print("-" * 20)
print(dataset[0]) # print first row in the dataset
print("-" * 20)
print(dataset)

# 19.8 using our list from reading a csv file to calculate the closing price
def read_csv(filepath, delimiter = ','):
    dataset = list()
    with open(filepath) as f:
        csv_file = csv.DictReader(f,delimiter = ',')
        for row in csv_file:
            dataset.append(row)
    return dataset

dataset = read_csv("data/stoks.csv")
total = 0
for row in dataset:
    total += float(row["Close"])
    print("Close: " + str([row["Close"]]))
    print("-" * 10)
    print(total)

# 19.9 using writerow
row_1 = ['employee_id', 'first_name', 'last_name'] # header row
row_2 = ['EMP2423424234','robert','balti'] # first row
row_3 = ['EMP446P234323','mark','smith'] # second row
row_4 = ['EMP4996392949','mary','caldwell'] # third row

with open('data/employee.csv','w') as csv_file: # open file in write mode
    # use the writer class to create a writer objet
    # that we will use to write data into the file
    writer = csv.writer(csv_file, delimiter = ",")
    writer.writerow(row_1) # writing the header row
    writer.writerow(row_2) # writing the first row 
    writer.writerow(row_3) # writing the second row
    writer.writerow(row_4) # writing the thire row

# 19.10 prompting the user for data for a csv file
with open('user_input.csv','w', newline = '') as csv_file:

    while True:
        user_input = input("Please enter text to add to file [enter quit to exit]: ")
        if user_input.lower() == 'quit':
            break
        else:
            writer = csv.writer(csv_file,delimiter = ',')
            writer.writerow([user_input])

f = open('user_input.csv', 'r')
print(f.read())
f.close()

# 19.11 appending data to a csv file
row_1 = ["EMP9090890890", "rodney","evans"] # first row
row_2 = ["EMP9949329193","lesa","clapper"] # second row
row_3 = ["EMP9994949903","mario","cruz"] # third row

# open file in append mode, which will add the data at theh end of the file
with open('data/employee.csv','a') as csv_file:
    # use the writer class to reate a writer objet
    # that we will use to write data into the file
    writer = csv.writer(csv_file, delimiter = ",")
    writer.writerow(row_1) # writing the first row
    writer.writerow(row_2) # writing the second row
    writer.writerow(row_3) # writing the third row 

f = open('data/employee.csv', 'r')
print(f.read())
f.close()

# 19.12 append or overwrite
while True:
    if os.path.exists('data/user_input.csv'):
        user_prompt = input("The file exists, what data would you like to append? [type quit to exit]: ")
        if user_prompt.lower() == 'quit':
           break
        else:
            with open('data/user_input.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter = ',')
                writer.writerow([user_prompt]) # writing the first row
        
f = open('data/user_input.csv', 'w')
print(f.read())
f.close()

# 19.13 writing multiple rows to a file at once
dataset = [["EMP4239U09208","vicki","gallegos"],["EMP20389098345","hector","bowen"]]

# open file in append mode, which will add the data at the end of the file
with open('data/employee.csv', 'a') as csv_file:
    # use the writer class to create a writer object
    # that we will use to write data into the file
    writer = csv.writer(csv_file,delimiter = ',')
    # write multiple rows at once using writerows
    writer.writerows(dataset)

f = open('data/employee.csv', 'r')
print(f.read())
f.close()

# 19.14 adding dictionary objects to a csv file

# create three rows of data; item order is not important because each dictionary
# uses keys to identify eah value
row_1 = {"employee_id":"EMP29003403","first_name":"rodney","last_name":"evans"}
row_2 = {"employee_id":"EMP23098320","first_name":"lesa","last_name":"clapper"}
row_3 = {"employee_id":"EMP20832094","first_name":"mario","last_name":"cruz"}

fieldnames = ["employee_id","first_name","last_name"]

with open('data/employee.csv','w') as csv_file:
    writer = csv.DictWriter(csv_file,delimiter=',',fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow(row_1) # write the first row
    writer.writerow(row_2) # write the second row
    writer.writerow(row_3) # write the third row

f = open('data/employee.csv','r')
print(f.read())
f.close()

# 19.15 adding transactions via dictionaries
count = 0
filename = 'data/transactions.csv'
dataset = {}

trans_date = input("Please enter the transaction date: ")
customer = input("Enter the customer: ")
merchant = input("Enter the merchant name: ")
total = input("Enter the total of the transaction: ")

input_data = {"trans_date":trans_date,"customer":customer,"merchant":merchant,"total":total}
print(input_data)

fieldnames = ["trans_date","customer","merchant","total"]

# Open file in append mode, which will add the data at the 
# end of the file
if os.path.exists(filename):
    with open(filename,'a') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writerow(input_data)

# Print out the data in the file:
f = open('data/transactions.csv','r')
print(f.read())
f.close()