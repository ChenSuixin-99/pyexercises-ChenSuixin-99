"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A dictionary describing a marketing customer, with at least five key-value fields
# 2. Process: Create the dictionary. Read and display it. Add one new field. Remove one field. Print all fields and values. Add error handling for accessing a non-existent key.
# 3. Out: The original dictionary, dictionary after adding a new field, dictionary after removing one field, and the value of the removed field.
# 4. My object, my five fields, and why those:
#    The object is a customer profile for marketing analysis.
#    The five fields are "name", "age", "city", "occupation", "email".
#    These fields are useful because marketers need customer name, age, location, job and contact to build customer segments and run targeted campaigns.


# Your code below

name = "ChenSuixin"
age = 24
city = "Paris"

person ={"name":"ChenSuixin", 
         "age": 24, 
         "city": "Paris"}

print("The dictionary is :", person)
person["occupation"] = "Engineer"

print("The dictionary after adding the occupation:", person)

city = person.pop("city")

print("The dictionary after removing the city:", person)
print("The city removed is ", city)
