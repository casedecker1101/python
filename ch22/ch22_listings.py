# 3 handling zero division error
a = 1
b = 0
try: # check that the operation is valid
    x = a / b
except ZeroDivisionError as e: # handle the error
    # print custom message to the user
    print("Division by zero error: zero cannot be used.")
    print(format(e)) # print the error message 

# 4 handling FileNotFoundError
try:
   file_object = open("data/bank_transacts.txt", 'r')
except FileNotFoundError as e:
    print("The file was not found.")
    print("The error was: " + str(format(e)))

# 5 handling multiple exceptions
import sys
a = 1
b = 'c'

try:
    x = a / b # this will raise a TypeError
except ZeroDivisionError as e:
    print("Error: division by zero.")
    print(format(e))
except TypeError as t:
    print("Error: incompatible types.")
    print(format(t))
except:
    print("Unexpected error. Try again." , sys.exc_info()[0])
    raise

# 6 validating user input
value_1 = input("Please enter a number: ")
value_2 = input("Please enter a second number: ")
try:
    x = int(value_1) / int(value_2)
    print(x)
except ValueError:
    try:
        x = float(value_1) / float(value_2)
        print(x)
    except ValueError:
        print("The first value is not an integer or a float.")
    try:
        x = float(value_2)
    except:
        print("The second value entered is not an integer or a float.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 7 combining exceptions
a = 1
b = 'c'
try:
    x = (a / int(b)) 
except (ZeroDivisionError, TypeError) as e:
    print(format(e))

# 8 checking a list for valid values
def check_numbers(input_list):    
    list = []
    for x in input_list:
        try:
            a = float(x)
            list.append(x)
        except ValueError:
            try:
                a = int(x)
                list.append(x)
            except (ValueError, ZeroDivisionError, TypeError) as e:
                print(x + " is not a a valid number.")
        except(ZeroDivisionError, TypeError) as e:
            print(x + " is not a valid number.")
    return list

input_list = ['1', '2', '3', 'a', '4.5', 'b']
print(check_numbers(input_list))

# check_numbers should return a list that contains the valid numbers.
numbers = check_numbers(input_list)
print(numbers)

# 9 multipel try statements

import sys
b = 0
a = 1
c = 'd'

try:
    # triggers default exception
    y = (a & b) 

    # this will throw an exception, which will trigger an except statement
    y = (a / int(c))

    # This would also throw an exception, but python ignores it because it is the second exception
    x = (a / b)
except ZeroDivisionError as e:
    print("Oops, ZeroDivisionError: " + format(e))

except TypeError as t:
    print("Oops, TypeError: " + format(t))

except:
    print("Unexpected error: " + str(sys.exc_info()[0]))
    raise

# 10 creating raise exceptions
print("Starting the program...")
try:
    raise ValueError("This is a custom ValueError.")
    raise TypeError("This is a raised TypeError.")
    raise Exception("This is a raised generic exception.")
    raise ZeroDivisionError("I raised This ZeroDivisionError.")
    raise RuntimeError("This is a raised RuntimeError.")
except ValueError as e:
    print("Caught an exception: " + format(e))
except TypeError as t:
    print("Caught an exception: " + format(t))
except ZeroDivisionError as ze:
    print("Caught an exception: " + format(ze))
except RuntimeError as re:
    print("Caught an exception: " + format(re))
except Exception as ex:
    print("Caught an exception: " + format(ex))

# 11 usint the general IOError exception
try:
    f = open("data/another_file_that_does_not_exist.txt", 'r')
    print(f.read())
    f.close()
except IOError as e:
    print("An IOError occurred: " + format(e))
    print("The file could not be opened or read.")
    raise

# 12 trying to import a nonexistent package
try:
    import wrong_package
except ImportError as e:
    print("An ImportError occurred: " + format(e))
    print("Module not found. Please check the name and try again.")

# 13 adding exception handling to opening a file
def read_csv(filepath, delimiter = ","):
    import csv
    dataset = list()
    try:
        with open(filepath) as f: # use open to read the file
            # use the csv reader to read the file
            f = csv.reader(f, delimiter = delimiter)

            # csv_file is an iterable object that we can iterate on using a for loop
            for row in f:
                dataset.append(row) # add each row to the dataset list
        return dataset
    except IOError as e:
        print("Unable to access file.")

a = read_csv("data/bank_transacts.txt")
print(a)

# 14 using the finally statement
try:
    f = open("data/text.txt", 'r')
    # file does not exist so this line throws a FileNotFoundError, which is a subclass of IOError
    print(len(f.read())) # this line will not execute because the exception is thrown on the previous line

# This except statement runs only if Python does not find the file
except IOError as e:
    print("An IOError occurred: " + format(e))
    print("The file could not be opened or read.")

# This finally statement runs whether or not Python finds the file
finally:
    print("Thanks for trying!")