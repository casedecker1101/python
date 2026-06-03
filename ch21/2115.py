# Functions for god knows what.
import random

from datetime import date, datetime
def dateReturn(datetime):
    return datetime.date()

def timeReturn(datetime):
    return datetime.time()

def oneWord(word):
    return word.strip().upper()

word_storage = ["Great job!", "Keep it up!", "You can do it!", "Don't give up!", "Believe in yourself!", "Stay positive!", "You are amazing!", "Never stop learning!", "Success is near!", "You got this!"]

print("Motivation and Discipline are the keys to success!:")



while True:
    user_input = input("Enter 'exit' to quit or press Enter to continue: ")
    if user_input.lower() == "exit":
        break
    else:    
        words = random.choice(word_storage)
        if datetime.now().hour < 12:
            print(f"Good morning! {words}")
        elif datetime.now().hour < 18:
            print(f"Good afternoon! {words}")
        else:
            print(f"Good Evening! {words}")
        print("Todays date is: " + str(dateReturn(datetime.now())))
        print("The current time is: " + str (timeReturn(datetime.now())))
        # random generator selects a word from the list and print it out
        print("Todays random word of the day is: " + oneWord(words))

        print("Have a nice day!")
    
    