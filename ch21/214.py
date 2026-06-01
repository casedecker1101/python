import math

numbers = []
customerInput = input("Enter a list of numbers separated by a space: ")
numbers.append(customerInput.split())
numbers = numbers[0] # conver the list of lists into a single list
numbers = list(map(lambda x: abs(int(x)), numbers)) # convert the list of strings into a list of integers using a lambda funcion and the map function, also take the absolute value of each number
print(numbers)