# Topic 24: Types of Errors

# Questions
# 1. What are syntax errors?
# 2. What are runtime errors?
# 3. What are logical errors?

# Notes
# Syntax: Mistakes in code structure
# Runtime: Errors during execution
# Logical: Code runs but gives wrong result

# Solutions
# Syntax error example:
# print('Hello'
# Runtime error example:
try:
    print(1/0)
except ZeroDivisionError:
    print("Runtime error: Division by zero")
# Logical error example:
def add(a, b):
    return a - b  # Should be a + b
print(add(2, 3))
