import random

def depressionFree():
    exercise_tasks = ["Walk", "Run", "Jog", "Bike Ride", "Yoga", "Stretching", "Dancing", "Swimming", "Hiking", "Playing a Sport"]

    home_tasks = ["Laundry", "Dishes", "Vacuuming", "Grocery Shopping", "Cooking", "Cleaning Bathroom", "Mowing Lawn", "Car Maintenance", "Organizing Closet", "Paying Bills"]

    self_care_tasks = ["Meditation", "Journaling", "Reading a Book", "Taking a Bath", "Listening to Music", "Practicing Gratitude", "Spending Time in Nature", "Connecting with Loved Ones", "Engaging in a Hobby", "Seeking Professional Help"]

    professional_tasks = ["Refactoring Code", "Writing Documentation", "Learning a New Programming Language", "Contributing to Open Source", "Attending a Webinar", "Networking with Peers", "Updating Resume", "Applying for Jobs", "Building a Portfolio", "Setting Career Goals"]
    
    all_tasks = exercise_tasks + home_tasks + self_care_tasks + professional_tasks
    random_task = random.choice(all_tasks)

    print(f"How does: {random_task} sound to get you moving and feeling better?")


print("Welcome to your gateway to a depression-free life! Let's find a task to keep you busy and productive.")
print("Remember, staying active and engaged can help improve your mood and overall well-being.")

while True:
    emotions = []

    emotional_state = input("How are you feeling today? ")
    emotions.append(emotional_state.split())

    if emotional_state.lower() == "exit":
        print("Thank you for using the depression-free life gateway. Take care and remember to reach out for support when needed.")
        break
    try: 
        with open("data/emotions.txt", "a") as file:
            for emotion in emotions:
                file.write(" ".join(emotion) + "\n")
    except Exception as e:
        print(f"An error occurred while saving emotions: {e}")
    except FileNotFoundError:
        print("The file path does not exist. Please check the path and try again.")
    except ValueError:
        print("Please enter only text.")
    else:
        print("Thank you for sharing your feelings.")
        if emotional_state.lower() in ["sad", "depressed", "unhappy", "down"]:
            print("I'm sorry to hear, I'm glad you're reaching out and takingsteps to feel better. Remember, it's okay to have bad days. Try todo something small, something like the sun can help take the chillaway.")
        elif emotional_state.lower() in ["happy", "good", "great", "excited"]:
            print(f"I'm so happy to hear you're feeling {emotional_state.lowe()}!")
        else:
            print(f"You're very brave for shaing that you're feeling {emotional_state.lower()}. Life is tough, but you're tougher. The past doesn't define you, and the future is full of possibilities. Never forget that you are strong, capable, and deserving of happiness. Keep pushing forward, and remember that you are not alone. There are people who care about you and want to support you. You can get through this, one day at a time.")
    depressionFree()
