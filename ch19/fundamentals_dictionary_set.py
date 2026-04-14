import os, csv

my_dictionary = {}
value = 0

artist_counts = {"Taylor Swift": 12, "Drake":9}
print(artist_counts["Drake"])

print(artist_counts.get("Adele"))
print(artist_counts.get("Adele",0))

artist_counts["Drake"] = 10

# increment counter pattern
artist = "Drake"
if artist not in artist_counts:
    artist_counts[artist] = 0
artist_counts[artist] += 1

# generalized counter pattern
key = "Value"
if key not in my_dictionary:
    my_dictionary[key] = value
my_dictionary[key] += value

# cleaner increment with get
artist_counts[artist] = artist_counts.get(artist,0) + 1

# add new key/value
my_dictionary["Key"] = 4

# delete entries
## Delete by key >> Errors if key is missing
del my_dictionary["key"]

# remove and return value (safer with default)
removed = my_dictionary.pop("Key", None)

# clear everything
artist_counts.clear()

# loop through dictionary keys
for key in my_dictionary:
    print(key)
    
# loop through dictionary key and value together
for key, value in my_dictionary.items():
    print(key,value)
    
# Set Fundamentals

# create a set
set_name = {"value1","value2","value3"}

# Empty set (important)
set_name = set() # correct
set_name = {} # This is an empty dictionary, similarity is only in the brackets.

# Add/update
set_name.add("value0") # add one item
set_name.update(["value1","value2"])

# Accessing set values
# -- Sets are unordered, so no indexing like set_name[0]
# -- Values are checked by membership
if "value" in set_name:
    print("message")
    
# Deleting values
set_name.remove("value") # error if value is missing
set_name.discard("value") # no error if missing
removed_set_value = set_name.pop() # removes arbitrary item
set_name.clear()