# define a function to filter out vowels
def is_vowel(letter):
    vowels = ['a','e','i','o','u']
    return letter in vowels

# sequence to be filtered
sequence = ['g','e','e','j','k','s']

# using the filter function
filtered = filter(is_vowel, sequence)

# convert to list and print
print(list(filtered)) # >>>> ['e','e']

# Example with lambda
# list of numbers
numbers = [1,2,3,4,5,6,7,8,9]

# filter even numbers using a lambda function
even_numbers = filter(lambda x: x % 2 == 0, numbers)
