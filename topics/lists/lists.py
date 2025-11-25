# Topic 07: Lists

# Questions
# 1. What is a list in Python?
# 2. List some list methods.
# 3. How do you use list comprehensions?

# Notes
# Lists are ordered, mutable collections.
# Methods: append(), extend(), insert(), remove(), pop(), sort(), reverse()
# List comprehensions: [expression for item in iterable]

# Solutions
my_list = [1, 2, 3]
my_list.append(4)
my_list.remove(2)
print(my_list)
squared = [x**2 for x in range(5)]
print(squared)
