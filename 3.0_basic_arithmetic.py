"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numeric values input by the user, converted to float
# 2. Process: Read two numbers. Calculate addition, subtraction, multiplication. For division, check if the second number is zero. If not zero, compute division; if zero, skip division calculation and print warning message.
# 3. Out: Print sum, difference, product. Print division result only when second number is not zero; otherwise print a zero warning message.
# 4. What happens when the second number is zero, and why: The program will print a warning message instead of calculating division. Division by zero is mathematically undefined and causes an error in Python, so we add an if condition to avoid crashing.


# Your code below
number_1 = float(input("Enter the first number:"))
number_2 = float(input("Enter the second number:"))

# adding the two numbers
sum = number_1 + number_2

print("The sum of two numbers is:", sum)

difference = number_1 - number_2
print("The differnce of the numbers is:", difference)

product = number_1 * number_2
print("The product of the numbers is:", product)

if number_2 != 0:
    division = number_1 / number_2
    print("The division of the numbers is:", division)
else:
    print("The number you entered is zero")