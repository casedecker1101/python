# Using lambda/map combination - convert text file to uppercase
from pathlib import Path


textStore = []
data_path = Path(__file__).resolve().parents[1] / 'JobReadyPython' / 'data' / 'flatland01.txt'
with open(data_path) as f:
    flatUpper = map(lambda x: x.upper(), f)
    print(list(flatUpper))

