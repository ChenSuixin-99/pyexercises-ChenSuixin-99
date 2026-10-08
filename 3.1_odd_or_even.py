"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Ask the user for a number N.
# 2. Process:Check each integer starting from 1 up to N. Use modulo % 2 to test odd/even.
# 3. Out:One printed line per number, stating whether the number is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
#    If user enters 0: print a message and stop, do not loop (range 1 to 0 is empty).
#    If user enters negative number: warn user and stop, since we count starting at 1.
#    If user enters 5000: run normally and print all 5000 lines.

# Your code below

N = int(input("Please enter a number N:"))

if N <= 0:
    print("Error: Please enter a positive integer greater than 0.")
else:
    for number in range(1, N+1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")
