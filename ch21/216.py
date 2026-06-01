from functools import reduce

numbers = ()

cinNumbers = input("Enter a series of numbers to find lowest value [type stop to exit]: ")

lowest_value = reduce(lambda a,b : a if a < b else b, cinNumbers.split()) # find the lowest value in the list of numbers using a reduce/lambda combination
print(type(lowest_value))
print(lowest_value)