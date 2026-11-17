"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# First name, last name, student ID, and email.

# 2. Process:
# Validate the first and last names separately.
# Combine them into one full name.
# Validate the student ID and email.
# Save only after all inputs are acceptable.

# 3. Out:
# Append one record to validated_students.csv.
# Columns: Full name, Student ID, Email.

# 4. Fields and acceptance rules:
# Full name combines the separately entered first and last names.
# First name: one uppercase English letter followed by zero or more
# lowercase English letters. Spaces and hyphens are not accepted.
# Last name: one or more uppercase English letters only.
# Student ID: exactly six digits from 0 to 9; leading zeros are allowed.
# Email: one or more English letters, digits, or underscores,
# followed by the exact, case-sensitive suffix @school.edu.
# Surrounding whitespace is removed before validation.

# Your code below
import csv
import re
from pathlib import Path


# [A-Z] matches one uppercase English letter.
# [a-z]* matches zero or more lowercase English letters.
FIRST_NAME_PATTERN = r"[A-Z][a-z]*"

# [A-Z]+ matches one or more uppercase English letters.
LAST_NAME_PATTERN = r"[A-Z]+"

# [0-9]{6} matches exactly six digits.
STUDENT_ID_PATTERN = r"[0-9]{6}"

EMAIL_PATTERN = r"[A-Za-z0-9_]+@school\.edu"


# Match the entire value against the pattern.
def is_valid(pattern, value):
    return re.fullmatch(pattern, value) is not None


# Validate both parts of the full name.
def is_valid_full_name(first_name, last_name):
    return (
        is_valid(FIRST_NAME_PATTERN, first_name)
        and is_valid(LAST_NAME_PATTERN, last_name)
    )


# Ask until the user enters an acceptable value.
def get_valid_input(prompt, pattern, error_message):
    while True:
        value = input(prompt).strip()

        if is_valid(pattern, value):
            return value

        print(error_message)


# Full name tests: one must pass and two must fail.
assert is_valid_full_name("Suixin", "CHEN")
assert not is_valid_full_name("suixin", "CHEN")
assert not is_valid_full_name("Suixin", "Chen")

# Student ID tests: one must pass and two must fail.
assert is_valid(STUDENT_ID_PATTERN, "012345")
assert not is_valid(STUDENT_ID_PATTERN, "12345")
assert not is_valid(STUDENT_ID_PATTERN, "12A456")

# Email tests: one must pass and two must fail.
assert is_valid(EMAIL_PATTERN, "suixin_1@school.edu")
assert not is_valid(EMAIL_PATTERN, "sui.xin@school.edu")
assert not is_valid(EMAIL_PATTERN, "suixin@School.edu")

print("All nine validation tests passed.")


# Collect and validate the two parts of the full name.
first_name = get_valid_input(
    "\nFirst name: ",
    FIRST_NAME_PATTERN,
    "Use an uppercase first letter followed by lowercase letters."
)

last_name = get_valid_input(
    "Last name: ",
    LAST_NAME_PATTERN,
    "Use uppercase English letters only."
)

full_name = first_name + " " + last_name

# Keep the ID as text to preserve leading zeros.
student_id = get_valid_input(
    "Student ID: ",
    STUDENT_ID_PATTERN,
    "Enter exactly 6 digits."
)

email = get_valid_input(
    "Email: ",
    EMAIL_PATTERN,
    "Use letters, digits, or underscores before the exact suffix @school.edu."
)


# Save only after every input has passed validation.
file_path = Path("validated_students.csv")
needs_header = (
    not file_path.exists()
    or file_path.stat().st_size == 0
)

with open(file_path, "a", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    if needs_header:
        writer.writerow(["Full name", "Student ID", "Email"])

    writer.writerow([full_name, student_id, email])

print("Data saved successfully!")
