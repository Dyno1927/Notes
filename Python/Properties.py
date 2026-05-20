# PYTHON PROPERTIES (@property, @setter, @deleter) - COMPLETE GUIDE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file explains Python properties:

Covers:
- @property (getter)
- @property.setter
- @property.deleter
- Why properties exist
- Encapsulation
- Real-world usage patterns

Goal:
Turn methods into attributes while keeping control.
"""


# -------------------------
# BASIC PROPERTY (GETTER)
# -------------------------

class Person:
    """
    Basic example of @property
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        """
        Getter → accessed like attribute

        Instead of:
        obj.fullname()
        we use:
        obj.fullname
        """
        return f"{self.first} {self.last}"


p = Person("John", "Doe")
print(p.fullname)   # looks like attribute, but is actually a method


# -------------------------
# PROPERTY WITH SETTER
# -------------------------

class PersonSetter:
    """
    Demonstrates setter usage
    """

    def __init__(self, name):
        self.fullname = name   # calls setter automatically

    @property
    def fullname(self):
        """
        Getter
        """
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        """
        Setter → controls how value is assigned

        Useful for validation and splitting values
        """
        first, last = name.split(" ")
        self.first = first
        self.last = last


p2 = PersonSetter("Ichigo Kurosaki")
print(p2.fullname)


# -------------------------
# PROPERTY WITH DELETER
# -------------------------

class PersonDeleter:
    """
    Demonstrates deleter usage
    """

    def __init__(self, name):
        self.fullname = name

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """
        Deleter → runs when using: del obj.fullname
        """
        print("Deleting name...")
        self.first = None
        self.last = None


p3 = PersonDeleter("Light Yagami")
del p3.fullname


# -------------------------
# WHY USE PROPERTIES
# -------------------------

class WithoutProperty:
    """
    Old way (not recommended)
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_fullname(self):
        return f"{self.first} {self.last}"


class WithProperty:
    """
    Modern way using @property
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


# Usage difference:
obj1 = WithoutProperty("A", "B")
print(obj1.get_fullname())   # looks like function

obj2 = WithProperty("A", "B")
print(obj2.fullname)         # looks like attribute


# -------------------------
# VALIDATION USING SETTER
# -------------------------

class Temperature:
    """
    Real-world use: validation
    """

    def __init__(self, temp):
        self.temperature = temp   # goes through setter

    @property
    def temperature(self):
        return self._temperature   # internal variable

    @temperature.setter
    def temperature(self, value):
        """
        Validation logic
        """
        if value < -273:
            print("Temperature below absolute zero!")
        self._temperature = value


t = Temperature(-300)
print(t.temperature)


# -------------------------
# READ-ONLY PROPERTY
# -------------------------

class Circle:
    """
    Property without setter → read-only
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """
        Cannot assign to this directly
        """
        return 3.14 * self.radius ** 2


c = Circle(5)
print(c.area)


# -------------------------
# PRIVATE ATTRIBUTE STYLE
# -------------------------

class BankAccount:
    """
    Demonstrates controlled access
    """

    def __init__(self, balance):
        self._balance = balance   # "protected" convention

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid balance!")
        else:
            self._balance = amount


acc = BankAccount(1000)
acc.balance = 2000
print(acc.balance)


# -------------------------
# COMPUTED PROPERTIES
# -------------------------

class Rectangle:
    """
    Property depends on other attributes
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(4, 5)
print(r.area)
print(r.perimeter)


# -------------------------
# FINAL SUMMARY
# -------------------------

"""
KEY IDEAS:

1. @property → turns method into attribute
2. @setter → controls assignment
3. @deleter → controls deletion
4. Helps in:
   - Encapsulation
   - Validation
   - Cleaner syntax

IMPORTANT RULE:
Use properties when:
- You want logic behind an attribute
- You may change implementation later
- You need validation or computed values

Avoid using them for EVERYTHING.
"""
