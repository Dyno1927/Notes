# FILE I/O - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers File I/O (Input/Output):

* Reading files
* Writing files
* Appending to files
* with statement (context manager)
* Working with paths (os, pathlib)
* JSON files
* CSV files
* Exception handling with files
"""

import csv
import json
import os

# -------------------------
# WRITING A FILE
# -------------------------

"""
Modes:
  "w"  → write (creates or overwrites)
  "a"  → append (adds to end)
  "r"  → read (default)
  "rb" / "wb" → read/write binary
"""

# Write (creates the file, overwrites if exists)
with open("notes.txt", "w") as f:
    f.write("Line 1: Hello!\n")
    f.write("Line 2: Python is great.\n")

print("File written.")

# Always use 'with' → it automatically closes the file


# -------------------------
# READING A FILE
# -------------------------

# Read entire file as one string
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)


# Read line by line (memory efficient for large files)
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip removes trailing \n


# Read all lines into a list
with open("notes.txt", "r") as f:
    lines = f.readlines()
    print(lines)


# -------------------------
# APPENDING TO A FILE
# -------------------------

with open("notes.txt", "a") as f:
    f.write("Line 3: Appended!\n")

# Verify
with open("notes.txt", "r") as f:
    print(f.read())


# -------------------------
# CHECKING IF FILE EXISTS
# -------------------------

if os.path.exists("notes.txt"):
    print("File exists.")
else:
    print("File not found.")


# -------------------------
# WORKING WITH PATHS
# -------------------------

"""
os.path → classic way
pathlib → modern, recommended way
"""

from pathlib import Path

# Current directory
cwd = Path.cwd()
print(f"Current dir: {cwd}")

# Build a path
filePath = Path("data") / "users.txt"
print(filePath)  # data/users.txt

# Check if exists
print(filePath.exists())

# Create directory
Path("data").mkdir(exist_ok=True)  # no error if already exists

# List files in a directory
for f in Path(".").iterdir():
    print(f)


# -------------------------
# JSON FILES
# -------------------------

"""
JSON = common format for storing structured data.
Python dicts ↔ JSON objects.
"""

# Write JSON
data = {"name": "Khanishk", "age": 16, "skills": ["Python", "C#"]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent makes it readable

print("JSON written.")


# Read JSON
with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded["name"])
print(loaded["skills"])


# -------------------------
# CSV FILES
# -------------------------

"""
CSV = comma-separated values.
Common for spreadsheet data.
"""

# Write CSV
students = [
    ["Name", "Age", "Grade"],
    ["Khanishk", 16, "A"],
    ["Aarav", 17, "B"],
    ["Maya", 18, "A+"],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("CSV written.")


# Read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# -------------------------
# EXCEPTION HANDLING WITH FILES
# -------------------------

"""
Files can fail: not found, permission denied, etc.
Always handle exceptions when working with files.
"""

try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist!")
except PermissionError:
    print("You do not have permission to read this file.")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("File operation attempted.")


# -------------------------
# CLEANUP (remove test files)
# -------------------------

for filename in ["notes.txt", "data.json", "students.csv"]:
    if os.path.exists(filename):
        os.remove(filename)

print("Cleanup done.")


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

Mode     | What it does
-------- | ----------------------------
"r"      | Read (default)
"w"      | Write (overwrites)
"a"      | Append (adds to end)
"rb/wb"  | Binary read/write

- Always use 'with' → auto closes file
- Use json.dump / json.load for JSON
- Use csv.writer / csv.reader for CSV
- Handle FileNotFoundError in try/except
- Use pathlib.Path for modern path handling
"""
