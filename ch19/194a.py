# Find any artists with pop songs in two different decades
# -- Search for artist
# -- Sub search for all different decades the artist appears on the excel
# Identify artist with most songs on playlist
# -- search for the artist 
# -- sub search for all different songs the artist has on the excel
# identify cluster with most songs
# -- search for the clusters
# -- sub search for the cluster that appears the most amount of times on the excel
# identify genres within each cluster
# -- search for the cluster
# -- sub search genre
# -- print genre
# identify era with most songs
# -- search era
# -- sub search era with the most songs

import csv
from pathlib import Path

# variables
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
file_name = "EvolutionPopUSA_MainData.csv"
file_path = DATA_DIR / file_name

if not file_path.exists():
    print(f"File missing, cannot continue: {file_path}")
    raise SystemExit

def search_artist(term):
    matches = []
    with open(file_path, newline="", encoding='utf-8') as artist_list:
        reader = csv.DictReader(artist_list)
        for row in reader:
            artist_name = row["artist_name"]
            artist_name_clean = row["artist_name_clean"]
            if term.lower() in artist_name.lower():
                matches.append(f"{artist_name} = {row['track_name']} ({row['year']})")
            elif term.lower() in artist_name_clean.lower():
                matches.append(f"{artist_name_clean} = {row['track_name']} ({row['year']})")
        return matches
    
def search_song(term):
    matches = []
    with open(file_path, newline="", encoding='utf-8') as track_name:
        reader = csv.DictReader(track_name)
        for row in reader:
            track_name = row ["track_name"]
            if term.lower() in track_name.lower():
                matches.append(f"{track_name} = {row['track_name']} ({row['year']})")
        return matches

def search_first(term):
    matches = []
    with open(file_path, newline="", encoding = 'utf-8') as first_entry:
        reader = csv.DictReader(first_entry)
        for row in reader:
            first_entry = row["first_entry"]
            if term.lower() in first_entry.lower():
                matches.append(f"{first_entry} = {row['first_entry']} ({row['year']})")
        return matches

def two_decades(term):
    # Dictionary creation
    artist_decades = {}
    # lower case conversion search term
    term_lower = term.lower()

    # opening of file and saving data into temporary variables
    with open(file_path, newline="", encoding='utf-8') as artist_list:
        # requires a reader variables to iterate through file 
        # creation of reader variables
        reader = csv.DictReader(artist_list)
        
        # iterate through reader variables using row variables
        for row in reader:
            # row = coulmn = rows in the column iterated
            artist_name = row["artist_name"]
            artist_name_clean = row["artist_name_clean"]

            # if the search tearm is in artist_name or artist_name_clean
            if term_lower in artist_name.lower() or term_lower in artist_name_clean.lower():
                # uses the capitalized artist name without special characters 
                key = artist_name_clean
                normalized_name = ''.join(ch for ch in artist_name.lower() if ch.isalnum())
                if key not in artist_decades:
                    artist_decades[key] = {"display_name": artist_name, "decades": set()}
                elif normalized_name == artist_name_clean.lower():
                    artist_decades[key]["display_name"] = artist_name

                artist_decades[key]["decades"].add(row["decade"])

    matches = []
    for artist_data in artist_decades.values():
        decades_found = sorted(artist_data["decades"])
        if len(decades_found) > 2:
            matches.append(
                f"{artist_data['display_name']} appears in {len(decades_found)} decades: {', '.join(decades_found)}"
            )

    return matches

def most_songs(term):
    artist_songs = []
    term_lower = term.lower()
    
    with open(file_path, newline="", encoding = 'utf-8') as songs_list:
        reader = csv.DictReader(songs_list)
        for row in reader:
            track_name = row["track_name"]
            if term.lower() in track_name.lower():
                artist_songs.append(f"{track_name} = {row['track_name']} ({row['artist_name']})")
        return artist_songs
        
            
print("--- Billboard 100 Through The Decades ---")
print("Type 'exit' to stop searching.\n")

while True:
    try:
        cinSearch = input("Options menu: [Search by artists, songs, years or decades | exit to quit] ").strip().lower()
    except EOFError:
        print("\nNo input detected. Exiting program.")
        break

    if cinSearch == 'exit':
        break
    elif cinSearch in {'search'}:
        try:
            search = input("Artist Name to begin: ").strip()
        except EOFError:
            print("\nNo search term detected. Exiting program.")
            break
        
        artists = search_artist(search)
        songs = most_songs(search)
        firsts = search_first(search)
        decades = two_decades(search)
        
        if artists:
            for artist in artists:
                print(artist)
            if decades:
                for hit in decades:
                    print(hit)
        elif songs:
            for song in songs:
                print(song)
        elif firsts:
            for first in firsts:
                print(first)            
        else:
            print("No matches found.")
    else:
        print("Type 'search' or 'exit' to quit.")
        
        
        

