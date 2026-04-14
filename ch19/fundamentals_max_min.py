# learning the fundamentals because we are waaaay behind
# finding max numbers in a list without using built-in functions

def find_max(numbers):
    if not numbers:
        return None # handle empty list case
    max_value = numbers[0] # start with first element
    for num in numbers[1:]: # loop from the second element to the end
        if num > max_value:
            max_value = num # update max if we find a bigger number
    return max_value

# Example usage
nums = [3,1,4,1,5,9,2,6,5,3,5]
print(find_max(nums)) # output should be 9

# finding min numbers in a list without using built-in functions
def find_min(numbers):
    if not numbers:
        return None # handle empty list case
    min_value = numbers[0] # start with first element
    for num in numbers[1:]: # loop from the second element to the end
        if num < min_value:
            min_value = num # update min if we find a smaller number
    return min_value

# example usage
nums = [3,1,4,1,5,9,2,6,5,3,5]
print(find_min(nums)) # output should be 1
print(find_max(nums)) # output should be 9

# finding max and min in a single pass
def find_min_max(numbers):
    if not numbers:
        return None, None # handle empty list case
    min_value = max_value = numbers[0] # start with first element
    for num in numbers[1:]: # loop from the second element to the end
        if num < min_value:
            min_value = num # update min if we find a smaller number
        elif num > max_value:
            max_value = num # update max if we find a bigger number
    return min_value, max_value

# example usage
nums = [3,1,4,1,5,9,2,6,5,3,5]
min_val, max_val = find_min_max(nums)
print(f"Min: {min_val}, Max: {max_val}") # output should be Min: 1, Max: 9