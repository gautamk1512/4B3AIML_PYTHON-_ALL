# Topic 09: Tuples

# Questions
# 1. What is a tuple?
# 2. How do you unpack a tuple?
# 3. What are tuple methods?

# Notes
# Tuples are ordered, immutable collections.
# Unpacking: a, b = (1, 2)
# Methods: count(), index()

# Solutions
t = (1, 2, 3)
a, b, c = t
print(a, b, c)
print(t.count(2))
print(t.index(3))
