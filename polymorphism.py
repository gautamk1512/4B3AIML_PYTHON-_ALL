# Topic 20: Polymorphism

# Questions
# 1. What is polymorphism?
# 2. What is operator overloading?
# 3. What is method overriding?

# Notes
# Polymorphism: Same interface, different implementation
# Operator overloading: Redefining operators for user-defined types
# Method overriding: Subclass provides specific implementation

# Solutions
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

s = Shape()
c = Circle()
print(c.area())

class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(3)
n2 = Number(4)
print(n1 + n2)
