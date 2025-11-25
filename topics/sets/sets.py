# Topic 11: Sets

# Questions
# 1. What is a set?
# 2. How do you add and remove elements?
# 3. What are set operations?

# Notes
# Sets are unordered collections of unique elements.
# Methods: add(), remove(), discard(), union(), intersection(), difference()

# Solutions
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)
print(s.union({5, 6}))
print(s.intersection({3, 4}))
