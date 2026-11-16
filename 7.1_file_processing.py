"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -
# -
# -
# -

# 1. In:
# names.txt contains ten lines, including eight names and two blank lines.

# 2. Process, problem by problem:
# Remove extra spaces by splitting and joining each line.
# Skip blank lines.
# Standardize the capitalization of names.
# Keep the surname prefix "van" lowercase in "van Rossum".
# Sort names by the complete surname, ignoring capitalization.

# 3. Out:
# Write eight cleaned names to names_cleaned.txt.
# Leave names.txt unchanged.

# 4. How I decide which word is the last name:
# This file uses given-name-first order.
# For two-word names, the second word is the surname.
# For Guido van Rossum, the complete surname is "van Rossum".
# I sort this surname under V, including its prefix.

# Your code below

from pathlib import Path

# Clean spacing and capitalization.
def clean_name(line):
    words = line.split()

    if not words:
        return ""

    words = [word.capitalize() for word in words]

    # Preserve the spelling of the compound surname in this file.
    if len(words) >= 3 and words[-2:] == ["Van", "Rossum"]:
        words[-2] = "van"

    return " ".join(words)


# Return the complete surname used for sorting.
def get_surname(name):
    words = name.split()

    if words[-2:] == ["van", "Rossum"]:
        return "van Rossum".casefold()

    return words[-1].casefold()


# Locate the input and output beside this Python file.
input_path = Path(__file__).resolve().parent / "names.txt"
output_path = input_path.with_name("names_cleaned.txt")

# Read the original file.
with open(input_path, "r", encoding="utf-8-sig") as file:
    original_lines = file.readlines()

# Clean names and remove blank lines.
cleaned_names = []
blank_count = 0

for line in original_lines:
    name = clean_name(line)

    if name:
        cleaned_names.append(name)
    else:
        blank_count += 1

# Sort the cleaned names by surname.
cleaned_names.sort(key=get_surname)

# Save to a new file without changing the original.
with open(output_path, "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")

# Display the results for checking.
print("Original lines:", len(original_lines))
print("Blank lines removed:", blank_count)
print("Output names:", len(cleaned_names))

print("\nSorted names:")
for name in cleaned_names:
    print(name)

print("\nSaved to:", output_path)