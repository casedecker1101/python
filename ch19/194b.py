import os
import csv

file_name = "EvolutionPopUSA_MainData.csv"  # Name of the CSV we expect.
folder = "data"  # Folder where the CSV should live.
file_path = os.path.join(folder, file_name)  # Full path used by all functions.

if not os.path.exists(folder):
    os.makedirs(folder)  # Create the folder once if missing.

if not os.path.exists(file_path):
    print("File missing, cannot continue.")  # Tell the user why we are stopping.
    raise SystemExit  # Exit now so later file reads do not crash.

def search_artist(term):
    search_term = term.lower()  # Lowercase once for case-insensitive matching.
    matches = []  # Collect formatted results here.

    with open(file_path, newline="", encoding="utf-8") as artist_list:
        reader = csv.DictReader(artist_list)
        for row in reader:
            artist_name = row["artist_name"]
            if search_term in artist_name.lower():
                matches.append(f"{artist_name} = {row['track_name']} ({row['year']})")

    return matches

def search_song(term):
    search_term = term.lower()  # Lowercase once for case-insensitive matching.
    matches = []  # Collect formatted results here.

    with open(file_path, newline="", encoding="utf-8") as songs_file:
        reader = csv.DictReader(songs_file)
        for row in reader:
            track_name = row["track_name"]
            if search_term in track_name.lower():
                matches.append(f"{track_name} = {row['artist_name']} ({row['year']})")

    return matches

def cluster_genres():
    genres_clusters = {} # Maps cluster id -> set of genres in that cluster
    with open(file_path, newline="", encoding="utf-8") as genres_file:
        reader = csv.DictReader(genres_file)
        for row in reader:
            genre = row["era"]
            cluster_id = row["cluster"]
            if cluster_id not in genres_clusters:
                genres_clusters[cluster_id] = set()
                genres_clusters[cluster_id].add(genre)
    results = []

    for cluster_id, genres in genres_clusters.items():
        genre_list = ", ".join(sorted(genres)) # sort genres for stable output
        results.append(f"Cluster {cluster_id} contains genres: {genre_list}")
    return results

def most_songs(term):
    artist_matches = {}  # Maps artist key -> display name + set of songs.
    search_term = term.lower()  # Compare using lowercase titles.

    with open(file_path, newline="", encoding="utf-8") as songs_list:
        reader = csv.DictReader(songs_list)

        for row in reader:
            track_name = row["track_name"]
            artist_name = row["artist_name"]
            artist_key = row["artist_name_clean"]

            if search_term in track_name.lower():
                if artist_key not in artist_matches:
                    artist_matches[artist_key] = {
                        "display_name": artist_name,  # Pretty name for printing.
                        "songs": set()  # Set removes duplicate song titles.
                    }
                artist_matches[artist_key]["songs"].add(track_name)

    if not artist_matches:
        return []  # Nothing matched the song search.

    top_artist_data = None  # Will store the best artist record.
    top_song_count = -1  # Starts below any real song count.

    for artist_data in artist_matches.values():
        current_song_count = len(artist_data["songs"])
        if current_song_count > top_song_count:
            top_song_count = current_song_count
            top_artist_data = artist_data

    unique_songs = sorted(top_artist_data["songs"])  # Sorted for stable output order.
    song_count = len(unique_songs)
    song_label = "song" if song_count == 1 else "songs"
    results = [
        f"Artist with the most matching songs: {top_artist_data['display_name']} ({song_count} {song_label})"
    ]

    for song in unique_songs:
        results.append(f"{top_artist_data['display_name']} = {song}")

    return results

def two_decades(term):
    search_term = term.lower()  # Compare using lowercase names.
    artists_by_decade = {}  # Maps artist key -> display name + set of decades.

    with open(file_path, newline="", encoding="utf-8") as artist_list:
        reader = csv.DictReader(artist_list)

        for row in reader:
            artist_name = row["artist_name"]
            artist_name_clean = row["artist_name_clean"]

            if search_term in artist_name.lower() or search_term in artist_name_clean.lower():
                if artist_name_clean not in artists_by_decade:
                    artists_by_decade[artist_name_clean] = {
                        "display_name": artist_name,  # Name shown in output.
                        "decades": set()  # Set keeps each decade once.
                    }
                artists_by_decade[artist_name_clean]["decades"].add(row["decade"])

    matches = []
    for artist_data in artists_by_decade.values():
        decades_found = sorted(artist_data["decades"])  # Sort for readable output.
        if len(decades_found) > 2:
            matches.append(f"{artist_data['display_name']} appears in {len(decades_found)} decades: {', '.join(decades_found)}")

    return matches

