def sum(a, b):
    return a + b
def difference(a, b):
    return a - b
def product(a, b):
    return a * b
def quotient(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero."
    
while True:
    print("Select Operation:")
    print("1. Sum")
    print("2. Difference")
    print("3. Product")
    print("4. Quotient")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            try:
                print(f"The sum of {num1} and {num2} is: {sum(num1, num2)}")
            except (OverflowError, ValueError) as e:
                print(f"Error: {e}")
                print("Please enter a smaller value for the sum operation.")
        elif choice == '2':
            try:
                print(f"The difference of {num1} and {num2} is: {difference(num1, num2)}")
            except (OverflowError, ValueError) as e:
                print(f"Error: {e}")
                print("Please enter a smaller value for the difference operation.")
        elif choice == '3':
            try:
                print(f"The product of {num1} and {num2} is: {product(num1, num2)}")
            except (OverflowError, ValueError) as e:
                print(f"Error: {e}")
                print("Error: The product is too large to handle. Please enter a smaller value for the product operation.")
        elif choice == '4':
            try:
                print(f"The quotient of {num1} and {num2} is: {quotient(num1, num2)}")
            except (ValueError, ZeroDivisionError) as e:
                print(f"Error: {e}")
                print("Please enter a valid number for the quotient operation.")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")