import random

inventory = ["Rusty Sword", "Health Potion"]
def explore_cave():
    encounters = [
        "You encounter a wild potato monster! It looks hungry.",
        "You find a hidden stash of gold coins.",
        "A trap is triggered! You take some damage.",
        "You discover a secret passage leading to a treasure room.",
        "You meet a lost adventurer who offers to join your party."
    ]
    return encounters

def check_inventory():
    print("Your inventory contains:")
    for item in inventory:
        print(f" - {item}")

def rest():
    print("You take a moment to rest and recover your strength.")
    print("Your health is fully restored.")
    print(random.choice(explore_cave()))

# A M.U.D (Multi-User Dungeon) In Python
def start_game():
    print("Welcome to Baklava! A multi-user dungeon game in Python.")
    print("You find yourself in the entrance of a mysterious cave.")
    print("It randomly generates different challenges and encounters as you explore.")
    while True:
        print("\nWhat would you like to do next?")
        print("1. Explore the cave")
        print("2. Check inventory")
        print("3. Rest")
        print("4. Exit game")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            print(random.choice(explore_cave()))
        elif choice == "2":
            check_inventory()
        elif choice == "3":
            rest()
        elif choice == "4":
            print("Thank you for playing Baklava! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
