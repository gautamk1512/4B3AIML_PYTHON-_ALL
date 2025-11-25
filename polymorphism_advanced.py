# Topic 23: Polymorphism (Advanced)

# Questions
# 1. What is method overloading?
# 2. What is method overriding?
# 3. What is the super keyword?

# Notes
# Method overloading: Not directly supported, can use default arguments
# Method overriding: Subclass redefines parent method
# super: Calls parent class method

# Solutions
class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        print("Child")
        super().show()
c = Child()
c.show()
