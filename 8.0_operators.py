"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# Two strings: "apple" and "Apple".
# The user's prediction for each expression.

# 2. Process:
# Compare the strings using six comparison operators.
# Combine selected comparison results using and, or, and not.
# Collect predictions before displaying the actual results.
# Count how many predictions are correct.

# 3. Out:
# A table showing each expression, prediction, result, and correctness.
# The total number of correct predictions.

# 4. My chosen values and surprising result:
# I chose "apple" and "Apple" to explore case-sensitive comparisons.
# After running, I will describe which result surprised me, or explain
# why none of the results surprised me.

# Your code below

a = "apple"
b = "Apple"

# Store the comparison results.
equal = a == b
not_equal = a != b
greater = a > b
less = a < b
greater_or_equal = a >= b
less_or_equal = a <= b

# Store expressions and their actual results.
checks = [
    ("a == b", equal),
    ("a != b", not_equal),
    ("a > b", greater),
    ("a < b", less),
    ("a >= b", greater_or_equal),
    ("a <= b", less_or_equal),
    ("(a > b) and (a != b)", greater and not_equal),
    ("(a > b) and (a == b)", greater and equal),
    ("(a < b) or (a == b)", less or equal),
    ("(a < b) or (a != b)", less or not_equal),
    ("not (a == b)", not equal),
    ("not (a > b)", not greater)
]

print("Value a:", repr(a))
print("Value b:", repr(b))
print("\nPredict each result before seeing the answers.")

# Collect every prediction before revealing the results.
predictions = []

for expression, result in checks:
    while True:
        answer = input(
            f"{expression} — True or False? "
        ).strip().lower()

        if answer in ("true", "false"):
            predictions.append(answer == "true")
            break

        print("Please enter True or False.")

# Display the results as a readable table.
print()
print(f"{'Expression':<26} {'Prediction':<12} {'Result':<8} {'Correct'}")
print("-" * 58)

correct_count = 0

for (expression, result), prediction in zip(checks, predictions):
    correct = prediction == result

    if correct:
        correct_count += 1

    print(
        f"{expression:<26} "
        f"{str(prediction):<12} "
        f"{str(result):<8} "
        f"{'Yes' if correct else 'No'}"
    )

print(f"\nCorrect predictions: {correct_count}/{len(checks)}")