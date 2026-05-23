# minimum score for each restaurant

import json
import os

def nameNormal(value):
    """Return lowercase text for consistent searching"""
    return value.strip().lower().replace(" ", "")

restaurants = []

with open("ch20/data/restaurant.json","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        restaurants.append(json.loads(line))

for restaurant in restaurants:
    name = restaurant.get("name", "Unknown")
    min_score = None
    for grade_entry in restaurant.get("grades", []):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            if min_score is None or score < min_score:
                min_score = score
    restaurant["min_score"] = min_score

# print the restaurant name and it's minimum score
for restaurant in restaurants:
    print(f"Restaurant: {restaurant.get('name', 'Unknown')}, Minimum Score: {restaurant.get('min_score', 'N/A')}")
    max_score = None
    for grade_entry in restaurant.get("grades", []):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            if max_score is None or score > max_score:
                max_score = score
            restaurant["max_score"] = max_score
    print(f"Restaurant: {restaurant.get('name', 'Unknown')}, Maximum Score: {max_score}")




