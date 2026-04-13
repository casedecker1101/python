# Takes unknown number of text files and merges them

# class definitions

class FileMerger:
    def __init__(self,*filepaths,mode="r",encoding="utf-8"):
        self.filepaths = filepaths
        self.mode = mode
        self.encoding = encoding

    def main(self):
        while cinMain != 'quit':
            filepaths_input = input("Enter filepaths, separate with commas: ")
            filepaths = [path.strip() for path in filepaths_input.split(",") if path.strip()]

    def viewFile(self):
        for filepath in self.filepaths:
            with open(filepath,self.mode,encoding=self.encoding) as file:
                print(file.read())

    def mergeFiles(self,output = "data/compressed.txt"):
        with open(output, "w", encoding = self.encoding) as outfile:
            for filepath in self.filepaths:
                with open(filepath,"r", encoding=self.encoding) as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
    
    def mergeFilesInput(self,output = input("Enter output path: ")):
        with open(output, "w", encoding=self.encoding) as outfile:
            for filepath in self.filepaths:
                with open(filepath,"r", encoding=self.encoding) as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")          
        
    def mergeDirectory(self):
        pass

# variables
cinMain = ""
mode = "r"
encoding = "utf-8"
while cinMain != 'quit':
    filepaths_input = input("Enter filepaths, separate with commas: ")
    filepaths = [path.strip() for path in filepaths_input.split(",") if path.strip()]
    cinMain = input("Type 'quit' to exit or press Enter to continue: ").strip().lower()
