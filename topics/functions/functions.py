# Topic 12: Functions

# Questions
# 1. How do you define a function?
# 2. What are parameters and arguments?
# 3. What is recursion?
# 4. What are decorators and generators?

# Notes
# Define with def keyword.
# Parameters: variables in function definition. Arguments: values passed.
# Recursion: function calling itself.
# Decorators: functions modifying other functions. Generators: yield values.

# Solutions
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
@my_decorator
def say_hi():
    print("Hi!")
say_hi()
def gen():
    for i in range(3):
        yield i
for value in gen():
    print(value)
