from functools import reduce 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_numbers(numbers):
    even_filter = filter(lambda x: x % 2 == 0, numbers) # filter the list of numbers to only include even numbers using a lambda function and the filter function
    even = reduce(lambda a, b : a + b, even_filter)
    print(type(even))
    print(even)


even_numbers(numbers)