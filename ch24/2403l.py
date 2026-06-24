import csv
import json

dataset = list()


def normalize_dataset(data):
    """Return a list of dict rows suitable for csv.DictWriter."""
    if isinstance(data, list):
        if not data:
            raise ValueError("JSON file contains an empty list.")
        if not all(isinstance(row, dict) for row in data):
            raise ValueError("JSON list must contain only objects.")
        return data

    if isinstance(data, dict):
        # If JSON root is a single object, save it as one row.
        if all(not isinstance(value, list) for value in data.values()):
            return [data]

        # If JSON root wraps a list of records (for example {'customers': [...]})
        # pick the first list of objects.
        for value in data.values():
            if isinstance(value, list):
                if not value:
                    raise ValueError("JSON contains an empty records list.")
                if not all(isinstance(row, dict) for row in value):
                    raise ValueError("Wrapped JSON list must contain only objects.")
                return value

    raise ValueError("JSON must be an object, a list of objects, or an object containing a list of objects.")

while True:
    file_input = input("Enter file path, quit to exit: ")

    if file_input == 'quit':
        break

    try:
        with open(file_input, encoding="utf-8") as json_file:
            raw_data = json.load(json_file)
            dataset = normalize_dataset(raw_data)
            print("File Open Successfully.")
    except json.JSONDecodeError:
        print("Invalid JSON format. Exiting program.")
        break
    except FileNotFoundError:
        print("File not found. Exiting Program.")
        break
    except ValueError as exc:
        print(f"JSON structure error: {exc}")
        continue

    # save to csv
    save_file = input("Enter file path for save location: ")

    try:
        with open(save_file, 'w', newline='', encoding='utf-8') as file_save:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(file_save, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
            print("CSV file saved successfully.")
    except IOError:
        print("File cannot be saved. Check permissions/location.")