"""
Topic: OOP Concepts (Object, Class, Abstraction, Encapsulation, Polymorphism, Inheritance)

Explanation:
1. Class: A blueprint for creating objects.
2. Object: An instance of a class.
3. Encapsulation: Hiding data (using private variables) and restricting access.
4. Inheritance: A child class inherits properties/methods from a parent class.
5. Polymorphism: Different classes can be used through the same interface (e.g., method overriding).
6. Abstraction: Hiding complex implementation details (often using Abstract Base Classes).
"""

# Code Breakdown:
# 1. Define a class `Car` (Encapsulation).
# 2. Create an object of `Car`.
# 3. Define Parent class `Animal` and Child class `Dog` (Inheritance).
# 4. Demonstrate Polymorphism (Overriding `speak` method).
# 5. Demonstrate Abstraction using `abc` module.

from abc import ABC, abstractmethod

# --- 1 & 2. Class and Object (with Encapsulation) ---
class Car:
    def __init__(self, brand, model):
        self.brand = brand      # Public attribute
        self.__speed = 0        # Private attribute (Encapsulation)

    def accelerate(self, increment):
        self.__speed += increment
        print(f"{self.brand} is going {self.__speed} km/h")

my_car = Car("Toyota", "Corolla")
my_car.accelerate(20)
# print(my_car.__speed) # This would raise an AttributeError

# --- 3 & 4. Inheritance and Polymorphism ---
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
print("\nPolymorphism:")
for animal in animals:
    print(animal.speak())

# --- 5. Abstraction ---
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

c = Circle(5)
print(f"\nAbstraction Area: {c.area()}")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Create a class `Person` with attributes `name` and `age`. Create an object and print its attributes.
# 2. Create a class `BankAccount` with a private attribute `_balance`. Add methods to deposit and withdraw money.
# 3. Create a base class `Vehicle` and a derived class `Bike` that inherits from `Vehicle`.
# 4. Demonstrate polymorphism by creating two classes `Bird` and `Airplane` that both have a `fly()` method.

# Solutions
print("\n--- Practice Solutions ---")

# 1. Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 25)
print(f"Person: {p.name}, Age: {p.age}")

# 2. BankAccount
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected/Private convention

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New Balance: {self._balance}")
        else:
            print("Insufficient funds")

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)

# 3. Vehicle and Bike
class Vehicle:
    def drive(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def drive(self):
        print("Bike is riding")

b = Bike()
b.drive()

# 4. Polymorphism
class Bird:
    def fly(self):
        return "Bird flying"

class Airplane:
    def fly(self):
        return "Airplane flying"

flyers = [Bird(), Airplane()]
for f in flyers:
    print(f.fly())

