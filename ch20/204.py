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

# 5 Minimum score for each restaurant
min_scores = []
for restaurant in restaurants:
    scores = get_scores(restaurant.get("grades", []))
    if scores:
        min_scores.append(min(scores))
        print(f"Restaurant: {restaurant.get('name')}, Minimum Score: {min(scores)}")
        print(f"Restaurant: {restaurant.get('name')}, Scores: {scores}")
        print(f"Minimum score for {restaurant.get('name')}:{min(scores)}")
        print(f"Minimum score for all restaurants: {min(min_scores)}")
        
# 6 Maximum score for each restaurant
max_scores = []
for restaurant in restaurants:
    scores = get_scores(restaurant.get("grades", []))
    if scores:
        max_scores.append(max(scores))
        print(f"Restaurant: {restaurant.get('name')}, Maximum Score: {max(scores)}")
        print(f"Restaurant: {restaurant.get('name')}, Scores: {scores}")
        print(f"Maximum score for {restaurant.get('name')}:{max(scores)}")
        print(f"Maximum score for all restaurants: {max(max_scores)}")

# 7 Average score for each type of cuisine in each borough
cuisine_borough_scores = {}
for restaurant in restaurants:
    cuisine = restaurant.get("cuisine")
    borough = restaurant.get("borough")
    scores = get_scores(restaurant.get("grades", []))

    if cuisine and borough and scores:
        key = (nameNormal(cuisine), nameNormal(borough))
        if key not in cuisine_borough_scores:
            cuisine_borough_scores[key] = []
        cuisine_borough_scores[key].extend(scores)
        for(cuisine_borough, scores) in cuisine_borough_scores.items():
            average_score = sum(scores) / len(scores) if scores else 0
            print(f"Cuisine: {cuisine_borough[0]}, Borough: {cuisine_borough[1]}, Average Score: {average_score:.2f}")
    
    # 8 Minimum Score for each type of cuisine in each borough
    min_cuisine_borough_scores = []
