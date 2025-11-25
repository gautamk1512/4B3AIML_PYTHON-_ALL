# Topic 10: Dictionary

# Questions
# 1. What is a dictionary?
# 2. How do you access and update values?
# 3. What are dictionary methods?

# Notes
# Dictionaries store key-value pairs.
# Access: d[key]
# Update: d[key] = value
# Methods: keys(), values(), items(), get(), pop(), update()

# Solutions
d = {"a": 1, "b": 2}
print(d["a"])
d["c"] = 3
print(d)
print(list(d.keys()))
print(list(d.values()))
