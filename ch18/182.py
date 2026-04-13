# combination of the two
# Takes two text files as input
# Concatenatenates the files into a single new file

class FileMod:
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2

    def merge(self):
        with open(self.file1, mode="r", encoding="utf-8") as f1:
            with open(self.file2, mode="r", encoding="utf-8") as f2:
                with open("merged.txt", mode="w", encoding="utf-8") as merged:
                    merged.write(f1.read() + f2.read())
                return "Files merged successfully into merged.txt"

cinMenu = ""
while cinMenu != 'quit':
    file1 = input("Enter first file to merge: ")
    file2 = input("Enter second file to merge: ")

    merge = FileMod(file1, file2)

    try:
        print(merge.merge())
    except FileNotFoundError:
        print("One or both files were not found. Check the paths and try again.")
    except OSError as err:
        print(f"Could not read file(s): {err}")

    cinMenu = input("Type 'quit' to exit or press Enter to continue: ")
