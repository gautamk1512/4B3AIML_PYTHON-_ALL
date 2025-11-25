# Topic 13: Modules

# Questions
# 1. How do you create and import modules?
# 2. What is a namespace?

# Notes
# Create a .py file. Import with import statement.
# Namespace: a container for names (variables, functions).

# Solutions
# Create a module: Save functions in mymodule.py
# Import:
# 1. Create a module (mymodule.py):
# def greet(name):
#     return f"Hello, {name}!"

# Import and use the module:
# import mymodule
# print(mymodule.greet("Alice"))

# 2. Demonstrate namespace:
x = 5  # This 'x' is in the global namespace

def show_namespace():
    y = 10  # 'y' is in the local namespace of this function
    print("Local namespace:", locals())

show_namespace()
print("Global namespace:", globals().get('x'))

# 3. Import built-in module and use a function:
import math
print(math.sqrt(16))
