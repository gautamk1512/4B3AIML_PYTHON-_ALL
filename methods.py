# Topic 17: Methods

# Questions
# 1. What are methods in Python?
# 2. What are special methods?
# 3. What is the self variable?

# Notes
# Methods: Functions defined inside a class
# Special methods: __init__, __str__, __len__, etc.
# self: Refers to the instance of the class

# Solutions
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}!"

    def __str__(self):
        return f"Person({self.name})"

p = Person("Alice")
print(p.greet())
print(str(p))
