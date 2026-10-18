# PYTHON BASICS - ADVANCED COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This is an advanced Python basics reference file.

Covers:

* All major data types
* Most commonly used built-in methods
* Practical usage patterns
* Clean examples with comments

NOTE:
This is NOT every single method in Python,
but it includes almost everything you will actually use.
"""

# -------------------------

# STRINGS

# -------------------------

"""
Strings are immutable sequences of characters.
"""

text = "hello world"

# Case methods

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

# Searching

print(text.find("world"))  # index or -1
print(text.index("hello"))  # error if not found

# Checking

print(text.startswith("he"))
print(text.endswith("ld"))
print(text.isalpha())
print(text.isalnum())
print(text.islower())
print(text.isupper())

# Replace & split

print(text.replace("world", "python"))
print(text.split(" "))  # returns list
print("-".join(["a", "b", "c"]))

# Stripping

msg = "   hi   "
print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())

# Formatting

name = "Khanishk"
age = 18
print(f"My name is {name} and I am {age}")

# -------------------------

# LISTS

# -------------------------

"""
Lists are ordered, mutable collections.
"""

nums = [1, 2, 3]

# Adding

nums.append(4)
nums.extend([5, 6])
nums.insert(1, 99)

# Removing

nums.remove(99)
nums.pop()  # last element
nums.pop(0)  # by index
nums.clear()

# Recreate for more examples

nums = [3, 1, 4, 2]

# Sorting

nums.sort()
nums.sort(reverse=True)

# Copying

copyNums = nums.copy()

# Info

print(len(nums))
print(nums.count(2))
print(nums.index(4))

# Reverse

nums.reverse()

# Loop

for n in nums:
    print(n)

# -------------------------

# TUPLES

# -------------------------

"""
Tuples are immutable.
"""

t = (1, 2, 3, 2)

print(t.count(2))
print(t.index(3))

# -------------------------

# SETS

# -------------------------

"""
Sets are unordered and unique.
"""

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Add/remove

s1.add(10)
s1.remove(1)
s1.discard(100)  # no error if not found

# Set operations

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

# Checks

print(s1.issubset(s2))
print(s1.issuperset(s2))

# Clear

s1.clear()

# -------------------------

# DICTIONARIES

# -------------------------

"""
Key-value pairs.
"""

person = {"name": "Khanishk", "age": 18}

# Access

print(person["name"])
print(person.get("age"))
print(person.get("city", "Not Found"))

# Add/update

person["city"] = "Aligarh"
person.update({"age": 19})

# Remove

person.pop("age")
person.popitem()
person.clear()

# Recreate

person = {"name": "Khanishk", "age": 18}

# Views

print(person.keys())
print(person.values())
print(person.items())

# Loop

for k, v in person.items():
    print(k, v)

# -------------------------

# NUMBERS (int, float)

# -------------------------

"""
Basic numeric operations and functions.
"""

x = 10
y = 3

print(abs(-10))
print(round(3.567, 2))
print(pow(2, 3))

# Division

print(x / y)
print(x // y)

# -------------------------

# BOOLEAN

# -------------------------

"""
True / False values.
"""

print(bool(0))
print(bool("text"))

# -------------------------

# BUILT-IN FUNCTIONS

# -------------------------

"""
Common built-ins used everywhere.
"""

nums = [1, 5, 3]

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sorted(nums))

# enumerate

for i, val in enumerate(nums):
    print(i, val)

# zip

names = ["A", "B"]
scores = [90, 80]

for n, s in zip(names, scores):
    print(n, s)

# -------------------------

# TYPE CHECKING

# -------------------------

"""
Check data types properly.
"""

print(isinstance(10, int))
print(isinstance("hi", str))

# -------------------------

# STRING ADVANCED METHODS

# -------------------------

text = "python123"

print(text.isdigit())
print(text.isnumeric())
print(text.isidentifier())

# -------------------------

# LIST COMPREHENSION

# -------------------------

"""
Short way to create lists.
"""

squares = [x**2 for x in range(5)]
print(squares)

# -------------------------

# LAMBDA (ANONYMOUS FUNCTION)

# -------------------------

square = lambda x: x * x
print(square(5))

# -------------------------

# FINAL NOTE

# -------------------------

"""
If you understand this file well:

You now know:

* Core Python syntax
* All major data structures
* Most important methods
* Functional basics
 """

"""
These methods below are some methods that are
edge-case meaning they will be used rarely but
can come handy
"""

text = "hello world"

# Alignment
print(text.center(20))
print(text.ljust(20))
print(text.rjust(20))

# Counting
print(text.count("l"))

# Case-insensitive comparison helper
print(text.casefold())

# Tabs expansion
print("hello\tworld".expandtabs(4))

# Formatting (older way)
print("My name is {}".format("Khanishk"))

# Checks
print("123".isdecimal())
print("abc123".isalnum())
print("   ".isspace())

# Prefix/suffix removal (modern & useful 🔥)
print("unhappy".removeprefix("un"))
print("file.txt".removesuffix(".txt"))

# Partition (splits into 3 parts)
print("a-b-c".partition("-"))

# Encoding (advanced)
print(b"hello")
