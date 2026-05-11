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
import os
from pprint import pprint

with open("ch20/data/prize.json", newline='', encoding='utf-8') as prize_json:
    read_json = json.load(prize_json)

    _dir = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(_dir, "data", "prize.json"), encoding='utf-8') as prize_json:
    read_json = json.load(prize_json)


full_names = [
    f"{nameNormal(laureate['firstname'])} {nameNormal(laureate['surname'])}"
    for prize in read_json["prizes"]
    for laureate in prize["laureates"]
    ]


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
#7
max_joint_count = max(len(prize.get("laureates", [])) for prize in read_json["prizes"])
most_joint_prizes = [
    prize for prize in read_json["prizes"]
    if len(prize.get("laureates", [])) == max_joint_count
]
for prize in most_joint_prizes:
    joint_names = [
        f"{laureate.get('firstname', '').strip()} {laureate.get('surname', '').strip()}".strip()
        for laureate in prize.get("laureates", [])
    ]
    print(
        f"Most jointly won prize: {prize['category']} ({prize['year']}) with {len(joint_names)} co-winners"
    )
    print(joint_names)

#8
economics_winners = 0
for prize in read_json.get("prizes", []):
    if prize.get("category") == "economics":
        economics_winners += len(prize.get("laureates", []))

print(f"Total economics winners: {economics_winners}")

#9 
peace_winners = 0
for prize in read_json.get("prizes",[]):
    if prize.get("category") == "peace":
        peace_winners += len(prize.get("laureates", []))
print(f"Total peace winners: {peace_winners}")

#10 
literature_winners = 0
for prize in read_json.get("prizes",[]):
    if prize.get("category") == "literature":
        literature_winners += len(prize.get("laureates", []))
print(f"Total literature winners: {literature_winners}")