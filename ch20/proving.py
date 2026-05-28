# proving script for restaurant score summaries

import json
import os


def nameNormal(value):
    """Return lowercase text for consistent searching"""
    return value.strip().lower().replace(" ", "")


def get_scores(grade_entries):
    return [
        grade.get("score")
        for grade in grade_entries
        if isinstance(grade.get("score"), (int, float))
    ]


restaurants = []
data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "restaurant.json")

with open(data_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            restaurants.append(json.loads(line))

# Minimum and maximum scores for each restaurant
for restaurant in restaurants:
    scores = get_scores(restaurant.get("grades", []))
    if not scores:
        continue

    print(
        f"Restaurant: {restaurant.get('name', 'Unknown')}, "
        f"Minimum Score: {min(scores)}, Maximum Score: {max(scores)}"
    )

# Maximum score for each cuisine in each borough
cuisine_borough_max_score = {}
for restaurant in restaurants:
    cuisine = nameNormal(restaurant.get("cuisine"))
    borough = nameNormal(restaurant.get("borough"))
    if not cuisine or not borough:
        continue

    scores = get_scores(restaurant.get("grades", []))
    if not scores:
        continue

    key = (cuisine, borough)
    current_max = max(scores)
    if key not in cuisine_borough_max_score:
        cuisine_borough_max_score[key] = current_max
    else:
        cuisine_borough_max_score[key] = max(cuisine_borough_max_score[key], current_max)

for (cuisine, borough), score in cuisine_borough_max_score.items():
    print(f"Maximum score for {cuisine.title()} in {borough.title()}: {score}")
