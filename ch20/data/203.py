# identify the most recent year in the dataset when someone received a nobel prize
# identify the earliest year when someone received a nobel prize
# identify the category with the highest number of prizes
# identify the laureate with the highest number of prizes
# identify the laureate who won the most recent price in peace
# prize in medicine
# yeah most jointly won the same prize in the same year
# how many prizes in economics
# in peace
# in literature

import json
from pprint import pprint

with open("ch20/data/prize.json", newline='', encoding='utf-8') as prize_json:
    read_json = json.load(prize_json)

highest_year = max(int(prize["year"]) for prize in read_json["prizes"])
earliest_year = min(int(prize["year"]) for prize in read_json["prizes"])

print(earliest_year)
print(highest_year)