# COMPREHENSIONS - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers comprehensions:

* List comprehension
* Dictionary comprehension
* Set comprehension
* Generator expression
* Nested comprehensions

Comprehensions are a SHORT, READABLE way to build collections.
"""

# -------------------------
# LIST COMPREHENSION
# -------------------------

"""
Syntax:
  [expression for item in iterable]
  [expression for item in iterable if condition]
"""

# Normal way:
squares = []
for x in range(1, 6):
    squares.append(x**2)

# Comprehension way:
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


# With condition (filter)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]


# Transformation
names = ["khanishk", "aarav", "maya"]
upperNames = [name.upper() for name in names]
print(upperNames)


# Combined: filter + transform
longNames = [name.title() for name in names if len(name) > 4]
print(longNames)


# -------------------------
# DICTIONARY COMPREHENSION
# -------------------------

"""
Syntax:
  {key: value for item in iterable}
"""

# Squares as a dict
squareDict = {x: x**2 for x in range(1, 6)}
print(squareDict)  # {1: 1, 2: 4, 3: 9, ...}


# Flip a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in original.items()}
print(flipped)  # {1: 'a', 2: 'b', 3: 'c'}


# From two lists
keys = ["name", "age", "city"]
values = ["Khanishk", 16, "Aligarh"]
profile = {k: v for k, v in zip(keys, values)}
print(profile)


# With condition
scores = {"Khanishk": 88, "Aarav": 55, "Maya": 92}
passed = {name: score for name, score in scores.items() if score >= 60}
print(passed)


# -------------------------
# SET COMPREHENSION
# -------------------------

"""
Syntax:
  {expression for item in iterable}
  (same as list but with {} — gives unique values)
"""

nums = [1, 2, 2, 3, 3, 3, 4]
uniqueSquares = {x**2 for x in nums}
print(uniqueSquares)  # no duplicates


# -------------------------
# GENERATOR EXPRESSION
# -------------------------

"""
Syntax:
  (expression for item in iterable)

Like list comprehension but:
- Uses () not []
- Does NOT build the whole list in memory
- Generates values ONE AT A TIME (lazy)
- Better for large data
"""

gen = (x**2 for x in range(1, 6))
print(gen)  # <generator object>
print(next(gen))  # 1
print(next(gen))  # 4

# Can loop through it
gen2 = (x**2 for x in range(1, 6))
for val in gen2:
    print(val)

# Use sum() with generator (memory efficient)
total = sum(x**2 for x in range(1, 1001))
print(total)


# -------------------------
# NESTED COMPREHENSION
# -------------------------

"""
A comprehension inside another comprehension.
Good for working with 2D data (grids, matrices).
"""

# 3x3 multiplication table as nested list
matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
for row in matrix:
    print(row)


# Flatten a 2D list into 1D
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in grid for num in row]
print(flat)


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

Type          | Syntax          | Result
-----------   | --------------- | -------
List          | [x for x in y]  | list
Dict          | {k:v for ...}   | dict
Set           | {x for x in y}  | set (unique)
Generator     | (x for x in y)  | lazy iterator

- Add if condition to FILTER
- Nest for loops for 2D structures
- Use generator for large data to save memory
"""
