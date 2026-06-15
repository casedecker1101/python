with open("data/emotions.txt", "r") as readFile:
    newFile = readFile.readline() 
    lines = ""
    for x in range(newFile):
        lines += readFile.readline()
    print(len(readFile.read()))