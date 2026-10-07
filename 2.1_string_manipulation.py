"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Ask the user for a sentence, then display it
# 2. Process:transformate the sentence into upper case in lower case with the number of characters it contains and with the first and last word
# 3. Out:Four modified versions of the original sentence, printed one after another.
# 4. My four transformations, and when each is useful:
#    upper(): Useful for making titles or verification codes.
#    lower(): Useful when comparing text without worrying about capitalisation.
#    strip(): Useful to clean extra spaces users accidentally type at start or end.
#    split(): Splits a string into a list, using spaces by default


# Your code below
sentence = input("Please enter a sentence: ")

trans_upper = sentence.upper()
trans_lower = sentence.lower()
trans_strip = sentence.strip()
trans_split = sentence.split()

print("1. All uppercase:", trans_upper)
print("2. All lowercase:", trans_lower)
print("3. Strip leading/trailing spaces:", trans_strip)
print("4. Splits a string into a list:", trans_split)