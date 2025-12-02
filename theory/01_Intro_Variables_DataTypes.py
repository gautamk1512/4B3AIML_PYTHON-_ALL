"""
Topic: Introduction to Python, Variables, and Data Types

Explanation:
1. Python Introduction: Python is a high-level, interpreted programming language known for its simplicity and readability.
2. Variables: Containers for storing data values. In Python, you don't need to declare the type explicitly.
3. Data Types:
   - Integers (int): Whole numbers (e.g., 10, -5).
   - Floats (float): Decimal numbers (e.g., 3.14, -0.01).
   - Strings (str): Text data enclosed in quotes (e.g., "Hello").
   - Booleans (bool): True or False values.
"""

# Code Breakdown:
# 1. Print a welcome message to demonstrate basic output.
# 2. Define variables of different types (integer, float, string, boolean).
# 3. Use the `type()` function to inspect the data type of each variable.
# 4. Perform basic operations (addition, concatenation) to show how types interact.
# 5. Print the results.

# 1. Basic Output
print("Welcome to Python Programming!")

# 2. Variable Declaration
age = 25                # Integer
height = 5.9            # Float
name = "Alice"          # String
is_student = True       # Boolean

# 3. Checking Data Types
print(f"Value: {age}, Type: {type(age)}")
print(f"Value: {height}, Type: {type(height)}")
print(f"Value: {name}, Type: {type(name)}")
print(f"Value: {is_student}, Type: {type(is_student)}")

# 4. Basic Operations
future_age = age + 5
greeting = "Hello, " + name

# 5. Output Results
print(f"In 5 years, {name} will be {future_age} years old.")
print(greeting)
