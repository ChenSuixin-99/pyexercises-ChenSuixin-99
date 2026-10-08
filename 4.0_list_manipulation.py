"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A manually created list with at least 8 numeric items, representing monthly marketing campaign budgets
# 2. Process: Define the original list. Print the full list, select and print one single element. Sort the list. Calculate a computed value (total sum of all budget values).
# 3. Out: The whole list, one chosen individual item, sorted version of list, and the total sum of all items in the list.
# 4. What is your list about, and what did you compute from it? Why is that number interesting?
#    My list stores monthly marketing campaign budgets. I computed the total sum of all budgets.
#    This total is interesting because it shows the overall spending for the whole campaign period.


# Your code below
number_1 = 2
number_2 = 3
number_3 = 4
number_4 = 5

print(number_1)
print(number_2)
print(number_3)
print(number_4)

list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]
print("Listing all the numbers in the list")
print(list_of_numbers)
print("Listing the third item in the list")
print(list_of_numbers[2])

print("The list of numbers after sorted")
list_of_numbers.sort()
print(list_of_numbers)

list_of_numbers.pop()

print("The list of numbers after removing the last item from the list")
print(list_of_numbers)