# Write function that takes as input path of two text files
# Concatenates both into one file
# Exception for both files

def twoFiles(filepath1,filepath2): 
    with open(filepath1, 'r') as f1, open(filepath2,'r') as f2:
        file1 = f1.read()
        file2 = f2.read()

    with open('data/file3.txt','a') as f3:
        f3.write(file1 + "\n" + file2)
        print(f"{file1} + {file2}")

twoFiles("data/flatland01.txt","data/IncidentTicket.txt")