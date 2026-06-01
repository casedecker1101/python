from functools import reduce

def positive(list_numbers):
    positive_filter = filter(lambda x: x > 0, list_numbers)
    positive = reduce(lambda x, y: x + y, positive_filter) # sum the positive numbers in the list together using a reduce/lambda combination
    return positive

list_numbers = [1, -2, 3, -4, 5]
print(positive(list_numbers))