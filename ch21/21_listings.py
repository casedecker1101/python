# 1. using a lambda function
x = lambda a : a + 10
print(x(5))

# 2 creating a lambda for power
x = lambda a : a ** 2
print(x(10))

# 3 using multiple inputs with a lambda function
x = lambda a, b : a * b
print(x(5, 6))

# 4 order of parameters matters
x = lambda a, b : a / b
print(x(6, 5))
print(x(5, 6))
# 5 items per person
PerPerson = lambda items, people : items /people
print(PerPerson(20,5))  # correct
print(PerPerson(5,20)) # incorrect

# 6 lambda to concatenate strings
x = lambda a, b, c: a + " " + b + " " + c
print(x("This", "is" , "lambda concatenation"))

# 7 using a lambda inside another function
def myfunc(n):
    return lambda a : a * n

doubler = myfunc(2) # we set the value of n
print(doubler(11)) # we set the value of a

# 8 creating a lambda function within a function
def pow_n(n):
    return lambda a: a ** n

pow_2 = pow_n(2) # we set the value of n
print(pow_2(6)) # we set the value of a

# 9 converting a character to uppercase 
def to_upper_case(s):
    return str(s).upper()

names = ['haythem', 'mike','james']
print(names)

names_upper = map(to_upper_case, names) # apply to_upper_case function to each element in names
print(type(names_upper))
names_upper_list = list(names_upper) # convert the names_upper map object to a python list
print(names_upper_list)
print(type(names_upper_list))

# 10 using map on a CSV file
def fromCSV(path, delimiter, quotechar):
    import csv # import the csv module
    data = list() # convert the csv into a list
    with open(path, newline='') as csvfile: # open the file
        filecontent = csv.DictReader(csvfile, delimiter = delimiter, quotechar = quotechar) # read the file content as a dictionary
        for row in filecontent: # iterate through the rows of the file content
            data.append(row) # append each row to the data list

    return data

def extract_month(row):
    # input is the entire row of data
    # extract the month from the date field
    # add the month field to the row and return the row
    value = row['Date'] # extract the date field from the row
    MM = ""
    # split function in python used to divide strings based on some delimiter
    a = value.split("/")
    MM = a[0] # the month is the first element of the split result
    # implement logic here
    new_row = row.copy()
    new_row.update({'Month':MM}) # add the month field to the row
    return new_row

data = fromCSV(path = 'JobReadyPython\data\stocks.csv', delimiter = ',', quotechar = '"')
print(data[0]) # print the first row of the data to see the structure of the data

data_mapped = map(extract_month, data) # apply the extract_month function to each row of the data
data_mapped_list = list(data_mapped) # convert the data mapped object to a list
print(data_mapped_list[0]) # print the first row of the mapped data to see the new structure of the data

# 11 using lambdas and map together
list_numbers = [1, 2, 3, 4, 5]
tuple_numbers =(5, 6, 7, 8, 9)
print(list_numbers)
print(tuple_numbers)
map_iterator = map(lambda x, y: x + y, list_numbers, tuple_numbers) # add the elements of the two lists together using a lambda function
map_list = list(map_iterator) # convert the map object to a list
print(map_list) # print the result of the map function

# 12 summing exchange rate and transaction amounts
exchange_rate = [1.25, 2, 1.3, 1.18]
transaction_amt = (5,6,7,8)
print(exchange_rate)
print(transaction_amt)

map_iterator = map(lambda x, y: x + y, exchange_rate, transaction_amt) # add the elements of the two lists 

map_list = list(map_iterator) # convert map object to list
print(map_list) # print the result of the map function

# 13 using filter
def initial_h(dataset):
    for x in dataset:
        if str.lower(x[0]) == "h": # normalize the case of the first letter and look for the letter h
            return True
        else:
            return False
names = ['haythem', 'mike', 'james', 'hannah']
print(names)
# extract the True results from the initial_h function to a new filter object
names_filtered = filter(initial_h, names)
print(type(names_filtered)) # print the type of the filter object
# convert the filter object to a list and print the result
names_filtered_list = list(names_filtered) # convert the filter object to a list
print(names_filtered_list) # print the result of the filter function

print(names_filtered_list)

#14 filtering for names containing the letter e
def contains_e(dataset):
    if 'e' in dataset:
        return True
    else:
        return False
names_filtered = filter(contains_e, names) # apply the contains_e function to each element in the names list
print(type(names_filtered)) # print the type of the filter object
names_filtered_list = list(names_filtered) # convert the filter object to a list
print(names_filtered_list) # print the result of the filter function

print("15")
# 15 using a filter and lambda on our stocks.csv data
def fromCSV2(path, delimiter, quotechar):
    import csv # import the csv module 
    data = list() # any data we will read will be returned in a list
    with open(path, newline='') as csvfile: # open the file
        filecontent = csv.DictReader(csvfile, delimiter = delimiter, quotechar = quotechar) # read the file content as a dictionary
        for row in filecontent: # iterate through the rows of the file content
            data.append(row) # append each row to the data list
        return data
data = fromCSV2(path = 'JobReadyPython\data\stocks.csv', delimiter = ',', quotechar = '"') # read the data from the csv file)
# filter all emements in the data where the open price is lower than the close price
data_filtered = filter(lambda x: x['Open'] < x['Close'], data)
print(type(data_filtered)) # print the type of the filter object

data_filtered_list = list(data_filtered) # convert the filter object to a list
for row in data_filtered_list: # display each element in the filtered list
    print(row)

# 16 multiplying numbers together
print("16")
from functools import reduce # import the reduce function from the functools module
list_numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, list_numbers) # multiply the elements of the list together using a lambda function and the reduce function
print(type(product)) 
print(product)

# 17 using a reduce and a lambda to calculate a sum
from functools import reduce

value_list = []

while True:
    user_input = input("Enter the deposits to add to the series to sum [ type quit to exit]: ")
    if user_input.lower() == 'quit':
        break
    else:
        value_list.append(int(user_input))
    
product = reduce(lambda x, y: x + y, value_list) # sum the elements of the list together using a lambda function and the reduce function
print(type(product))
print(product)

# 18 starting with an initial value in reduce
from functools import reduce
list_numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, list_numbers, 10) # multiply the elements of the list together using a reduce/lambda combination
print(type(product))
print(product)

# 19 summing the total account balance
from functools import reduce

value_list = []
prev_bal = int(input("Enter your previous balance: "))
while True:
    user_input = input("Enter the deposits to add to the series to sum [ type quit to exit]: ")
    if user_input.lower() == 'quit':
        break
    else: 
        value_list.append(int(user_input))
product = reduce(lambda x, y: x + y, value_list, prev_bal) # sum the elements of the list together using a reduce/lambda combination
print(type(product))
print(product)

# 20 finding the highest value in a colletion of values
from functools import reduce
list_numbers = [1, 2, 3, 4, 5]
max_element = reduce(lambda a,b : a if a > b else b, list_numbers) # find the maximum element in the list using a reduce/lambda combination
print(type(max_element))
print(max_element)

# 21 finding the lowest value
from functools import reduce
value_list = []

while True:
    user_input = input("Enter the deposits to determine the lowest deposit [type stop to exit]: ")
    if user_input.lower() == 'stop':
        break
    else:
        value_list.append(int(user_input))
    
if len(value_list) > 0:
    product = reduce(lambda x, y: x if y > x else y, value_list) # find the minimum element in the list using a reduce/lambda combination
else:
    product = "Nothing."

print("The values you entered were: " + str(value_list))
print("The lowest value is: " + str(product))