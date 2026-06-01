# map/lambda combination determine prime number from input
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

user_input = int(input("Enter a number to determine if it is prime: "))
result = map(lambda x: is_prime(x), [user_input]) # use a map/lambda combination to determine if the input number is prime
print(list(result))