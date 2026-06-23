# extract class
class extract:
    def fromCSV(self, file_path, delimiter=",", quotechar="|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
                  csv_file = csv.DictReader(f, delimiter = delimiter, quotechar = quotechar)
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
    
    def fromMYSQL(self, host, username, password, db, query):
          if not host or not username or not db or not query:
                raise Exception("Please make sure  that you input a valid host, username, password, database, and query.")
          import pymysql
                  
                  
