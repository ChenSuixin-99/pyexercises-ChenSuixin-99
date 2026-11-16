"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: The user's first name, last name, date of birth, and student number.
# 2. Process:Append one student record without overwriting previous entries.
# 3. Out, file name and columns:
# File: student_data.csv
# Columns: First Name, Last Name, Date of Birth, Student Number.
# 4. Why these columns, and what this file is for:
# Names identify students, and student numbers distinguish their records.
# Date of birth supports age-based summaries.

# Your code below
import csv
from pathlib import Path
from datetime import datetime, date

def get_required_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")

print("Please fill in the following details")
first_name = input("First Name: ")
last_name = input("Last Name: ")
while True:
    birth = input("Date of Birth (DD/MM/YYYY): ").strip()

    try:
        birth_date = datetime.strptime(birth, "%d/%m/%Y").date()

        if birth_date > date.today():
            print("Date of birth cannot be in the future.")
            continue
        birth = birth_date.strftime("%d/%m/%Y")
        break

    except ValueError:
        print("Please enter a valid date, for example 15/06/2000.")

student_number = input("Student Number: ")

file_path = Path("student_data.csv")
needs_header = (
    not file_path.exists()
    or file_path.stat().st_size == 0
)

with open(file_path, "a", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    # Write the header only when needed.
    if needs_header:
        writer.writerow([
            "First Name",
            "Last Name",
            "Date of Birth",
            "Student Number"
        ])

    # Always append the new student record.
    writer.writerow([
        first_name,
        last_name,
        birth,
        student_number
    ])

print("Data saved successfully!")