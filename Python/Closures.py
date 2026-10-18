# CLOSURES - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers closures:

* What a closure is
* How inner functions work
* nonlocal keyword
* Real-world uses
* Closures vs classes

A closure is an inner function that REMEMBERS
the variables from its outer function — even after
the outer function has finished running.
"""

# -------------------------
# BUILDING BLOCK: INNER FUNCTION
# -------------------------

"""
Functions can be defined inside other functions.
The inner function can access the outer function's variables.
"""


def outer():
    message = "Hello from outer!"

    def inner():
        print(message)  # inner can see outer's variable

    inner()


outer()


# -------------------------
# THE CLOSURE
# -------------------------

"""
A closure happens when:
1. There's an inner function
2. The inner function uses variables from the outer function
3. The outer function RETURNS the inner function

The inner function "closes over" the outer variables
and keeps them alive even after outer() is done.
"""


def makeGreeter(name):
    def greet():
        print(f"Hello, {name}!")  # name is "enclosed"

    return greet  # return the function, not its result


greetKhanishk = makeGreeter("Khanishk")
greetAarav = makeGreeter("Aarav")

greetKhanishk()  # Hello, Khanishk!
greetAarav()  # Hello, Aarav!

# makeGreeter() has finished — but name is still remembered!


# -------------------------
# PRACTICAL: COUNTER
# -------------------------


def makeCounter(start=0):
    """
    Each counter has its own independent count
    """
    count = [start]  # use list so it's mutable inside inner

    def increment():
        count[0] += 1
        return count[0]

    return increment


counter1 = makeCounter()
counter2 = makeCounter(100)

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 101  — independent!
print(counter1())  # 3


# -------------------------
# NONLOCAL KEYWORD
# -------------------------

"""
'nonlocal' lets the inner function MODIFY
a variable in the outer function's scope.
(Without it, reassigning creates a new local variable.)
"""


def makeCounter_v2(start=0):
    count = start

    def increment():
        nonlocal count  # tell Python: use the outer 'count'
        count += 1
        return count

    return increment


c = makeCounter_v2()
print(c())  # 1
print(c())  # 2
print(c())  # 3


# -------------------------
# PRACTICAL: MULTIPLIER FACTORY
# -------------------------


def multiplier(factor):
    def multiply(n):
        return n * factor  # factor is enclosed

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
print(double(10))  # 20


# -------------------------
# CLOSURE vs CLASS
# -------------------------

"""
A closure is like a lightweight class.
Use a closure for simple stateful behavior.
Use a class when it gets more complex.
"""


# Closure version
def makeAccount(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def getBalance():
        return balance

    return deposit, getBalance


deposit, getBalance = makeAccount(1000)
print(getBalance())  # 1000
deposit(500)
print(getBalance())  # 1500


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

1. Inner function + outer variable = closure
2. The enclosed variable stays alive after outer returns
3. Use 'nonlocal' to MODIFY an outer variable
4. Each closure call gets its own independent enclosed data
5. Closures are the foundation of decorators!

When to use closures:
- Factory functions (makeGreeter, multiplier)
- Stateful functions without a full class
- When you need to "bake in" a value
"""
