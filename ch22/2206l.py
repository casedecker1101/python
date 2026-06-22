# display tr/except for - missing files
# message must be meaningful, allowing second path entry
# checks new path
# option to quit if path cannot be provided

class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter=delimiter, quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset
    
    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

while True:
    file_path = input("Please enter the file path: ")

    if file_path == 'quit':
        break 

    try:
        with open(file_path, 'r') as f:
            print(f"{file_path} is valid. ")

    except FileNotFoundError:
        file_path = input("Please enter a valid file path: ")

        if file_path == 'quit':
             break
        
        try:
                with open(file_path, 'r') as f:
                    print(f"{file_path} is valid.")
                    break
        except FileNotFoundError:
                print("File not found, exiting program.")



e = extract()
dataset1 = e.fromCSV(file_path="data/missing_file.csv")
dataset2 = e.fromJSON(file_path="data/missing_file.json")
