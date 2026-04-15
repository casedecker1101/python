# Professor-Style Walkthrough for 194a.py

## Big Picture
This program is a beginner-friendly music search tool. It reads a CSV dataset of songs, artists, years, and decades, then lets the user type a search request. The program responds by searching for artists, songs, first-entry data, and whether an artist appears across multiple decades.

Think of the program as having four jobs:

1. Find the data file safely.
2. Open the CSV file and read rows as dictionaries.
3. Search through the rows using helper functions.
4. Run an input loop so the user can keep searching until they quit.

---

## Line-by-Line Walkthrough

### Opening comments
The first block of comments is a planning section. These lines act like a mini outline for the assignment. They show what the program is supposed to do before the actual code begins.

This is a good student habit because it turns a large problem into smaller parts.

---

### Imports
The program imports the CSV module and the Path class.

- CSV lets Python read comma-separated values like a spreadsheet.
- Path helps build file locations safely.

This is stronger than hardcoding a fragile file location.

---

### File setup variables
The program creates several variables:

- BASE_DIR means the folder where the script lives.
- DATA_DIR means the data folder inside that chapter.
- file_name stores the CSV file name.
- file_path joins the folder and file name into one full path.

Why this matters:
A lot of beginners write a plain relative path and it works only sometimes. This version is safer because it always starts from the script’s real location.

---

### File existence check
Before doing any searching, the program checks whether the CSV file exists.

If the file is missing:

- it prints a message
- it stops the program immediately

This is an example of defensive programming. The programmer checks for a problem early instead of letting the program crash later with a confusing error.

---

## Function Walkthroughs

### search_artist
This function receives a search word called term.

Step by step:

1. It creates an empty list called matches.
2. It opens the CSV file.
3. CSV DictReader turns each row into a dictionary.
4. For every row, it pulls out artist_name and artist_name_clean.
5. It compares the search word to both versions of the artist’s name.
6. If a match is found, it adds a formatted sentence to the list.
7. At the end, it returns all matches.

Important beginner idea:
This is a search pattern you will use often.

- open a file
- loop through rows
- test a condition
- collect matching results
- return the list

Why lowercasing is used:
Lowercasing makes the search case-insensitive, so Adele and adele behave the same.

---

### search_song
This function is almost the same pattern as search_artist, but it checks the song title instead of the artist.

That is a good example of code reuse through structure. The student is repeating a familiar pattern with a different field from the CSV.

What to notice:

- matches is still the collection list
- the loop still uses DictReader
- the if statement now tests track_name
- the function still returns a list of formatted answers

This reinforces how powerful loops and conditionals become once you understand them.

---

### search_first
This function searches the first_entry column.

Conceptually it works just like the earlier searches:

- open the file
- read each row
- examine one column
- collect results

This is useful for first-semester students because it shows that once you know the pattern, you can search any column in the file with only small changes.

---

### two_decades
This is the most advanced function in the file and deserves extra attention.

Its purpose is not just to find one match. Instead, it groups information by artist and keeps track of which decades that artist appears in.

#### Core ideas inside this function

##### 1. Dictionary storage
The variable artist_decades is a dictionary.

Each key is a cleaned-up artist name.
Each value is another dictionary containing:

- a display name
- a set of decades

This is called a nested data structure.

##### 2. Lowercasing once
The line that stores term_lower is efficient. Instead of calling lower again and again on the same search term, the program computes it once.

##### 3. Reading every row
The program loops through the CSV one row at a time.

For each row it checks whether the search term appears in either:

- the normal artist name
- the cleaned artist name

##### 4. Normalization
The line that builds normalized_name removes non-letter and non-number characters.

This is a more advanced beginner technique. It helps compare names that may be written slightly differently in the dataset.

Example:
A name with punctuation or spacing differences can still be grouped under one clean key.

##### 5. Using a set
The decades are stored in a set, not a list.

That matters because a set automatically prevents duplicates.
If an artist appears ten times in the 1980s, the set still stores the 1980s only once.

That makes the final count of decades accurate.

##### 6. Final filtering
After all rows are processed, the function loops through the stored artist data.

It sorts the decades for a cleaner display, then checks whether the artist appears in more than two decades.
If yes, it builds a summary sentence and adds it to the results.

This is a great end-of-semester function because it combines:

- dictionaries
- nested dictionaries
- sets
- loops
- string methods
- conditional logic
- formatted output

---

### most_songs
This function searches songs using the term provided by the user.

What it currently does:

- opens the CSV file
- loops through every row
- checks whether the term appears in the track name
- stores matching song lines in a list
- returns the list

A professor note:
The function name suggests it might identify the artist with the most songs, but the current version mainly returns matching song entries. That means the name is a little more ambitious than the behavior.

This is normal in student code. A function can start simple and later grow into its full intended purpose.

---

## Main Program Flow

### Welcome messages
The two print statements introduce the program and explain how to quit.

This is part of user experience. Even a simple console program should tell the user what to do.

---

### Infinite loop with while True
The main interaction happens inside a while True loop.

That means the program keeps running until something causes a break.

This is a classic menu-driven program structure.

---

### try and except around input
The program protects the input call with try and except EOFError.

This is good defensive coding. It prevents the program from crashing if the input stream closes unexpectedly.

For a beginner, the key idea is:

- try means attempt this risky code
- except means handle the problem gracefully if something goes wrong

---

### Exit logic
If the user types exit, the loop breaks and the program ends.

This is the clean stopping condition.

---

### Search branch
If the user types search, the program asks for a search term.

Then it calls four helper functions:

- search_artist
- most_songs
- search_first
- two_decades

This is a strong design choice because the main loop stays readable while the detailed work is handled by separate functions.

That is exactly the kind of modular thinking students should practice near the end of a first Python course.

---

### Printing results
The program checks each returned list.

- If artist matches exist, it prints them.
- If decade results exist too, it prints those afterward.
- If there were no artist matches but song matches exist, it prints song matches.
- If there were no song matches but first-entry matches exist, it prints those.
- If none exist, it prints No matches found.

This is a chain of decision making using if, elif, and else.

A student should notice that the order matters. Python checks these branches from top to bottom.

---

## Most Important First-Semester Lessons in This Program

### 1. Functions break big problems into small ones
Each function has one main responsibility.

### 2. Files can be searched row by row
CSV DictReader is an excellent tool when working with spreadsheets.

### 3. Strings are often cleaned before comparison
Using lower helps make searches more flexible.

### 4. Dictionaries and sets are powerful
The two_decades function is a very good example of grouping and counting information.

### 5. Loops and conditions drive almost everything
The program repeatedly reads, tests, stores, and prints.

### 6. Good programs fail safely
The file check and the try-except blocks are important real-world habits.

---

## Professor Summary
This is a solid late-first-semester program because it goes beyond simple print statements and arithmetic. It introduces data files, structured searching, nested storage, and user interaction.

If I were teaching this in class, I would say the most important function to study carefully is two_decades, because it shows how Python can organize real data in a meaningful way.

The easiest way to master this file is:

1. Read one function at a time.
2. Say out loud what each loop is doing.
3. Trace one sample row through the code.
4. Watch how the data structure changes after each match.

That is how you move from beginner syntax to actual programming thinking.
