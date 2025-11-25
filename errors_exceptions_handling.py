# Topic 25: Errors and Exceptions Handling

# Questions
# 1. How does Python handle exceptions?
# 2. What are types of exceptions?
# 3. How do you use try/except/else/finally?
# 4. How do you raise and create custom exceptions?

# Notes
# Use try/except blocks
# Types: ZeroDivisionError, ValueError, etc.
# Custom: Define class inheriting from Exception

# Solutions
try:
    x = int(input("Enter a number: "))
    print(10/x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("No error")
finally:
    print("Done")

class MyError(Exception):
    pass
raise MyError("Custom error!")
