# compute avg score for each restaurant
# * minimum score for each restaurant
# * maximum score 
# * average score for each type of cuisine in each borough
# * minimum score 
# * maximum score

import json
import os
from pprint import pprint

def nameNormal(value):
    """Return lowercase text for consistent searching"""
    return value.strip().lower().replace(" ", "")

with open("ch20/data/restaurant.json", newline="", encoding='utf-8') as rest_json:
    read_json = json.load(rest_json)

    _dir = os.path.dirname(os.path.abspath(__file__))

average_score = read_json["score"]
values = average_score.values()

average_score = sum(values) / len(values)

print(average_score)
