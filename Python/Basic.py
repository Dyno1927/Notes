# PYTHON BASICS - COMPLETE LEARNING FILE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers core Python basics:

* Variables & Data Types
* Strings & f-strings
* Operators
* Conditionals
* Loops
* Functions
* Collections (List, Tuple, Set, Dict)
* String/List methods
* Basic concepts you MUST know

Use this as a reference + revision file.
"""

# -------------------------

# VARIABLES & DATA TYPES

# -------------------------

"""
Python is dynamically typed → no need to declare type
"""

name = "Khanishk"  # str (string)
age = 18  # int (integer)
height = 5.9  # float (decimal)
is_student = True  # bool (boolean)

# type() → check data type

print(type(name))
print(type(age))

# -------------------------

# TYPE CASTING

# -------------------------

"""
Converting one data type to another
"""

num = "100"
num_int = int(num)  # string → int
num_float = float(num)  # string → float

print(num_int + 50)

# -------------------------

# STRINGS

# -------------------------

"""
Strings are immutable → cannot be changed after creation
"""

text = "Hello World"

# Access characters

print(text[0])  # H
print(text[-1])  # d

# Slicing

print(text[0:5])  # Hello

# String methods

print(text.lower())
print(text.upper())
print(text.replace("World", "Python"))
print(text.split(" "))

# -------------------------

# F-STRINGS

# -------------------------

"""
Modern way to format strings
"""

first = "John"
last = "Doe"

full = f"{first} {last}"
print(full)

# Expressions inside f-string

print(f"Next year age: {age + 1}")

# -------------------------

# OPERATORS

# -------------------------

"""
Arithmetic Operators
"""

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # floor division
print(a % b)  # remainder
print(a**b)  # power

"""
Comparison Operators
"""

print(a > b)
print(a == b)
print(a != b)

"""
Logical Operators
"""

print(True and False)
print(True or False)
print(not True)

# -------------------------

# CONDITIONALS

# -------------------------

"""
if, elif, else
"""

x = 20

if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")

# -------------------------

# LOOPS

# -------------------------

"""
For loop
"""

for i in range(5):
    print(i)

"""
While loop
"""

count = 0
while count < 3:
    print(count)
    count += 1

# -------------------------

# FUNCTIONS

# -------------------------

"""
Functions allow reusable code
"""


def greet(name):
    """
    Function that returns greeting message
    """
    return f"Hello {name}"


print(greet("Khanishk"))

"""
Default parameters
"""


def power(base, exp=2):
    return base**exp


print(power(3))
print(power(3, 3))

# -------------------------

# LISTS

# -------------------------

"""
Lists are ordered, mutable collections
"""

nums = [1, 2, 3, 4]

nums.append(5)
nums.remove(2)
nums.sort()

print(nums)

# Loop through list

for n in nums:
    print(n)

# -------------------------

# TUPLES

# -------------------------

"""
Tuples are ordered but immutable
"""

point = (10, 20)

print(point[0])

# -------------------------

# SETS

# -------------------------

"""
Sets are unordered and unique
"""

nums_set = {1, 2, 3, 3}

print(nums_set)  # duplicates removed

nums_set.add(5)
nums_set.remove(1)

# -------------------------

# DICTIONARIES

# -------------------------

"""
Key-value pairs
"""

person = {"name": "Khanishk", "age": 18}

print(person["name"])

person["age"] = 19

for key, value in person.items():
    print(key, value)

# -------------------------

# STRING METHODS (IMPORTANT)

# -------------------------

text = "python"

print(text.capitalize())
print(text.isalpha())
print(text.isdigit())

# -------------------------

# LIST METHODS (IMPORTANT)

# -------------------------

nums = [3, 1, 4]

nums.append(10)
nums.insert(1, 99)
nums.pop()
nums.reverse()

print(nums)

# -------------------------

# INPUT

# -------------------------

"""
Takes input from user (always string)
"""

user_name = input("Enter your name: ")

print(f"Hello {user_name}")

# -------------------------

# BASIC EXCEPTION HANDLING

# -------------------------

"""
Handles errors safely
"""

try:
    x = int("abc")
except ValueError:
    print("Conversion failed")

# -------------------------

# FINAL NOTE

# -------------------------

"""
This is all about the basics of python and 
simple-good-to-know things
"""
