# Reads file line by line into list
# Read line into list

#variable
cinMain = ""
storage = []
# classes
class Fileviewer:
    def __init__(self,filepaths,viewer):
        self.filepaths = filepaths
        self.viewer = viewer

    def viewer(self):
       # read input from text file to variable
        with open("merged.txt","r",encoding="utf-8") as outfile:
            list.append(outfile.read())
            print(list)
# intro loop
while cinMain != 'quit':
    cinMain = input("Enter the file path or quit to exit the program: ")
    if cinMain == 'quit':
        exit()