def highest_cluster():
    # Step 1: Storage - Key is cluster id, value is count of songs in that cluster
    cluster_counts = {}  # Maps cluster id -> song count.

    # Step 2: Open and read the CSV file
    with open(file_path, newline="", encoding="utf-8") as cluster_file:
        reader = csv.DictReader(cluster_file)

        # Step 3: Loop through every row and tally up each cluster
        for row in reader:
            cluster_id = row["cluster"]  # Grab the cluster value from this row.

            # Step 4: If we haven't seen this cluster before, start counting at 0
            if cluster_id not in cluster_counts:
                cluster_counts[cluster_id] = 0

            # Step 5: Add 1 to this cluster's count
            cluster_counts[cluster_id] += 1

    # Step 6: If nothing was found, return early
    if not cluster_counts:
        return []

    # Step 7: Find which cluster had the highest count
    top_cluster = max(cluster_counts, key=cluster_counts.get)
    top_count = cluster_counts[top_cluster]

    # Step 8: Build and return results like other functions
    results = [f"Largest cluster: {top_cluster} ({top_count} songs)"]
    return results

def era_most_songs():
    eraMS = {}

    with open(file_path, newline="", encoding="utf-8") as era_file:
        reader = csv.DictReader(era_file)
        
        for row in reader:
            era = row["era"]
            track_name = row["track_name"]

            if era not in eraMS:
                if track_name not in eraMS:
                    eraMS[era] = {"songs": set()}
                    eraMS[era]["songs"].add(track_name)
        top_era = max(eraMS, key=eraMS.get)
        
    results = [f"Era with the most songs: {top_era} ({track_name}} songs)"]
    return results
            
def main():
    print("--- Billboard 100 Through The Decades ---")
    print("Type 'exit' to stop searching.\n")

    while True:
        try:
            menu_choice = input("Options Menu: search or exit: ").strip().lower()  # Normalize user input.
        except EOFError:
            print("\nNo input detected. Exiting program.")
            break

        if menu_choice == "exit":
            break

        if menu_choice != "search":
            print("Please type 'search' or 'exit'.")
            continue

        try:
            search_type = input("Search by artist, song or cluster: ").strip().lower()  # Normalize user input.
        except EOFError:
            print("\nNo search type detected. Exiting program.")
            break

        if search_type == "artist":
            artist = input("Enter the artist to search for: ")
            artists = search_artist(artist)
            decades = two_decades(artist)  # Extra insight for artist searches.

            if artists:
                for match in artists:
                    print(match)
            else:
                print("No artist matches found.")

            if decades:
                for hit in decades:
                    print(hit)

        elif search_type == "song":
            song = input("Enter the song to search for: ")
            song_matches = search_song(song)
            top_artist_results = most_songs(song)  # Extra insight for song searches.
            most_songs_era = era_most_songs()
            
            if song_matches:
                for match in song_matches:
                    print(match)
            else:
                print("No song matches found.")

            if top_artist_results:
                for line in top_artist_results:
                    print(line)
            
            if most_songs_era:
                for hit in most_songs_era:
                    print(hit)
        
        elif search_type == "cluster":
            cluster_results = highest_cluster()  # Get the largest cluster info.
            genre_results = cluster_genres() # Get genres in each cluster for extra insight.
            
            if cluster_results:
                for result in cluster_results:
                    print(result)
            if genre_results:
                for result in genre_results:
                    print(result)
            else:
                print("No cluster data found.")
        else:
            print("Please type 'artist', 'song', or 'cluster'.")

if __name__ == "__main__":
    main()  # Entry point when running this file directly.