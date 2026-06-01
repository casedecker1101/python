# Computing the square root
def nthPower(x, n):
    return lambda x: x ** n
n = int(input("Enter the power value: "))
x = int(input("Enter the value to compute the nth power of: "))
square = nthPower(x, n) # set the n value to 2 to compute the square
print(square(x)) # compute the nth power of x using the lambda function returned by nthPower

