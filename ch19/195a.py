"""Accesses the Car Database for arbitrary data on automobiles"""
import csv
from pathlib import Path

# Storage
carDatabase = {}

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
            carDatabase[row["id"]] = row
            print(carDatabase)
        return carDatabase

def carMake(term):
    searchTerm = normalize_text(term)
    make = []

    with open(file_path, newline="", encoding="utf-8") as csv_make:
        reader = csv.DictReader(csv_make)
        results = filter(lambda row: searchTerm in normalize_text(row["make"]), reader,)
        for row in results:    
            make.append(f"{row['make']} {row['body_style']} {row['price']}")
    print(make)
    return make

def fuelEfficient():
    matches = []
    
    with open(file_path, newline="", encoding="utf-8") as csv_fuelefficient:
        reader = csv.DictReader(csv_fuelefficient)
        results = filter(lambda row: row["city_mpg"].isdigit() and int(row["city_mpg"]) >= 35, reader,)
        
        for row in results:
            matches.append(f"{row['make']} {row['body_style']} {row['city_mpg']} mpg")
    return matches

def horsePower():
    matches = []
    with open(file_path, newline="", encoding="utf-8") as csv_hp:
        reader = csv.DictReader(csv_hp)
        results = filter(lambda row: row["horsepower"].isdigit() and int(row["horsepower"]) >= 100, reader,)
        
        for row in results:
            matches.append(f"{row['make']} {row['body_style']} {row['horsepower']} hp")
    return matches

def price(inputPrice):
    matches = []
    inputPrice = int(inputPrice)
    with open(file_path, newline="", encoding="utf-8") as csv_prices:
        reader = csv.DictReader(csv_prices)
        results = filter(lambda row: row["price"].isdigit() and int(row["price"]) <= inputPrice, reader,)
        
        for row in results:
            matches.append(f"Price: {row['price']} Make: {row['make']} Body: {row['body_style']} HP: {row['horsepower']} MPG: {row['city_mpg']}")
        return matches

cinMain = input("Please enter the budget you broke bastard: ")
print(price(cinMain))
