# identify the most recent year in the dataset when someone received a nobel prize
# identify the earliest year when someone received a nobel prize
# identify the category with the highest number of prizes
# identify the laureate with the highest number of prizes
# identify the laureate who won the most recent prize in peace
# prize in medicine
# most jointly won the same prize in the same year
# how many prizes in economics
# in peace
# in literature

def nameNormal(value):
    """"Return lowercase text for consistent searching"""
    return value.strip().lower().replace(" ", "")

import json
from pprint import pprint

with open("ch20/data/prize.json", newline='', encoding='utf-8') as prize_json:
    read_json = json.load(prize_json)

full_names = [
    f"{nameNormal(laureate['firstname'])} {nameNormal(laureate['surname'])}"
    for prize in read_json["prizes"]
    for laureate in prize["laureates"]]
#1
highest_year = max(int(prize["year"]) for prize in read_json["prizes"])
#2
earliest_year = min(int(prize["year"]) for prize in read_json["prizes"])
#3
highest_cat = max(read_json["prizes"], key=lambda prize: len(prize["laureates"]))
#4
dupe = [name for name in full_names if full_names.count(name) > 1]
winner = max(set(full_names), key=lambda n: full_names.count(n))
#5
peace = max(read_json["prizes"], key=lambda prize: prize["category"] == "peace")
#6
medicine = max(read_json["prizes"], key=lambda prize: prize["category"] == "medicine")

# most jointly won the same prize in the same year
joint = [print(name) for name in full_names if full_names.count(name) >1 ]

joint = []
for name in full_names:
    if full_names.count(name) >1:
        joint.append(name)
        print(name)
        
print(joint)