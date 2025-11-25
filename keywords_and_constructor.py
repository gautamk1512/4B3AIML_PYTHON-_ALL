# Topic 18: Keywords and Constructor

# Questions
# 1. What is a constructor?
# 2. What is a default argument in constructors?
# 3. What is the static keyword?
# 4. What is the 'this' keyword in Python?

# Notes
# Constructor: __init__ method
# Default argument: Parameter with default value
# Static keyword: @staticmethod decorator
# 'this' keyword: Python uses 'self' instead

# Solutions
class Animal:
    def __init__(self, name="Dog"):
        self.name = name
    @staticmethod
    def speak():
        print("Animal speaks")

pet = Animal()
print(pet.name)
Animal.speak()
