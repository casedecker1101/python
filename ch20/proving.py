# 5 maximum score for each type of cuisine in each borough

import json

# name normalization function
def nameNormal(value):
    """Return lowercase text for consistent searching"""
    return value.strip().lower().replace(" ", "")

with open("ch20/data/restaurant.json","r",encoding="utf-8") as f:
    restaurants = [json.loads(line.strip()) for line in f if line.strip()]
    # maximum score for each type of cuisine in each borough
    cuisine_borough_max_score = {}
    for restaurant in restaurants:
        cuisine = nameNormal(restaurant.get("cuisine"))
        borough = nameNormal(restaurant.get("borough"))
        if not cuisine or not borough:
            continue
        max_score = max((grade.get("score") for grade in restaurant.get("grades", []) if isinstance(grade.get("score"), (int,float))), default = 0,)
        if cuisine not in cuisine_borough_max_score:
            cuisine_borough_max_score[cuisine] = {}
        if borough not in cuisine_borough_max_score[cuisine]:
            cuisine_borough_max_score[cuisine][borough] = max_score
        else:
            cuisine_borough_max_score[cuisine][borough] = max(cuisine_borough_max_score[cuisine][borough], max_score)
            print(f"Maximum score for {cuisine} in {borough}: {cuisine_borough_max_score[cuisine][borough]}")