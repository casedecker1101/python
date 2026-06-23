# write a python program 
# prompts the user 
# for the path of an existing CSV file
# copies the data from that file 
# into a new csv file
import csv
dataset = ()

while True:
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, newline = "") as f:
            print(f"{file_path} successfully opened.")
            reader = csv.DictReader(f)
            dataset = list(reader)
        break
    except FileNotFoundError:
        print(f"{file_path} not valid, please enter a valid file path.")

if dataset:
    fieldnames = dataset[0].keys()
    with open("data/2401.csv", "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames, dialect="excel")
        writer.writeheader()
        writer.writerows(dataset)
    print("File saved successfully.")
else:
    print("No rows found in source file.")