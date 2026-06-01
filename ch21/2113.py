import csv
from pathlib import Path
path = Path(__file__).resolve().parents[1] / 'JobReadyPython' / 'data' / 'stocks.csv'

# highest price of the day is the Open price

def goodStockDay(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    good_day_filter = list(filter(lambda x: x['High'] == x['Open'], data)) # filter the data to only include days where the high price is higher than the open price
    print(good_day_filter)

goodStockDay(path)
