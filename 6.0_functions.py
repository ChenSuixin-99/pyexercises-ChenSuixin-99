"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# A list of monthly marketing campaign budgets.

# 2. Process:
# Add all the budget values together.

# 3. Out:
# Return the total budget as a number.

# 4. My function name, and why return rather than print:
# calculate_total_budget clearly describes the calculation.
# return allows the result to be stored and used in later calculations.
# print only displays the result on the screen.

# Your code below
# 1. In:
# The user enters monthly marketing budgets in EUR, separated by spaces.

# 2. Process:
# Convert the input into a list of numbers and add them together.

# 3. Out:
# Return the total budget as a number.

# 4. My function name, and why return rather than print:
# calculate_total_budget clearly describes what the function does.
# return allows the result to be stored and used later.
# print only displays the result.


# Calculate and return the total budget.
def calculate_total_budget(budgets):
    return sum(budgets)


# Ask for three different lists and display their totals.
for i in range(3):
    print("\nBudget list", i + 1)

    user_input = input("Enter budgets in EUR, separated by spaces: ")
    budgets = [float(value) for value in user_input.split()]

    total = calculate_total_budget(budgets)

    print("Your list:", budgets)
    print("Total budget:", total, "EUR")


# Check the function with an empty list.
# Returning 0 is acceptable because there are no budget entries.
print("\nEmpty list total:", calculate_total_budget([]))