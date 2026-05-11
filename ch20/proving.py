# how many prizes in economics
# in peace
# in literature

def nameNormal(value):
    """"Return lowercase text for consistent searching"""
    return value.strip().lower().replace(" ", "")

import json
import os

_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(_dir, "data", "prize.json"), encoding='utf-8') as prize_json:
    read_json = json.load(prize_json)

winners = 0

for prize in read_json.get("prizes", []):
    if prize.get("category") == "peace":
        winners += len(prize.get("laureates", []))

print(f"Total economics winners: {winners}")