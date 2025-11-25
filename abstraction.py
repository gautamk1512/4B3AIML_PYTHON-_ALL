# Topic 21: Abstraction

# Questions
# 1. What is abstraction?
# 2. What are abstract classes?

# Notes
# Abstraction: Hiding implementation details
# Abstract class: Class with abstract methods

# Solutions
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

d = Dog()
print(d.sound())
