# OBJECT ORIENTED PROGRAMMING (OOP) - COMPLETE REFERENCE
# WHEN GOING THROUGH THE FILE YOU MAY HAVE TO COMMENT
# OUT THE OTHER CODE BECAUSE IT MAY COME IN YOUR WAY
# COMMENTING SHORTCUT :-
# 1. SELECT THE REST OF THE CODE
# 2. USE CTRL + K CTRL + C AND TO UN-COMMENT CTRL + K
# CTRL + U

"""
This file demonstrates OOP concepts in Python:

Covers:
- Classes & Objects
- Instance vs Class variables
- Methods (instance, class, static)
- Properties (getter, setter, deleter)
- Magic/Dunder methods
- Inheritance
- Method overriding
- Encapsulation basics
- Real-world structure using Employee system

This is a learning + reference file.
"""

# -------------------------
# BASE CLASS
# -------------------------


class Employee:
    """
    Base class for all employees.

    Demonstrates:
    - Class variables
    - Instance variables
    - Methods
    - Properties
    - Magic methods
    """

    # Class variables (shared across ALL instances)
    raiseAmount: int = 1.05
    numOf_emps: int = 0

    def __init__(self, first, last, pay) -> str | int:
        """
        Constructor (initializer)

        Runs automatically when object is created.
        Used to initialize instance variables.
        """
        self.first = first
        self.last = last
        self.pay = int(pay)

        # Increment total employees count
        Employee.numOf_emps += 1

    # -------------------------
    # PROPERTIES
    # -------------------------

    @property
    def fullname(self) -> str:
        """
        Getter → allows method to be accessed like attribute

        Example:
        emp.fullname  (instead of emp.fullname())
        """
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        """
        Setter → allows setting value like attribute

        Example:
        emp.fullname = "John Doe"
        """
        first, last = name.split("")
        self.last = last

    @fullname.deleter
    def fullname(self):
        """
        Deleter → allows deleting attribute

        Example:
        del emp.fullname
        """
        print("delete Name !")
        self.first = None
        self.last = None

    @property
    def email(self) -> str:
        """
        Computed property → dynamically generated value
        """
        return f"{self.first}.{self.last}@company.com"

    # -------------------------
    # INSTANCE METHODS
    # -------------------------

    def applyRaise(self) -> int:
        """
        Instance method → works on object data

        Uses class variable to update salary
        """
        self.pay = int(self.pay * self.raiseAmount)

    # -------------------------
    # MAGIC (DUNDER) METHODS
    # -------------------------

    def __repr__(self) -> str | int:
        """
        Developer-friendly representation
        Used for debugging and recreating object
        """
        return f'Employee("{self.first}", "{self.last}", "{self.pay}")'

    def __str__(self) -> str:
        """
        User-friendly representation
        Used when printing object
        """
        return f"{self.fullname()}, {self.email}"

    def __add__(self, other):
        """
        Operator overloading (+)

        Allows:
        emp1 + emp2 → adds salaries
        """
        return self.pay + other.pay

    def __len__(self):
        """
        Allows:
        len(emp) → length of full name
        """
        return len(self.fullname())

    # -------------------------
    # CLASS METHODS
    # -------------------------

    @classmethod
    def setRaise_amt(cls, amount) -> int:
        """
        Class method → works on class, not instance

        Used to modify class variables
        """
        cls.raiseAmount = amount

    @classmethod
    def fromString(cls, empStr) -> str:
        """
        Alternative constructor

        Example:
        "John-Doe-50000"
        """
        first, last, pay = empStr.split("-")
        return cls(first, last, pay)

    # -------------------------
    # STATIC METHODS
    # -------------------------

    @staticmethod
    def isWorkday(day) -> bool:
        """
        Static method → independent function inside class

        Does not access class or instance
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# -------------------------
# INHERITANCE
# -------------------------


class Developer(Employee):
    """
    Child class of Employee

    Demonstrates:
    - Inheritance
    - Method reuse
    - Class variable override
    """

    # Override class variable
    raiseAmount = 1.10

    def __init__(self, first, last, pay, progLang) -> str | int:
        """
        super() → calls parent class constructor
        """
        super().__init__(first, last, pay)
        self.progLang = progLang  # New attribute


# -------------------------
# MANAGER CLASS
# -------------------------


class Manager(Employee):
    """
    Manager class

    Demonstrates:
    - Composition (manager has employees)
    - Working with lists of objects
    """

    def __init__(self, first, last, pay, employees=None) -> str | int:
        """
        Avoid mutable default argument (VERY IMPORTANT)
        """
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp) -> str:
        """
        Adds employee to manager list
        """
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self, emp) -> str:
        """
        Removes employee from manager list
        """
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmps(self) -> str:
        """
        Prints all employees under manager
        """
        for emp in self.employees:
            print("-->", emp.fullname())


# -------------------------
# TESTING / OBJECT CREATION
# -------------------------

"""
Creating Employee objects
"""
emp1 = Employee("Ryusui", "Nanami", "50000")
emp2 = Employee("Ichigo", "Kurosaki", "60000")


"""
Creating Developer objects
"""
dev1 = Developer("Orihime", "Kurosaki", "70000", "C")
dev2 = Developer("Ulquiora", "Cifar", "80000", "C++")


"""
Creating Manager object with employees
"""
mgr1 = Manager("Byakuya", "Kuchiki", "50000", [dev1, dev2])


# -------------------------
# QUICK CONCEPT SUMMARY
# -------------------------

"""
KEY TAKEAWAYS:

1. Class → blueprint
2. Object → instance of class
3. Instance variables → unique per object
4. Class variables → shared across all objects
5. Methods:
   - Instance → uses self
   - Class → uses cls
   - Static → independent

6. Inheritance → reuse code
7. Magic methods → customize behavior
8. Properties → control attribute access
9. Composition → object inside object
"""
