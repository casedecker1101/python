# How many movies are included in the file
# In what year was the movie "A Separation" made?
# How many movies has Martin Scorsese directed?

# Normalize names so comparisons ignore case and spaces.
def nameNormal(value):
    # Convert to lowercase, trim whitespace, and remove internal spaces.
    return value.lower().strip().replace(" ", "")

# 1. How many movies are included in the file?
# Load the movie data from the JSON file.
import json

# Open the file and parse the JSON array into memory.
with open("ch20/data/movies.json", "r", encoding="utf-8") as f:
    # Read the file contents into a Python list.
    movies = json.load(f)
    # Print the number of movies loaded.
    print(f"Total number of movies: {len(movies)}")

# 2. In what year was the movie "A Separation" made?
# Store the title we want to search for.
movie_title = "A Separation"
# Hold the year once we find the matching movie.
movie_year = None
# Walk through every movie until the title matches.
for movie in movies:
    # Compare normalized titles so spacing and capitalization do not matter.
    if nameNormal(movie.get("title", "")) == nameNormal(movie_title):
        # Save the movie year from the matching record.
        movie_year = movie.get("year")
        # Stop searching after the first match.
        break
# Print the result after the loop finishes.
print(f"The movie '{movie_title}' was made in the year: {movie_year}")

# 3. How many movies has Martin Scorsese directed?
# Store the director name we want to count.
director_name = "Martin Scorsese"
# Count movies where any normalized director name matches.
scorsese_movie_count = sum(
    1
    for movie in movies
    if any(
        nameNormal(d) == nameNormal(director_name)
        for d in movie.get("directors", [])
    )
)
# Print the total number of movies directed by Martin Scorsese.
print(f"Martin Scorsese has directed {scorsese_movie_count} movies.")

# 4. Average number of movies a director has directed?
# Use a defaultdict to track movie counts per director.
from collections import defaultdict
# Map normalized director names to the number of movies they directed.
director_movie_counts = defaultdict(int)
# Count one movie at a time for each director.
for movie in movies:
    # Read the directors list from the current movie.
    directors = movie.get("directors", [])
    # Increment each listed director's count.
    for director in directors:
        director_movie_counts[nameNormal(director)] += 1
# Compute how many unique directors were seen.
total_directors = len(director_movie_counts)
# Compute the average movies per director.
average_movies_per_director = sum(director_movie_counts.values()) / total_directors if total_directors else 0
# Print the average for review.
print(f"Average number of movies directed per director: {average_movies_per_director:.2f}")

# 5 Names of all movie genres
for movie in movies:
    genres = movie.get("genres", [])
    for genre in genres:
        print(len(genre))

# 6 Average number of genres per movie
total_genres = 0
for movie in movies:
    genres = movie.get("genres", [])
    total_genres += len(genres)
    average_genres_per_movie = total_genres / len(movies) if movies else 0
print(f"Average number of genres per movie: {average_genres_per_movie:.2f}")

# 7 list all movies that have won an Oscar
for movie in movies:
    awards = movie.get("awards", [])
    for award in awards:
        if nameNormal(award.get("name", "")) == nameNormal("Oscar") and award.get("won", False):
            print(movie.get("title", "Unknown"))
            break

# 8 list all movies that have won an Oscar in the Best Picture category
for movie in movies:
    awards = movie.get("awards", [])
    for award in awards:
        if (nameNormal(award.get("name", "")) == nameNormal("Oscar") and award.get("won", False) and nameNormal(award.get("category", "")) == nameNormal("Best Picture")):
            print(movie.get("title", "Unknown"))
            break

# 9 list all movies that have won an Oscar in the Best Picture category and were directed by Martin Scorsese
for movie in movies:
    awards = movie.get("awards", [])
    directors = movie.get("directors", [])
    if any(nameNormal(d) == nameNormal("Martin Scorsese") for d in directors):
        for award in awards:
            if (nameNormal(award.get("name", "")) == nameNormal("Oscar") and award.get("won", False)
            and nameNormal(award.get("category", "")) == nameNormal("Best Picture")):
                print(movie.get("title", "Unknown"))
                break

# 10 list all movies directed by Brian De Palma that have won an Oscar in any category
for movie in movies:
    awards = movies.get("awards",[])
    directors = movie.get("directors", [])
    if any(nameNormal(d) == nameNormal("Brian De Palma") for d in directors):
        for award in awards:
            if nameNormal(award.get("name", "")) == nameNormal("Oscar") and award.get("won", False):
                print(movie.get("title", "Unknown"))
                break


