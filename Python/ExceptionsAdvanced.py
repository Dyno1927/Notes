# EXCEPTION HANDLING (ADVANCED) - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers advanced exception handling:

* try / except / else / finally
* Multiple exception types
* Exception object (as e)
* Raising exceptions
* Custom exceptions
* Exception chaining
* Context managers (with)
"""

# -------------------------
# BASIC STRUCTURE
# -------------------------

"""
try     → code that might fail
except  → what to do if it fails
else    → runs if NO exception occurred
finally → ALWAYS runs (cleanup)
"""

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Success! Result: {result}")  # only runs if no error
finally:
    print("This always runs.")


# -------------------------
# CATCHING SPECIFIC EXCEPTIONS
# -------------------------

"""
Always catch SPECIFIC exceptions first,
then broad ones. Catching Exception too early
hides bugs.
"""


def safeDivide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    except TypeError:
        print("Both values must be numbers!")
        return None


print(safeDivide(10, 2))
print(safeDivide(10, 0))
print(safeDivide(10, "x"))


# -------------------------
# EXCEPTION OBJECT (as e)
# -------------------------

"""
'as e' gives you access to the error message and details.
"""

try:
    x = int("abc")
except ValueError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")


# -------------------------
# CATCHING MULTIPLE IN ONE LINE
# -------------------------

try:
    data = [1, 2, 3]
    print(data[10])
except (IndexError, KeyError) as e:
    print(f"Access error: {e}")


# -------------------------
# RAISING EXCEPTIONS
# -------------------------

"""
Use 'raise' to trigger an exception yourself.
Useful for validating input.
"""


def setAge(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is not realistic.")
    return age


try:
    print(setAge(25))
    print(setAge(-5))
except ValueError as e:
    print(f"ValueError: {e}")


# -------------------------
# CUSTOM EXCEPTIONS
# -------------------------

"""
You can create your own exception types by
inheriting from Exception.

This makes error handling more specific and readable.
"""


class InsufficientFundsError(Exception):
    """
    Raised when account balance is too low
    """

    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Tried to withdraw ₹{amount} but only ₹{balance} available.")


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= amount
        return self._balance


acc = BankAccount(1000)

try:
    acc.withdraw(500)
    print("Withdrew ₹500 successfully.")
    acc.withdraw(800)  # this will fail
except InsufficientFundsError as e:
    print(f"Custom error: {e}")


# -------------------------
# EXCEPTION CHAINING
# -------------------------

"""
When you catch an exception and raise another,
use 'raise NewException from original'
to keep the traceback chain.
"""

try:
    try:
        x = int("not a number")
    except ValueError as e:
        raise RuntimeError("Failed to process input.") from e  # chains to original
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Caused by: {e.__cause__}")


# -------------------------
# CONTEXT MANAGERS (with)
# -------------------------

"""
'with' is used for resources that need cleanup (files, connections).
It calls __enter__ and __exit__ automatically.

You can make your own context manager using a class.
"""


class ManagedResource:
    def __enter__(self):
        print("Resource opened.")
        return self  # what gets bound to 'as' variable

    def __exit__(self, excType, excVal, excTb):
        print("Resource closed (always).")
        return False  # False means: don't suppress exceptions


with ManagedResource() as res:
    print("Using resource.")
    # even if error happens here, __exit__ still runs

print("Done.")


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

try      → risky code
except   → handle specific error
else     → runs if no error
finally  → always runs

raise    → trigger an error manually
Exception → base class for custom errors

Best practices:
- Catch specific exceptions, not bare 'except:'
- Use 'as e' to inspect the error
- Create custom exceptions for your app's logic
- Use 'finally' for cleanup (closing files, etc.)
- Use 'raise X from Y' to preserve cause chain
"""
