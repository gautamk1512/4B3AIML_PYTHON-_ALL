# Topic 15: File Handling

# Questions
# 1. How do you open, read, and write files in Python?
# 2. What are file operations?

# Notes
# Use open(), read(), write(), close()
# Operations: reading, writing, appending, deleting

# Solutions
with open("sample.txt", "w") as f:
    f.write("Hello, file!")
with open("sample.txt", "r") as f:
    print(f.read())
