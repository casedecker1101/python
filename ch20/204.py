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
for restaurant in restaurants:
    max_score = None
    for grade_entry in restaurant.get("grades", []):
        score = grade_entry.get("score")
        if isinstance(score, (int, float)):
            if max_score is None or score > max_score:
                max_score = score
            restaurant["max_score"] = max_score
            # Print the restaurant name and it's maximum score
            print(f"Restaurant: {restaurant.get('name', 'Unknown')}, Maximum Score: {max_score}")

# 4 average score for each type of cuisine in each borough
cuisine_borough_scores = {}
for restaurant in restaurants:
    cuisine = restaurant.get("cuisine")
    borough = restaurant.get("borough")
    if cuisine and borough:
        key = (nameNormal(cuisine), nameNormal(borough))
        if key not in cuisine_borough_scores:
            cuisine_borough_scores [key] = {"total_score": 0, "count": 0}
            for grade_entry in restaurant.get("grades", []):
                score = grade_entry.get("score")
                if isinstance(score, (int, float)):
                    cuisine_borough_scores[key]["total_score"] += score
                    cuisine_borough_scores[key]["count"] += 1

        # Print average score for each type of cuisine in each borough
        for (cuisine, borough), data in cuisine_borough_scores.items():
            average_score = data["total_score"] / data["count"] if data["count"] else 0
            print(f"Cuisine: {cuisine.title()}, Borough: {borough.title()}, Average Score: {average_score:.2f}")
    
    # 5 Minimum score for each type of cuisine in each borough
    cuisine_borough_min_scores = {}
    for restaurant in restaurants:
        cuisine = restaurant.get("cuisine")
        borough = restaurant.get("borough")
        if cuisine and borough:
            key = (nameNormal(cuisine), nameNormal(borough))
            if key not in cuisine_borough_min_scores:
                cuisine_borough_min_scores[key] = None
                for grade_entry in restaurant.get("grades", []):
                    score = grade_entry.get("score")
                    if isinstance(score, (int, float)):
                        if cuisine_borough_min_scores[key] is None or score < cuisine_borough_min_scores[key]:
                            cuisine_borough_min_scores[key] = score
                # Print minimum score for each type of cuisine in each borough
                for (cuisine, borough), min_score in cuisine_borough_min_scores.items():
                    print(f"Cuisine: {cuisine.title()}, Borough: {borough.title()}, Minimum Score: {min_score}")

    #6 Maximum score for each type of cuisine in each borough
    cuisine_borough_max_scores = {}
    for restaurant in restaurants:
        cuisine = restaurant.get("cuisine")
        borough = restaurant.get("borough")
        if cuisine and borough:
            key = (nameNormal(cuisine), nameNormal(borough))
            if key not in cuisine_borough_max_scores:
                cuisine_borough_max_scores[key] = None
                for grade_entry in restaurant.get("grades", []):
                    score = grade_entry.get("score")
                    if isinstance(score, (int, float)):
                        if cuisine_borough_max_scores[key] is None or score > cuisine_borough_max_scores[key]:
                            cuisine_borough_max_scores[key] = score
                # Print maximum score for each type of cuisine in each borough
                for (cuisine, borough), max_score in cuisine_borough_max_scores.items():
                    print(f"Cuisine: {cuisine.title()}, Borough: {borough.title()}, Maximum Score: {max_score}")








# 9 Maxmimum score for each restaurant
score = max(grade_entry.get("score") for restaurant in restaurants for grade_entry in restaurant.get("grades", []) if isinstance(grade_entry.get("score"), (int, float)))

print(f"Maximum score across all restaurants: {score}")
