
dataset = ()

while True:
    file_path = input("Enter file path to CSV file: ")
    
    if file_path == 'quit':
        break

    # loading data from csv
    try:
        import csv
        with open(file_path) as f:
            reader = csv.DictReader(f)
            dataset = list(reader)
            print("File open successfully.")
    except FileNotFoundError:
        file_path = input("Enter a valid file path or quit to exit: ")
        
        if file_path == 'quit':
           break
        
        try:
            with open(file_path) as f:
                reader = csv.DictReader(f)
                dataset = list(reader)
                print("File open successfully.")
        except FileNotFoundError:
            print("File not found. Exiting program.")

    # saving data to json
    saved_file = input("Enter location to save the file: ")
    
    try:
        import json
        with open(saved_file, 'w') as json_save:
            json.dump(dataset, json_save)
            print("File saved successfully.")
    except (IOError,OSError):
        print("File unable to be saved due to system error.")
        
            