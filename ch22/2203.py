# function prompts user for integer n 
# reads first n lines of a file
# creative way to handle n greater than the number of lines
# add exceptions - user enters something other than an integer n
# add exceptions - file not found

def readFile():
    while True:
        filepath = input("Please enter filepath: ")

        try:
            with open(filepath, 'r') as file_obj:
                file_lines = file_obj.readlines()
        except FileNotFoundError:
            print("File not found, please try again.")
            continue

        while True:
            try:
                nValue = int(input("Please enter lines to read: "))
            except ValueError:
                print("Value not an integer.")
                continue

            if nValue < 0:
                print("Negative value entered.")
                continue

            break
# If the requested number of lines is greater, error with a message, read the file and state the number of lines in the file.

        if nValue > len(file_lines):
            print(f"File has fewer lines than requested. Reading entire file. The file has {len(file_lines)} lines.")
            nValue = len(file_lines)

        print("".join(file_lines[:nValue]), end="")
        break
readFile()