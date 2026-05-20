# ABSTRACT CLASSES & INTERFACES (ABC) - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file covers:

* Abstract classes (using ABC)
* Abstract methods
* Interfaces in Python (via ABC)
* Why use abstract classes
* Real-world patterns

Python doesn't have a built-in 'interface' keyword like Java/C#.
Instead, we use ABC (Abstract Base Class) for both
abstract classes AND interface-like contracts.
"""

from abc import ABC, abstractmethod

# -------------------------
# ABSTRACT CLASS
# -------------------------

"""
An abstract class:
- Cannot be instantiated (no objects directly)
- Forces subclasses to implement certain methods
- Can have both abstract AND normal methods
"""

class Shape(ABC):
    """
    Abstract base class for all shapes.
    Any subclass MUST implement area() and perimeter().
    """

    @abstractmethod
    def area(self):
        """Must be implemented by subclass"""
        pass

    @abstractmethod
    def perimeter(self):
        """Must be implemented by subclass"""
        pass

    # Normal method — shared by all subclasses
    def describe(self):
        print(f"I am a {self.__class__.__name__}.")
        print(f"  Area:      {self.area():.2f}")
        print(f"  Perimeter: {self.perimeter():.2f}")


# shape = Shape()   ← TypeError! Can't instantiate abstract class


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Works!
shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    s.describe()
    print()


# -------------------------
# INTERFACE PATTERN (pure ABC)
# -------------------------

"""
A pure interface has ONLY abstract methods — no implementation.
All subclasses must implement every method.

Python doesn't have a keyword for this, but a class
with only @abstractmethod acts like an interface.
"""

class Saveable(ABC):
    """
    Interface: anything that can be saved
    """
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self, data):
        pass


class Printable(ABC):
    """
    Interface: anything that can be printed
    """
    @abstractmethod
    def print_info(self):
        pass


# A class can implement MULTIPLE ABCs (like multiple interfaces)
class UserProfile(Saveable, Printable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        print(f"Saving {self.name} to database...")

    def load(self, data):
        self.name = data["name"]
        self.age = data["age"]
        print(f"Loaded profile: {self.name}")

    def print_info(self):
        print(f"Name: {self.name} | Age: {self.age}")


user = UserProfile("Khanishk", 16)
user.print_info()
user.save()
user.load({"name": "Aarav", "age": 17})
user.print_info()


# -------------------------
# ABSTRACT PROPERTY
# -------------------------

"""
You can make properties abstract too,
forcing subclasses to define them.
"""

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        """Every animal must define its sound"""
        pass

    def speak(self):
        print(f"{self.__class__.__name__} says: {self.sound}")


class Dog(Animal):
    @property
    def sound(self):
        return "Woof!"

class Cat(Animal):
    @property
    def sound(self):
        return "Meow!"


Dog().speak()
Cat().speak()


# -------------------------
# CHECKING INSTANCES
# -------------------------

"""
isinstance() works with ABCs too.
"""

c = Circle(3)
print(isinstance(c, Shape))      # True
print(isinstance(c, Saveable))   # False


# -------------------------
# SUMMARY
# -------------------------

"""
KEY POINTS:

Abstract class (ABC):
- Inherit from ABC
- Use @abstractmethod to force subclass to implement
- Cannot be instantiated directly
- Can have regular methods too

Interface pattern:
- Pure ABC with only @abstractmethod
- A class can inherit from multiple ABCs

vs Regular inheritance:
- Regular: subclass can choose to override or not
- Abstract: subclass MUST implement or gets TypeError

When to use:
- When multiple classes share a "contract"
- When you want to enforce method names across a family
- When writing a framework or plugin system
"""
