from functools import reduce

numbers = ()

highest_number = reduce(lambda a, b: a if a > b else b, numbers) # find the highest number in the tuple using a reduce/lambda combination
print(type(highest_number))
print(highest_number)