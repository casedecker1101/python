# 18.1 siimple file I/O script
f = open("myfile.txt", "r")
print(f.readling())
f.close()

# 18.2 opening the flatland01.txt file
# Open our file in read mode
f = open("data/flatland01.txt", mode = "r")

# Read and display text file
print(f.read())

# Close our file resource
f.close()

# 18.3 reading the contents of a text file
f = open("data/flatland01.txt", mode = "r")
text = f.read()
print(text)
f.close()

# 18.4 limiting the amount read 
f - open("data/flatland01.txt", "r")
print(f.read(100)) # this will pull pull the first 100 characters
f.close()

# 18.5 creating a function to read characters from a file
def head(filepath, num_char):
    f = open(filepath, mode = "r")
    output = f.read(num_char)
    f.close()
    return output

# return the first 20 characters in the file data/text.txt
text = head("IncidentTicket.txt", 20)
print(text)

# 18.6 IncidentTicket.txt

# 18.7 reading lines of a text file
f = open("IncidentTicket.txt", "r") # read file in read mode
print(f.readline()) # read first line
print(f.readline()) # read second line
print(f.readline()) # read third line
print(f.readline()) # read fourth line

f.close()

# 18.8 creating a function to read lines of a file
def head(filepath,num_lines):
    f = open(filepath, mode = "r")
    lines = ""
    for x in range(num_lines):
        lines += f.readline()
    f.close()
    return lines

# return the first 3 lines in the file
text = head("IncidentTicket.txt", 3)
print(text)

# 18.9 iterating through a file
f = open("IncidentTicket.txt", "r")

for line in f:  # the file object can be iterated on at the line level. 
    print(line) # with each iteration, line contains the current line.

f.close()

# 18.10 iterating and checking the start of the line
def line_starts_with(file_path, fchar):
    f = open(file_path, mode = "r")
    output = ""
    for line in f:
        if fchar == line[0]:
            output += line
        return output

# return all lines in the file data/text.txt that start with "I"
text = line_starts_with("IncidentTicket.txt", "I")
print(text)

# 18.11 writing to a file
f = open("data/test_file.txt", "a")

f.write("Hello World!")
f.write("Hello World!")
f.write("Hello World!")

f.close()

# 18.12 writing transaction data to a file
import datetime

f = open("ReportFile.txt","a")

f.write("Acme Bank EBP")
f.write("\nDate: " + str(datetime.date.today()))
f.write("\nReport File 0001")

f.close()

# 18.13 writing a list to a file
customers = ["Ax Lodevick", "Frank Prys", "Ania Hearle"]

def write_list_2_file(input_list, input_file_path):
    f = open(input_file_path "a")
    for name in input_list:
        name = "\n" + name
        f.write(name)
    f.close()

write_list_2_file(customers,"Customers.txt")

# 18.14 overwriting a file
f = open("data/test_file.txt", "w")
f.write("This will overwrite whatever existed in the file.")
f.close() 

# 18.15 prompting the user for a file to overwrite
input_1 = input("Please enter a fie name: ")
input_2 = input("Enter the text you would like within the file: ")

f = open(input_1, mode = "w")
f.write(input_2)
f.close()

# 18.16 creating a new file

# this file should not exist ...
f = open("data/another_file.txt", "x")
f.close()

# we created this file earlier ... 
f = open("data/test_file.txt", "x")
f.close()

# 18.17 prompting the user to create a file
input_1 = input("Please enter a file name: ")
input_2 = input("Enter the the text you would like owitin the file: ")
input_3 = input("Enter the read/write mode for the file [a,x,r,w]: ")

f = open(input_1, input_3)
f.write(input_2)
f.close()

# 18.18 checking for a file's existence
import os
if os.path.exists(("data/missing_file.txt")):
    print("The file exiists.")
else:
    print("The file doesn't exist." )

# 18.19 checking for the entered file's existence
import os
file_name = input("Please enter a file name to check for: ")
if os.path.exists("data/" + file_name):
    print("The file exists.")
else:
    print("The file doesn't exist.")

# 18.20 deleting a file
import os 
os.remove("data/test_file.txt") # deleting file from previous example
print("The file test_file.txt deleted successfully.")

# The following file doesn't exist, so will cause error:
os.remove("data/missing_file.txt")
print("The file missing_file.txt deleted successfully.")

# 18.21 prompting to remove a file
import os

file_name = input("Please enter a file name to check for: ")
directory = "data/"
if os.path.exists(directory + file_name):
    print("The file exists.")
    user_input = input("Would you like to delete the file? [yes/no]")
    if user_input.lower() == 'yes':
        os.remove(directory + file_name)
        print("The file " + directory + file_name + " was deleted successfully.")
    else:
        print("The file doesn't exist.")

