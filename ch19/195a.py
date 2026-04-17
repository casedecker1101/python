# Create function - reads car_data into list
# - Each element must be a dictionary
# -- Dictionary keys are the column names
# --- Values are the elements in each column

import csv
from pathlib import Path

# Storage
carDatabase = []

# Variables
BASE_DIR = Path(__file__).resolve().parent # Folder containing this script.

DATA_DIR = BASE_DIR / "data" # Main local data folder.

FILE_NAME = "car_data.csv" # Database

file_path = DATA_DIR / FILE_NAME # Full path used by all functions

# Begin Function Definitions

# normalizes all input
def normalize_text(value):
    """Return lowercase text for consistent searching """
    return value.strip().lower()

def readData():
    with open(file_path,newline="",encoding="utf-8") as carData:
        reader = csv.DictReader(carData)
        
        for row in reader:
            carDatabase.append(row)
            print(carDatabase)
        return carDatabase

value = readData()
print(value)  


