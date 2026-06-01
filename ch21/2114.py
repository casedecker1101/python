import csv
from pathlib import Path
data_path = Path(__file__).resolve().parents[1] / 'JobReadyPython' / 'data' / 'stocks.csv'


def goodDay(data_path):
    with open(data_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    goodDay = list(filter(lambda x: x['Close'] == x['High'], data))
    print(goodDay)

goodDay(data_path)