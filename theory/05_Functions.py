"""
Topic: Defining and Using Functions

Explanation:
1. Function: A block of reusable code that runs when called.
2. Definition: Use `def` keyword.
3. Arguments (Parameters): Data passed into functions.
4. Return Values: Data sent back from the function using `return`.
5. Built-in Functions: Pre-defined functions in Python (e.g., `len()`, `max()`, `sum()`).
"""

# Code Breakdown:
# 1. Define a simple greeting function.
# 2. Define a function with arguments and a return value (add numbers).
# 3. Define a function with default arguments.
# 4. Demonstrate usage of built-in functions.

# 1. Simple Function
def greet():
    print("Hello! This is a function.")

greet()  # Call function

# 2. Arguments and Return Value
def add_numbers(a, b):
    """Returns the sum of a and b."""
    return a + b

result = add_numbers(10, 5)
print(f"Sum of 10 and 5 is: {result}")

# 3. Default Arguments
def introduce(name, role="Student"):
    print(f"I am {name} and I am a {role}.")

introduce("Alice")             # Uses default role
introduce("Bob", "Teacher")    # Overrides default role

# 4. Built-in Functions
numbers = [10, 20, 30, 40, 50]
print("\nBuilt-in Functions:")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Length: {len(numbers)}")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Write a function `square(n)` that takes a number and returns its square.
# 2. Write a function `is_even(n)` that returns True if the number is even, otherwise False.
# 3. Write a function that takes two arguments, `name` and `age`, and prints a message.
# 4. Use the built-in `max()` function to find the largest number in `[5, 12, 8, 21, 3]`.
