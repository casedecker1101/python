import csv # import the csv module
from functools import reduce
from pathlib import Path
data_path = Path(__file__).resolve().parents[1] / 'JobReadyPython' / 'data' / 'stocks.csv'

def badStockDay(path):
    with open(data_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    bad_day = list(filter(lambda x: x['Open'] > x['Close'], data)) # filter the data to only include days where the open price is higher than the close price
    print(bad_day)

badStockDay(data_path)
