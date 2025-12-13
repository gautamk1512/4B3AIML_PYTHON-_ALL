"""
Topic: Working with Modules and Packages

Explanation:
1. Module: A file containing Python code (functions, classes, variables).
2. Package: A directory containing multiple modules and an `__init__.py` file.
3. Importing:
   - `import module_name`: Imports the whole module.
   - `from module_name import item`: Imports specific parts.
   - `import module_name as alias`: Imports with a shorter name.
"""

# Code Breakdown:
# 1. Import the built-in `math` module.
# 2. Use `math.sqrt` and `math.pi`.
# 3. Import the `random` module as `rnd`.
# 4. Generate a random number.
# 5. Demonstrate how you would import from a custom package (commented out).

# 1. Standard Import
import math

# 2. Using Module Functions
root = math.sqrt(16)
print(f"Square root of 16 is: {root}")
print(f"Value of PI: {math.pi}")

# 3. Aliasing
import random as rnd

# 4. Using Alias
rand_num = rnd.randint(1, 100)
print(f"Random number (1-100): {rand_num}")

# 5. Custom Package Example (Conceptual)
"""
Structure:
my_package/
    __init__.py
    module1.py
    module2.py

Usage:
from my_package import module1
module1.my_function()
"""
print("\n(Custom package structure explained in comments)")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Import the `datetime` module and print the current date and time.
# 2. Create a Python file named `my_math.py` with a function `add(x, y)`. Import it into another file and use the function.
# 3. Use the `random` module to simulate a dice roll (generate a number between 1 and 6).
# 4. Import only the `pi` constant from the `math` module and print its value.

# Solutions
print("\n--- Practice Solutions ---")

# 1. DateTime
import datetime
print(f"Current Date/Time: {datetime.datetime.now()}")

# 2. Custom Module (Assuming my_math.py exists with add(x,y))
# To test this, ensure my_math.py is in the same directory
try:
    import my_math
    print(f"2 + 3 = {my_math.add(2, 3)}")
except ImportError:
    print("my_math.py not found. Please create it first.")

# 3. Dice Roll
import random
print(f"Dice roll: {random.randint(1, 6)}")

# 4. Import Pi
from math import pi
print(f"PI: {pi}")

