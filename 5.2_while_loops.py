"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:User text input, repeatedly asked to type "yes".
# 2. Process:Use while loop to keep prompting user.
#   Count each attempt. Stop either when user enters "yes" OR when max attempts reached (safety limit).
# 3. Out:A final summary message showing total number of tries, whether user succeeded or hit the attempt limit.
# 4. My stop condition:normalized input equals "yes". 
#    My attempt limit: 5 tries maximum.
#    My summary: prints total attempts and tells user if they answered correctly or ran out of attempts.


# Your code below

i = 0
while i < 5:
    user_input = input("Please enter the word yes: ")
    i = i + 1

    cleaned_answer = user_input.strip().lower()

    if cleaned_answer == "yes":
        break

print("Total attempts:", i)
if cleaned_answer == "yes":
    print("Success! You typed yes correctly.")
else:
    print("You have used all 5 attempts, program stopped.")


