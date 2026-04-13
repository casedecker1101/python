list = []
# Read input to variable
cin = input("Input to variable: ")
list.append(cin)

# read input from text file to variable
with open("merged.txt","r",encoding="utf-8") as outfile:
    list.append(outfile.read())
    print(list)