# function prompts user for integer n 
# reads first n lines of a file
# creative way to handle n greater than the number of lines
# add exceptions - user enters something other than an integer n
# add exceptions - file not found

def readFile():
    filepath = input("Please enter filepath: ")
    try:
        with open(filepath, 'r') as readFile:
    except FileNotFoundError:
            print("File not found, please try again.")
            filepath = input("Please enter filepath: ")
            with open(filepath, 'r') as readFile:
            lines = ""
            nValue = int(input("Please enter lines to read: "))
            if nValue < 0:
                raise ValueError("Negative value entered.")
            if len(readFile.readlines()) < nValue:
                print("File has fewer lines than requested. Reading entire file.")
            elif nValue != int(nValue):
                raise ValueError("Value not an integer.")
            for x in range(nValue):
                lines += readFile.readline()
            print(lines, end="")
readFile()