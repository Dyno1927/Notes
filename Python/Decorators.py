# DECORATORS - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers decorators:

* What a decorator is
* How to write one
* Decorators with arguments
* Multiple decorators
* Real-world use cases (timer, logger, validator)

A decorator WRAPS a function to add extra behavior
without changing the function's own code.
"""

# -------------------------
# BUILDING BLOCKS FIRST
# -------------------------

"""
In Python, functions are objects.
You can pass them as arguments and return them.
That's what makes decorators possible.
"""


def say_hello():
    print("Hello!")


def run(func):
    func()  # calling a function passed as argument


run(say_hello)


# -------------------------
# YOUR FIRST DECORATOR
# -------------------------

"""
A decorator is a function that:
1. Takes a function as input
2. Wraps it with extra code
3. Returns the new wrapped function
"""


def my_decorator(func):
    def wrapper():
        print("--- Before ---")
        func()  # calls the original function
        print("--- After ---")

    return wrapper


def greet():
    print("Hello, Khanishk!")


# Apply decorator manually:
greet = my_decorator(greet)
greet()


# -------------------------
# @ SYNTAX (SYNTACTIC SUGAR)
# -------------------------

"""
@ is a shortcut for wrapping.

@my_decorator
def greet(): ...

is the same as:
greet = my_decorator(greet)
"""


@my_decorator
def farewell():
    print("Goodbye!")


farewell()


# -------------------------
# DECORATOR WITH ARGUMENTS
# -------------------------

"""
When the function being decorated takes arguments,
use *args and **kwargs in the wrapper.
"""


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done: {func.__name__}")
        return result  # don't forget to return!

    return wrapper


@log
def add(a, b):
    return a + b


print(add(3, 4))


# -------------------------
# REAL-WORLD: TIMER
# -------------------------

import time


def timer(func):
    """
    Measures how long a function takes to run
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result

    return wrapper


@timer
def slow_task():
    time.sleep(0.5)
    print("Task done.")


slow_task()


# -------------------------
# REAL-WORLD: VALIDATOR
# -------------------------


def require_positive(func):
    """
    Ensures arguments are positive before calling function
    """

    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print(f"Error: {arg} is not positive!")
                return None
        return func(*args, **kwargs)

    return wrapper


@require_positive
def square_root(n):
    return n**0.5


print(square_root(9))  # works
print(square_root(-4))  # blocked by decorator


# -------------------------
# STACKING DECORATORS
# -------------------------

"""
You can apply multiple decorators.
They run from BOTTOM to TOP (innermost first).
"""


@log
@timer
def compute(n):
    return sum(range(n))


print(compute(1000))


# -------------------------
# DECORATOR WITH PARAMETERS
# -------------------------

"""
If you want to PASS arguments TO the decorator itself,
add an extra outer function.
"""


def repeat(times):
    """
    Runs the function 'times' times
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say(msg):
    print(msg)


say("Hello!")


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

1. Decorator = wrapper function
2. Wraps a function without changing it
3. @ syntax is shorthand for func = decorator(func)
4. Always use *args, **kwargs in wrapper
5. Always return result from wrapper
6. Stack multiple with multiple @

Common uses:
- Logging
- Timing
- Auth checking
- Caching
- Input validation
"""
