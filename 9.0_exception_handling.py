"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# A number entered by the user as the divisor.
# Enter q to quit.

# 2. Process:
# Convert the input to a float.
# Divide 100 by the number.
# Handle invalid numbers and division by zero separately.
# Allow unlimited attempts until the user enters q.

# 3. Out:
# Display the division result or a specific error message.
# Ask again after both successful and unsuccessful attempts.

# 4. The two failures, and whether they deserve the same message:
# ValueError occurs when the input cannot be converted to a number.
# ZeroDivisionError occurs when the divisor is zero.
# They need different messages because the user must fix different problems.
# Separate handlers explain the exact problem without hiding unrelated bugs.

# Your code below

# Keep asking until the user chooses to quit.
while True:
    user_input = input(
        "\nEnter a number to divide 100 by, or q to quit: "
    ).strip()

    if user_input.lower() == "q":
        print("Goodbye!")
        break

    try:
        number = float(user_input)
        result = 100 / number

    except ValueError:
        print("Invalid input. Please enter a number, such as 4 or 2.5.")

    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero number.")

    else:
        print("100 /", number, "=", result)
