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

data = fromCSV(path = 'data/stocks.csv', delimiter = ',', quotechar = '"')
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