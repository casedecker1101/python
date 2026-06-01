from functools import reduce

dict_my = {"elephant": 1, "turtle": 2, "dog": 3}

highest_value = reduce(lambda x, y: x if x[1] > y[1] else y, dict_my.items())
print(type(highest_value))
print(highest_value)
