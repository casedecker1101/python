# 1 - 2
from functools import reduce
import random
numbers = []

def randomInput():
    numbers = [random.randint(1, 100) for i in range(10)]
    try:
        fragOut = reduce(lambda x, y : x % y, numbers) / int(input("Enter a number: "))
        fragOut.append(numbers)
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ValueError:
        print("Enter a valid number.")

randomInput()
    
# 3
def fileSearch():
    try:
        with open("data.txt") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No dice, file not found.")

fileSearch()

# 4
def guessNumber():
    number = random.randint(1, 100)
    try:
        guess = int(input("Whats the number? "))
        if guess == number:
            print("Correct!")
        else:
            print(f"Wrong! The number was {number}.")
    except ValueError:
        print("Enter a valid number.")

guessNumber()

# 5
def safeInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number.")

safeInput("Enter a number: ")