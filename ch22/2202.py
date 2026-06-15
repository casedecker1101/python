while True:
    try:
        p = float(input("Enter initial deposit: "))
        r = float(input("Enter the interest rate: "))
        n = float(input("Enter times per year interest is calculated: "))
        t = float(input("Enter the number of years since the initial deposit: "))
        print(f"Initial Deposit: {p} - Interest Rate: {r} - Per Annum Calculation: {n} - Time Since Initial Deposit: {t}")
        current_deposit = ((p* (1 + r/n))**(n*t))
        print(f"Value of Current Deposit {current_deposit}")
        break
    except ValueError:
        print("Invalid input. Please try a decimal or integer.")