# examples
try:
    number = int("hellO")
except ValueError:
    print("That wasn't a number!")

# Real world example
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number.")

# Multiple exceptions 
try:
    result = 10 / int(input("Enter a number: "))
except ValueError:
    print("You must enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Optional finally block
try:
    file = open("data.txt")
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("This block is executed no matter what.")

# Optional else block
try: 
    x = int(input("Number: "))
except ValueError:
    print("Invalid number.")
else:
    print(f"You entered the number {x}.")


