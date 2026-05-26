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


def get_scores(grade_entries):
    return [
        grade_entry.get("score")
        for grade_entry in grade_entries
        if isinstance(grade_entry.get("score"), (int, float))
    ]

restaurants = []

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "restaurant.json")

with open(data_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        restaurants.append(json.loads(line))

# Average, minimum, and maximum score for each restaurant
restaurant_stats = []
for restaurant in restaurants:
    scores = get_scores(restaurant.get("grades", []))
    if not scores:
        continue

    restaurant_stats.append(
        {
            "name": restaurant.get("name", "Unknown Restaurant"),
            "borough": restaurant.get("borough", "Unknown Borough"),
            "cuisine": restaurant.get("cuisine", "Unknown Cuisine"),
            "average": sum(scores) / len(scores),
            "minimum": min(scores),
            "maximum": max(scores),
        }
    )

print("Average, minimum, and maximum score for each restaurant:")
for stat in restaurant_stats:
    print(
        f"{stat['name']} ({stat['borough']}, {stat['cuisine']}): "
        f"avg={stat['average']:.2f}, min={stat['minimum']}, max={stat['maximum']}"
    )

# Average, minimum, and maximum score for each type of cuisine in each borough

cuisine_borough_score = {}

for restaurant in restaurants:
    cuisine = nameNormal(restaurant.get("cuisine"))
    borough = nameNormal(restaurant.get("borough"))
    if not cuisine or not borough:
        continue

    key = (cuisine, borough)
    scores = get_scores(restaurant.get("grades", []))
    if scores:
        cuisine_borough_score.setdefault(key, []).extend(scores)

cuisine_borough_stats = {
    key: {
        "average": sum(scores) / len(scores),
        "minimum": min(scores),
        "maximum": max(scores),
    }
    for key, scores in cuisine_borough_score.items()
    if scores
}

print("Average, minimum, and maximum score for each type of cuisine in each borough:")
for (cuisine, borough), stat in cuisine_borough_stats.items():
    print(
        f"{cuisine.title()} in {borough.title()}: "
        f"avg={stat['average']:.2f}, min={stat['minimum']}, max={stat['maximum']}"
    )
