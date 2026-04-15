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

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data" / "EvolutionPopUSA_MainData.csv"

if not file_path.exists():
        print(f"File missing, cannot continue: {file_path}")
        raise SystemExit

print("--- Billboard 100 Through The Decades ---")
print("Type 'exit' to stop searching. \n")
        
while True:
    cinSearch = input("Options Menu Search [exit to quit]: " )
    if cinSearch.lower() == 'exit':
        break
    elif cinSearch == 'Artist search: ':
        # Open the file
        with open('data/EvolutionPopUSA_MainData.csv') as artistList:
            search = input("Search Term: ")
            for artist in artistList:
                if search in artist:
                    print(search)