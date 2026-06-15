# Finding the number of lines in a file
def readFile():
    filepath = input("Please enter the file path: ")
    with open(filepath, "r") as file:
        lines = ""
        for line in file:
            lines += line
        print(len(lines.splitlines()))
        return lines

readFile()
