# Python Programming Topics: Code Notes & Examples

# Topic 01: Introduction
print("Hello, Python!")

# Topic 02: Variables and Tokens
x = 10  # integer variable
y = 3.14  # float variable
name = "Alice"  # string variable

# Topic 03: Input/Output
user_input = input("Enter something: ")
print("You entered:", user_input)

# Topic 04: Operators
# Arithmetic
sum_result = 5 + 3
# Comparison
is_equal = (5 == 3)
# Logical
is_true = (True and False)

# Topic 05: Control statements
if x > 5:
    print("x is greater than 5")
for i in range(3):
    print(i)
while x > 0:
    x -= 1

# Topic 06: Numbers
decimal_num = 42
binary_num = bin(decimal_num)
octal_num = oct(decimal_num)
hex_num = hex(decimal_num)

# Topic 07: Lists
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Topic 08: Strings
s = "Python"
print(s.upper())
print(s[1:4])

# Topic 09: Tuples
t = (1, 2, 3)
print(t)

# Topic 10: Dictionary
d = {"a": 1, "b": 2}
print(d["a"])

# Topic 11: Sets
s = {1, 2, 3}
s.add(4)
print(s)

# Topic 12: Functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Bob"))

# Topic 13: Modules
import math
print(math.sqrt(16))

# Topic 14: Python Packages
# Install with pip: pip install requests
import requests

# Topic 15: File Handling
with open("sample.txt", "w") as f:
    f.write("Hello, file!")
with open("sample.txt", "r") as f:
    print(f.read())

# Topic 16: OOPs Introduction
class Animal:
    pass

# Topic 17: Methods
class Dog:
    def bark(self):
        print("Woof!")
d = Dog()
d.bark()

# Topic 18: Keywords and Constructor
class Person:
    def __init__(self, name):
        self.name = name
p = Person("Alice")

# Topic 19: Inheritance
class Parent:
    pass
class Child(Parent):
    pass

# Topic 20: Polymorphism
class Bird:
    def speak(self):
        print("Tweet!")
class Parrot(Bird):
    def speak(self):
        print("Squawk!")
b = Bird()
p = Parrot()
b.speak()
p.speak()

# Topic 21: Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Topic 22: Access Modifiers and Encapsulation
class Encapsulate:
    def __init__(self):
        self._protected = "protected"
        self.__private = "private"
    def get_private(self):
        return self.__private
e = Encapsulate()
print(e._protected)
print(e.get_private())
