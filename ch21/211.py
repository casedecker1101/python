# 211: Map Function to Compute Square Roots
# Computing square root 
# create a script that uses the map() function to compute the square root of each value in an input set of integers.
# do not use import math or any other library to compute the square root, instead use the exponentiation operator ** to compute the square root.
def compute_square_roots(numbers):
    return list(map(lambda x: x ** 0.5, numbers))
input_numbers = list(map(int, input("Enter a set of integers separated by spaces: ").split()))
print(compute_square_roots(input_numbers))

# 212: Converting a text file to upercase
# create a script that reads a text file and converts its content to uppercase.
def convert_file_to_uppercase(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    with open(file_path, 'w') as file:
        file.write(content.upper())
file_path = input("Enter the path to the text file: ")
convert_file_to_uppercase(file_path)

