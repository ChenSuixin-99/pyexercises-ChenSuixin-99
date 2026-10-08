"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The original list created in exercise 4.0
# 2. Process:Produce four views: original, reversed copy, ascending sorted copy, descending sorted copy.
# 3. Out:Print original, reversed list, sorted smallest first, sorted largest first. Finally print original again.
# 4. My four orders, and which ones modify the original:
#    Original list: unchanged.
#    Reversed: list[::-1] creates a new list; original not modified.
#    Sorted smallest first: sorted() returns new list; original not modified.
#    Sorted largest first: sorted(..., reverse=True) returns new list; original not modified.

# Your code below
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

print("Original list:", list_of_numbers)

reversed_list = list_of_numbers[::-1]
print("Reversed list:", reversed_list)

sorted_asc = sorted(list_of_numbers)
print("Sorted, smallest first:", sorted_asc)

sorted_desc = sorted(list_of_numbers, reverse=True)
print("Sorted, largest first:", sorted_desc)

print("Original list at end:", list_of_numbers)