# Professor-Style Walkthrough for 194b.py

## Overview
This program is a polished, beginner-friendly search tool built around a CSV dataset of popular songs. It demonstrates the kind of Python thinking students are expected to develop by the end of a first semester: file handling, loops, dictionaries, sets, functions, user input, and program organization.

The main goals of the program are to:

1. safely locate the data file
2. search by artist or song
3. identify artists that appear across multiple decades
4. find the cluster with the most songs
5. identify the era with the most songs

---

## Section 1: Module description and imports
The opening triple-quoted string is a module docstring. Think of it as a label at the top of the file that explains what the program does.

Then the program imports:

- csv, to read spreadsheet-style data
- Path from pathlib, to build safe file paths

This is a very good real-world improvement over using fragile plain strings for file locations.

---

## Section 2: File path setup
The code creates a path in steps:

- BASE_DIR is the folder where the Python file lives
- DATA_DIR is the data folder inside that chapter
- FILE_NAME stores the CSV file name
- file_path combines everything into a full path

Professor note:
This is one of the best changes in the file. It prevents the common beginner error where a program works in one terminal but fails in another because the current working folder changed.

---

## Section 3: normalize_text
This helper function takes any text and returns a cleaned lowercase version.

Why this matters:

- removes extra spaces with strip
- ignores uppercase versus lowercase by using lower

That means a user can type SUZANNE, suzanne, or Suzanne and still get the same result.

This is a small function, but it improves the whole program.

---

## Section 4: File existence check
Before running any searches, the program checks whether the CSV file exists.

If the file is missing, it prints a clear message and stops immediately.

That is excellent defensive programming. A student should understand that strong programs check for likely problems early.

---

## Section 5: search_artist
This function searches the dataset for artist names.

### What it does
- receives the user’s search term
- normalizes the text
- opens the CSV file
- reads rows as dictionaries
- checks both artist_name and artist_name_clean
- stores matching lines in a list
- returns the completed list

### Why this is important
This is a classic search function pattern:

- loop through data
- test a condition
- collect matches
- return results

A first-semester student should be able to explain this function line by line.

---

## Section 6: search_song
This function uses the same overall design as search_artist, but it searches song titles instead of artist names.

That is a valuable lesson: once you understand one search pattern, you can reuse it in other places with only small changes.

Students should notice that the logic stays almost the same:

- create an empty list
- open the file
- loop through each row
- compare the term with one field
- append matches

---

## Section 7: cluster_eras
This is an important intermediate-level function.

Instead of just collecting matching rows, it groups information by cluster.

### Data structure used
The function builds a dictionary named eras_by_cluster.

- key = cluster id
- value = a set of eras

That combination is very powerful.

Why use a set instead of a list?
Because sets automatically remove duplicates.

So if the same era appears many times in one cluster, it is still stored only once.

### What the function teaches
This function introduces grouping, which is a major step up from simple searching.

A student moving toward the end of semester one should pay close attention to this logic.

---

## Section 8: most_songs
This is one of the most important functions in the file.

Its job is to identify which artist has the most song titles matching the search term.

### Key ideas here
The function uses a dictionary where each artist key maps to:

- a display name
- a set of songs

That means the program is not just finding rows. It is organizing and summarizing data.

### Why the set matters again
The set prevents duplicate song titles from being counted more than once.

### Why max is important
After reading the data, the function uses max to find the artist whose song set has the greatest length.

That is a very nice example of comparing collection sizes.

For many first-semester students, this function represents the jump from basic looping to true data processing.

---

## Section 9: two_decades
This is probably the most educational function in the program.

Its purpose is to identify artists that appear in two or more decades.

### How it works
1. It normalizes the search term.
2. It creates a dictionary called artists_by_decade.
3. It loops through every row in the CSV.
4. It checks whether the search term appears in the artist name.
5. If the artist is not yet in the dictionary, it creates a nested record.
6. It adds the row’s decade to a set.
7. After the file is processed, it prints only the artists whose set contains at least two decades.

### Why this matters so much
This function combines:

- dictionaries
- nested dictionaries
- sets
- loops
- conditionals
- sorting
- formatted strings

That is exactly the kind of integrated thinking students need by the end of a first Python course.

---

## Section 10: highest_cluster
This function counts how many songs belong to each cluster.

### Core pattern
- create an empty counting dictionary
- loop through each row
- if the cluster is not in the dictionary yet, start it at 0
- add 1 for every row seen
- use max to find the largest count

This is a counting pattern and is extremely common in programming.

Students should practice writing variations of this idea often.

---

## Section 11: era_songs
This function determines which era contains the most unique songs in the dataset.

Like earlier functions, it uses a dictionary with sets.

- key = era
- value = set of songs

Once the loop finishes, the program finds the era whose set is largest.

This is another strong example of grouping plus counting.

---

## Section 12: main
The main function controls the whole user experience.

### Opening output
It prints a title and instructions.

### The loop
It uses a while True loop so the user can keep searching until they type exit.

### Error handling
The try-except blocks protect the program from input-related errors.

### Menu logic
The user can search by:

- artist
- song
- cluster

The program then calls the appropriate helper functions and prints the results.

This is a very good example of decomposition:

- main handles the menu and user interaction
- helper functions handle the actual data work

That is how larger programs stay readable.

---

## Section 13: main guard
The final lines:

if __name__ == "__main__":
    main()

make sure the program runs only when the file is executed directly.

This is a standard Python pattern and good practice for organized code.

---

## Final professor comments
This is a strong first-semester project because it moves beyond isolated syntax practice and starts solving a real data problem.

If I were emphasizing the most important functions for study, I would rank them like this:

1. two_decades
2. most_songs
3. highest_cluster
4. cluster_eras

These functions show how Python can store, group, and summarize information from a dataset.

The best way to study this file is to trace one search term through the program and watch how each function builds its result step by step.
