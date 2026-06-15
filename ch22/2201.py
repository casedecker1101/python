while True:
    try:
        x = input("Enter a number: ")
        try:
            x = int(x)
        except ValueError:
            try:
                x = float(x)
            except ValueError:
                try:
                    x = complex(x)
                except ValueError:
                    raise ValueError("The value entered is not a number.")
        print(type(x))
        print(x)            
    except ValueError as e:
        print(format(e))