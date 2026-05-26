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

restaurants = []

with open("ch20/data/restaurant.json","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        restaurants.append(json.loads(line))

# Average score for each restaurant
total_score = 0
score_count = 0

for restaurant in restaurants:
    for grade_entry in restaurant.get("grades", []):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            total_score += score
            score_count += 1

average_score = total_score / score_count if score_count else 0

print(f"Total scores counted: {score_count}")
print(f"Average score across all restaurants: {average_score:.2f}")

min_score = []

for restaurant in restaurants:
    for grade_entry in restaurant.get("grades",[]):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            min_score.append(score)
print(f"Minimum score across all restaurants: {min(min_score)}")
print(f"Maximum score across all restaurants: {max(min_score)}")
print(f"Average score across all restaurants: {sum(min_score)/len(min_score):.2f}")

# 4 average score for each type of cuisine in each borough

cuisine_borough_score = {}

for restaurant in restaurants:
    cuisine = nameNormal(restaurant.get("cuisine"))
    borough = nameNormal(restaurant.get("borough"))
    if not cuisine or not borough:
        continue

    key = (cuisine, borough)
    for grade_entry in restaurant.get("grades", []):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            cuisine_borough_score.setdefault(key, []).append(score)

cuisine_borough_avg_score = {
    key: sum(scores) / len(scores)
    for key, scores in cuisine_borough_score.items()
    if scores
}

print("Average score for each type of cuisine in each borough:")
for (cuisine, borough), avg_score in cuisine_borough_avg_score.items():
    print(f"{cuisine.title()} in {borough.title()}: {avg_score:.2f}")
