"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# An integer entered by the user.

# 2. Process, function by function:
# is_zero checks whether the number is zero.
# is_positive checks whether the number is positive.
# is_negative checks whether the number is negative.
# is_even checks whether the number is divisible by 2.
# detailed_number determines the sign and parity using the helper functions.

# 3. Out:
# Return a message describing the number's sign and parity.
# Display the returned message on the screen.

# 4. The question my fourth function answers:
# Is the number positive, negative, or zero, and is it even or odd?
# Small functions make each condition easier to test independently.


# Your code below6
def check(number):
    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative")
    else:
        print("The number is zero")

num = int(input("Enter a number: "))
check(num)

def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0

def is_zero(num):
    return num == 0

def is_even(num):
    return num % 2 == 0

def detailed_number(num):
    if is_zero(num):
        sign = "zero"
    elif is_positive(num):
        sign = "positive"
    else:
        sign = "negative"
    if is_even(num):
        parity = "even"
    else:
        parity = "odd"
    return f"The number is {sign} and {parity}."

num = int(input("Enter a number: "))
print(detailed_number(num))