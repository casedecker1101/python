import os

try:
    if not os.path.exists("data/flatland01.txt") or not os.path.exists("data/IncidentTicket.txt"):
        raise FileNotFoundError("One or more input files are missing")
    with open("data/flatland01.txt", 'r') as file01, open("data/IncidentTicket.txt", 'r') as file02, open("data/combined.txt", 'w') as file03:
        data01 = file01.read()
        data02 = file02.read()
        data = data01 + data02
        file03.write(data)
except FileNotFoundError as e:
    print(f"Error: {e}")
except IOError as e:
    print(f"Error: Cannot Write to Location {e}")