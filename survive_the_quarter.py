# Name: Suixin CHEN
# Group: B

# 1. Input:
# Read scenarios from scenarios_B.csv.
# The file uses semicolons as separators and has 14 columns.
# Each row contains an ID, a situation, and three options: A, B, and C.
# Each option has text, a budget change, a reputation change, and feedback.
# Changes are written as integers. Negative numbers mean a decrease.

# 2. Process:
# Display the day number, budget, reputation, situation, and options.
# Ask the player to choose A, B, or C.
# Ask again if the input is invalid.
# Apply the budget and reputation changes. Keep reputation at 100 or below.
# Display feedback and record the move.
# End the game immediately if budget or reputation is zero or below.

# 3. Output:
# Show why the player was fired, or show the final score and title.
# Display the moves with the largest and smallest reputation changes.
# Append the player's name, budget, reputation, title, and date to results.csv.

# 4. Possible problems:
# Invalid choice: ask again until the player enters A, B, or C.
# Budget or reputation reaches zero or below: end the game immediately.

# Extra feature:
# I choose the difficulty feature.
# Easy mode starts with 15000 EUR, and hard mode starts with 6000 EUR.
# This lets players experience different levels of budget pressure.

# Import random to shuffle the scenarios.
import csv
import random
from datetime import date

# Read the scenarios and return them as a list.
def load_scenarios(filename):
    with open(filename, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        scenarios = list(reader)

    return scenarios


# Display the situation and the three choices.
def display_scenario(scenario):
    print("\nSituation:", scenario["Situation"])
    print("A:", scenario["A_Choice"])
    print("B:", scenario["B_Choice"])
    print("C:", scenario["C_Choice"])

# Ask for a valid choice and return it in uppercase.
def get_choice():
    while True:
        choice = input("Choose A, B, or C: ").strip().upper()

        if choice in ("A", "B", "C"):
            return choice

        print("Invalid choice. Please enter A, B, or C.")

# Return the selected option as a tuple.
def get_option(scenario, choice):
    option = (
        scenario[choice + "_Choice"],
        int(scenario[choice + "_Money"]),
        int(scenario[choice + "_Buzz"]),
        scenario[choice + "_Reaction"]
    )
    return option

# Apply the changes and return the updated budget and reputation.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option

    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)

    return budget, reputation

# Return the player's title based on the final status.
def get_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return "Fired"

    score = reputation + budget // 200

    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"

    # Append one game result to the results file.
def save_result(name, budget, reputation, title):
    with open("results.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            budget,
            reputation,
            title,
            date.today().isoformat()
        ])

# Ask for a difficulty and return the starting budget.
def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").strip().lower()

        if difficulty == "easy":
            return 15000
        elif difficulty == "hard":
            return 6000

        print("Invalid difficulty. Please enter easy or hard.")

# Ask for the player's name.
name = input("Enter your name: ").strip()

while not name:
    name = input("Please enter a non-empty name: ").strip()

# Load the scenarios and shuffle their order.
scenarios = load_scenarios("scenarios_B.csv")
random.shuffle(scenarios)

# Set the starting budget based on the chosen difficulty.
budget = choose_difficulty()
reputation = 50

# NEW 1: Create an empty list to store the moves.
history = []

# Play up to ten days using different scenarios.
for day, scenario in enumerate(scenarios[:10], start=1):
    print("\n--- Day", day, "---")
    print("Budget:", budget, "EUR")
    print("Reputation:", reputation)

    # Display the scenario and get the selected option.
    display_scenario(scenario)
    choice = get_choice()
    option = get_option(scenario, choice)

    # Unpack the option and update the player's status.
    text, budget_change, reputation_change, feedback = option
    budget, reputation = apply_choice(budget, reputation, option)

    # NEW 2: Record this move after updating the status.
    history.append(
        (day, scenario["Situation"], choice, reputation_change)
    )

    # Display the feedback and updated status.
    print("\nFeedback:", feedback)
    print("Updated budget:", budget, "EUR")
    print("Updated reputation:", reputation)

    # Stop immediately if either value reaches zero or below.
    if budget <= 0 or reputation <= 0:
        print("\nYou are fired!")

        if budget <= 0:
            print("Reason: Your budget ran out.")

        if reputation <= 0:
            print("Reason: Your reputation reached zero or below.")

        break

else:
    # This runs only if all ten days finish without a break.
    print("\nCongratulations! You survived all 10 days.")

# NEW 3: Show the best and worst moves after the game ends.
if history:
    best_move = max(history, key=lambda move: move[3])
    worst_move = min(history, key=lambda move: move[3])

    print("\nBest move:")
    print("Day:", best_move[0])
    print("Situation:", best_move[1])
    print("Choice:", best_move[2])
    print("Reputation change:", best_move[3])

    print("\nWorst move:")
    print("Day:", worst_move[0])
    print("Situation:", worst_move[1])
    print("Choice:", worst_move[2])
    print("Reputation change:", worst_move[3])

# Display the final status and title.
title = get_title(budget, reputation)

print("\n--- Final Result ---")
print("Final budget:", budget, "EUR")
print("Final reputation:", reputation)
print("Title:", title)

# Calculate and display a score only if the player survived.
if title != "Fired":
    score = reputation + budget // 200
    print("Final score:", score)

# Save the result after the game ends.
save_result(name, budget, reputation, title)
print("\nYour result has been saved to results.csv.")