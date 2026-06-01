from functools import reduce 

dict_my = {"elephant": 1, "turtle": 2, "dog": 3}

# Compare key names (index 0) and keep the tuple with the alphabetically last key.
last_alphabet = reduce(lambda a, b: a if a[0] > b[0] else b, dict_my.items())
print(type(last_alphabet))
print(last_alphabet)