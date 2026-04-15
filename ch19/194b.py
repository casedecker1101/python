"""Billboard 100 Through The Decades.

A beginner-friendly CSV search program for artists, songs, clusters, and eras.
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # Folder containing this script.
DATA_DIR = BASE_DIR / "data"  # Chapter-local data folder.
FILE_NAME = "EvolutionPopUSA_MainData.csv"  # Name of the CSV we expect.
file_path = DATA_DIR / FILE_NAME  # Full path used by all functions.


def normalize_text(value):
    """Return lowercase text for consistent searching."""
    return value.strip().lower()


def artist_name_matches(search_term, artist_name, artist_name_clean):
    """Return True when the search term matches the artist name cleanly."""
    cleaned_search = "".join(ch for ch in search_term if ch.isalnum())
    normalized_words = [
        "".join(ch for ch in word.lower() if ch.isalnum())
        for word in artist_name.split()
    ]

    if " " in search_term:
        return search_term in artist_name.lower()

    return cleaned_search in normalized_words or cleaned_search == artist_name_clean.lower()

if not file_path.exists():
    print(f"File missing, cannot continue: {file_path}")
    raise SystemExit  # Exit now so later file reads do not crash.

def search_artist(term):
    """Return all artist matches for the user search term."""
    search_term = normalize_text(term)
    matches = []  # Collect formatted results here.

    with open(file_path, newline="", encoding="utf-8") as artist_list:
        reader = csv.DictReader(artist_list)
        for row in reader:
            artist_name = row["artist_name"]
            artist_name_clean = row["artist_name_clean"]
            if artist_name_matches(search_term, artist_name, artist_name_clean):
                matches.append(f"{artist_name} = {row['track_name']} ({row['year']})")

    return matches

def search_song(term):
    """Return all song-title matches for the user search term."""
    search_term = normalize_text(term)  # Lowercase once for case-insensitive matching.
    matches = []  # Collect formatted results here.

    with open(file_path, newline="", encoding="utf-8") as songs_file:
        reader = csv.DictReader(songs_file)
        for row in reader:
            track_name = row["track_name"]
            if search_term in track_name.lower():
                matches.append(f"{track_name} = {row['artist_name']} ({row['year']})")

    return matches

def cluster_eras():
    """Return the eras represented inside each cluster."""
    eras_by_cluster = {}  # Maps cluster id -> set of eras in that cluster.

    with open(file_path, newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file)
        for row in reader:
            era_label = row["era"]
            cluster_id = row["cluster"]
            if cluster_id not in eras_by_cluster:
                eras_by_cluster[cluster_id] = set()
            eras_by_cluster[cluster_id].add(era_label)

    results = []
    for cluster_id, eras in eras_by_cluster.items():
        era_list = ", ".join(sorted(eras))
        results.append(f"Cluster {cluster_id} contains eras: {era_list}")
    return results

def most_songs(term):
    """Return the artist with the most matching song titles."""
    artist_matches = {}  # Maps artist key -> display name + set of songs.
    search_term = normalize_text(term)  # Compare using lowercase titles.

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

    top_artist_data = max(
        artist_matches.values(),
        key=lambda artist_data: len(artist_data["songs"])
    )

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
    """Return artists that appear in two or more decades."""
    search_term = normalize_text(term)  # Compare using lowercase names.
    artists_by_decade = {}  # Maps artist key -> display name + set of decades.

    with open(file_path, newline="", encoding="utf-8") as artist_list:
        reader = csv.DictReader(artist_list)

        for row in reader:
            artist_name = row["artist_name"]
            artist_name_clean = row["artist_name_clean"]

            if artist_name_matches(search_term, artist_name, artist_name_clean):
                if artist_name_clean not in artists_by_decade:
                    artists_by_decade[artist_name_clean] = {
                        "display_name": artist_name,  # Name shown in output.
                        "decades": set()  # Set keeps each decade once.
                    }
                artists_by_decade[artist_name_clean]["decades"].add(row["decade"])

    matches = []
    for artist_data in artists_by_decade.values():
        decades_found = sorted(artist_data["decades"])  # Sort for readable output.
        if len(decades_found) >= 2:
            matches.append(
                f"{artist_data['display_name']} appears in {len(decades_found)} decades: {', '.join(decades_found)}"
            )

    return matches

def highest_cluster():
    """Return the cluster with the greatest number of songs."""
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
    top_cluster = max(cluster_counts, key=lambda cluster_id: cluster_counts[cluster_id])
    top_count = cluster_counts[top_cluster]

    # Step 8: Build and return results like other functions
    results = [f"Largest cluster: {top_cluster} ({top_count} songs)"]
    return results

def era_songs():
    """Return the era with the largest number of unique songs in the dataset."""
    era_to_songs = {}

    with open(file_path, newline="", encoding="utf-8") as era_file:
        reader = csv.DictReader(era_file)
        for row in reader:
            era = row["era"]
            song = row["track_name"]
            if era not in era_to_songs:
                era_to_songs[era] = {"songs": set()}
            era_to_songs[era]["songs"].add(song)

    if not era_to_songs:
        return []

    top_era = max(era_to_songs, key=lambda era: len(era_to_songs[era]["songs"]))
    top_count = len(era_to_songs[top_era]["songs"])

    results = [f"Era with the most songs in the dataset: {top_era} ({top_count} songs)"]
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
            artist = input("Enter the artist to search for: ").strip()
            if not artist:
                print("Please enter an artist name.")
                continue

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
            song = input("Enter the song to search for: ").strip()
            if not song:
                print("Please enter a song title.")
                continue

            song_matches = search_song(song)
            top_artist_results = most_songs(song)  # Extra insight for song searches.
            most_songs_era = era_songs()
            
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
            era_results = cluster_eras()  # Get the eras in each cluster for extra insight.

            if cluster_results:
                for result in cluster_results:
                    print(result)
            if era_results:
                for result in era_results:
                    print(result)
            else:
                print("No cluster data found.")
        else:
            print("Please type 'artist', 'song', or 'cluster'.")

if __name__ == "__main__":
    main()  # Entry point when running this file directly.