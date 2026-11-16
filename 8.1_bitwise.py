"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In:
# Four permission flags: READ, WRITE, EXEC, and DELETE.
# The user initially has READ and WRITE permissions.

# 2. Process:
# Combine READ and WRITE using bitwise OR.
# Check for EXEC using bitwise AND.
# Add EXEC using OR, then remove WRITE using AND and NOT.

# 3. Out:
# Display permissions as decimal and four-digit binary values.
# Display whether EXEC is present before and after the change.

# 4. Expected result:
# The final value is 5, or 0101 in binary.
# This represents READ and EXEC permissions.

# Your code below
# Define one bit for each permission.
READ = 1 << 0       # 0001
WRITE = 1 << 1      # 0010
EXEC = 1 << 2       # 0100
DELETE = 1 << 3     # 1000

# Combine the initial permissions.
user_permissions = READ | WRITE

print("Initial permissions:", user_permissions)
print("Initial binary:", format(user_permissions, "04b"))

# Check EXEC before changing the permissions.
has_exec = (user_permissions & EXEC) != 0
print("Has EXEC before change:", has_exec)

# Add EXEC and remove WRITE.
user_permissions = (user_permissions | EXEC) & ~WRITE

print("\nFinal permissions:", user_permissions)
print("Final binary:", format(user_permissions, "04b"))

# Check the updated permissions.
has_exec = (user_permissions & EXEC) != 0
print("Has EXEC after change:", has_exec)

# Display each final permission in a table.
print(f"\n{'Permission':<12} {'Enabled'}")

for name, flag in [
    ("READ", READ),
    ("WRITE", WRITE),
    ("EXEC", EXEC),
    ("DELETE", DELETE)
]:
    enabled = (user_permissions & flag) != 0
    print(f"{name:<12} {enabled}")