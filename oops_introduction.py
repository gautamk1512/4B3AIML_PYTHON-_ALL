# Topic 16: OOPs Introduction

# Questions
# 1. What are Python OOP concepts?
# 2. What is an object and a class?
# 3. What are class attributes?

# Notes
# OOP concepts: Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction
# Object: Instance of a class
# Class: Blueprint for objects
# Class attributes: Variables shared by all instances

# Solutions
class Car:
    wheels = 4  # class attribute
    def __init__(self, brand):
        self.brand = brand  # instance attribute

car1 = Car("Toyota")
print(car1.brand)
print(Car.wheels)
