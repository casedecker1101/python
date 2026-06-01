import csv
from functools import reduce
from pathlib import Path
data_path = Path(__file__).resolve().parents[1] / 'JobReadyPython' / 'data' / 'stocks.csv'

def highestClose(path):
    with open(data_path) as f:
        reader = csv.DictReader(f)
        high = reduce(lambda x, y: x if float(x['High']) > float(y['High']) else y, reader)
    return high
print(highestClose(data_path))