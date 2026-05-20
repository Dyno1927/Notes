# ITERATORS & GENERATORS - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers:

* Iterators (what they are, how to build one)
* Generators (yield keyword)
* Generator functions vs generator expressions
* Why use generators (memory efficiency)
"""

# -------------------------
# WHAT IS AN ITERATOR?
# -------------------------

"""
An iterator is any object that:
1. Has __iter__() → returns itself
2. Has __next__() → returns next value, raises StopIteration when done

Lists, strings, dicts are ITERABLES (you can loop over them).
When you use a for loop, Python calls iter() then next() behind the scenes.
"""

nums = [1, 2, 3]
it = iter(nums)       # get iterator from list

print(next(it))       # 1
print(next(it))       # 2
print(next(it))       # 3
# print(next(it))     # StopIteration!


# -------------------------
# BUILDING A CUSTOM ITERATOR
# -------------------------

class CountUp:
    """
    Counts from start to end
    """

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self      # the object itself is the iterator

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


counter = CountUp(1, 5)
for n in counter:
    print(n)


# -------------------------
# GENERATORS
# -------------------------

"""
A generator is a SIMPLER way to make an iterator.

Instead of a class with __iter__ and __next__,
you write a function with yield.

yield → pauses the function, returns a value,
        and REMEMBERS where it left off.
"""

def count_up(start, end):
    current = start
    while current <= end:
        yield current          # pause here, return value
        current += 1           # resumes from here next time

gen = count_up(1, 5)

print(next(gen))   # 1
print(next(gen))   # 2

for n in count_up(1, 5):
    print(n)


# -------------------------
# WHY GENERATORS? (MEMORY)
# -------------------------

"""
A list stores ALL values in memory at once.
A generator produces values ONE AT A TIME.

For large data, generators are WAY more efficient.
"""

# This builds a list of 1 million numbers in memory
big_list = [x * 2 for x in range(1_000_000)]

# This produces them one at a time — barely uses memory
big_gen = (x * 2 for x in range(1_000_000))

# Use sum without loading everything
total = sum(x * 2 for x in range(1_000_000))
print(total)


# -------------------------
# YIELD FROM
# -------------------------

"""
yield from → delegates to another generator/iterable
Makes it easy to chain generators
"""

def first_half():
    yield 1
    yield 2
    yield 3

def second_half():
    yield 4
    yield 5

def all_numbers():
    yield from first_half()   # delegates to first_half
    yield from second_half()

for n in all_numbers():
    print(n)


# -------------------------
# REAL-WORLD: INFINITE SEQUENCE
# -------------------------

"""
Generators can produce INFINITE sequences
because they generate one value at a time.
"""

def natural_numbers():
    """
    Generates 1, 2, 3, 4, ... forever
    """
    n = 1
    while True:
        yield n
        n += 1

gen = natural_numbers()
for _ in range(5):
    print(next(gen))   # safely get first 5


# -------------------------
# REAL-WORLD: FILE READER
# -------------------------

"""
Reading a huge file line by line — memory efficient
"""

def read_lines(filepath):
    """
    Yields one line at a time instead of loading the whole file
    """
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

# Usage (only works if file exists):
# for line in read_lines("big_file.txt"):
#     print(line)


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

Iterator:
- Object with __iter__ and __next__
- Raises StopIteration when done

Generator:
- Function with yield
- Automatically an iterator
- Pauses and resumes execution
- Memory efficient (one value at a time)

yield from → delegates to another iterable

When to use generators:
- Large datasets
- Infinite sequences
- Streaming data (files, APIs)
"""
