# 211: Map Function to Compute Square Roots
# Compute square roots for a list of integers without importing math.
def compute_square_roots(numbers):
    return list(map(lambda value: value ** 0.5, numbers))


input_numbers = list(map(int, input("Enter a set of integers separated by spaces: ").split()))
print(compute_square_roots(input_numbers))


# Alternate lambda pattern for powers from the incoming branch.
def nthPower(_, n):
    return lambda value: value ** n


n = int(input("Enter the power value: "))
x = int(input("Enter the value to compute the nth power of: "))
power_fn = nthPower(x, n)
print(power_fn(x))

