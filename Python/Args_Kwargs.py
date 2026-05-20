# *args & **kwargs - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers *args and **kwargs:

* *args  → variable number of positional arguments (tuple)
* **kwargs → variable number of keyword arguments (dict)

Use them when you don't know in advance
how many arguments a function will receive.
"""

# -------------------------
# *args (positional)
# -------------------------

"""
*args packs all extra positional arguments into a TUPLE
"""

def add(*args):
    """
    Can accept any number of numbers
    """
    total = 0
    for n in args:
        total += n
    return total

print(add(1, 2))           # 3
print(add(1, 2, 3, 4, 5))  # 15


def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Khanishk", "Aarav", "Maya")


# -------------------------
# **kwargs (keyword)
# -------------------------

"""
**kwargs packs all extra keyword arguments into a DICT
"""

def show_info(**kwargs):
    """
    Can accept any named arguments
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Khanishk", age=16, city="Aligarh")


# -------------------------
# COMBINING: normal + *args + **kwargs
# -------------------------

"""
ORDER MATTERS:
  1. normal params first
  2. *args second
  3. **kwargs last
"""

def profile(name, *hobbies, **details):
    print(f"Name: {name}")
    print(f"Hobbies: {hobbies}")      # tuple
    print(f"Details: {details}")      # dict

profile("Khanishk", "coding", "gaming", age=16, city="Aligarh")


# -------------------------
# UNPACKING with * and **
# -------------------------

"""
You can also UNPACK a list/dict into a function using * and **
"""

nums = [1, 2, 3]
print(add(*nums))     # unpacks list → add(1, 2, 3)

info = {"name": "Khanishk", "age": 16}
show_info(**info)     # unpacks dict → show_info(name="Khanishk", age=16)


# -------------------------
# REAL-WORLD EXAMPLE
# -------------------------

def create_user(username, *roles, **settings):
    """
    username  → required
    *roles    → any number of roles
    **settings → optional config
    """
    print(f"User: {username}")
    print(f"Roles: {roles}")
    print(f"Settings: {settings}")

create_user("khanishk99", "admin", "editor", theme="dark", lang="en")


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

* *args   → tuple of extra positional args
* **kwargs → dict of extra keyword args
* Order: normal → *args → **kwargs
* * unpacks a list when calling a function
* ** unpacks a dict when calling a function
"""
