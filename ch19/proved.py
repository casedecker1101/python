import os
import csv

file_name = "EvolutionPopUSA_MainData.csv"  # Name of the CSV we expect.
folder = "data"  # Folder where the CSV should live.
file_path = os.path.join(folder, file_name)  # Full path used by all functions.


def era_songs():
    era_to_songs = {}

    with open(file_path,newline="",encoding="utt-8")as era_file:
        reader = csv.DictReader(era_file)
        for row in reader:
            era = row["era"]
            song = row["track_name"]
            if era not in era_to_songs:
                    era_to_songs[era] = {"songs": set()}
            era_to_songs[era]["songs"].add(song)

    top_era = max(era_to_songs, key=lambda era: len(era_to_songs[era]["songs"]))
    top_count = len(era_to_songs[top_era]["songs"])
        
    results = [f"Era with the most songs: {top_era} ({top_count} songs)"]