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
minimum_score = 0

for restaurant in restaurants:
    for grade_entry in restaurant.get("grades", []):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            total_score += score
            score_count += 1

# 1 Average score for each restaurant
average_score = total_score / score_count if score_count else 0

print(f"Total scores counted: {score_count}")
print(f"Average score across all restaurants: {average_score:.2f}")

# 2 Minimum score for each restaurant
for restaurant in restaurants:
    min_score = None
    for grade_entry in restaurant.get("grades", []):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            if min_score is None or score < min_score:
                min_score = score
            restaurant["min_score"] = min_score
            # Print the restaurant name and it's minimum score
            print(f"Restaurant: {restaurant.get('name', 'Unknown')}, Minimum Score: {min_score}")

# 3 Maximum score for each restaurant


# 9 Maxmimum score for each restaurant
score = max(grade_entry.get("score") for restaurant in restaurants for grade_entry in restaurant.get("grades", []) if isinstance(grade_entry.get("score"), (int, float)))

print(f"Maximum score across all restaurants: {score}")