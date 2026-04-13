# Takes unknown number of text files and merges them

# class definitions

class FileMerger:
    def __init__(self,*filepaths,mode="r",encoding="utf-8"):
        self.filepaths = filepaths
        self.mode = mode
        self.encoding = encoding

    def viewFile(self):
        for filepath in self.filepaths:
            with open(filepath,mode = self.mode ,encoding=self.encoding) as file:
                print(file.read())

    def mergeFiles(self,output = "data/compressed.txt"):
        with open(output, "w", encoding = self.encoding) as outfile:
            for filepath in self.filepaths:
                with open(filepath,"r", encoding=self.encoding) as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
    
    def mergeFilesInput(self, output=None):
        if output is None:
            output = input("Enter output path: ")
        with open(output, "w", encoding=self.encoding) as outfile:
            for filepath in self.filepaths:
                with open(filepath,"r", encoding=self.encoding) as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")          
        
    def mergeDirectory(self):
        pass

filepaths = []
fileMerger = FileMerger(*filepaths,mode="r",encoding = "utf-8")

while True:
    filepaths_input = input("Enter filepaths, separate with commas, or type 'quit' to exit: ").strip()
    if filepaths_input.lower() == 'quit':
        break

    filepaths = [path.strip() for path in filepaths_input.split(",") if path.strip()]
    fileMerger = FileMerger(*filepaths, mode="r", encoding="utf-8")
    fileMerger.viewFile()

