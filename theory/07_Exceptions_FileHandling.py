"""
Topic: Exceptions and File Handling

Explanation:
1. Exceptions: Errors detected during execution.
   - try: Block of code to test for errors.
   - except: Block of code to handle the error.
   - else: Executes if no error occurs.
   - finally: Executes regardless of the result.
2. File Handling: Reading from and writing to files.
   - Modes: 'r' (read), 'w' (write), 'a' (append).
"""

# Code Breakdown:
# 1. Use `try-except` to handle division by zero.
# 2. Use `finally` to indicate cleanup/completion.
# 3. Write to a file using `open()` with mode 'w'.
# 4. Read from the file using mode 'r'.

# --- Exception Handling ---
print("--- Exception Handling ---")
try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
else:
    print(f"Result is: {result}")
finally:
    print("Execution complete.")

# --- File Handling ---
print("\n--- File Handling ---")
filename = "test_file.txt"

# Writing
with open(filename, "w") as file:
    file.write("Hello, this is a test file.\nPython file handling is easy.")
print(f"Written to {filename}")

# Reading
print(f"Reading from {filename}:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Write a Python program that asks for an integer input and handles the `ValueError` if the user enters a string.
# 2. Write a program that attempts to open a non-existent file and handles the `FileNotFoundError`.
# 3. Create a file named `notes.txt`, write 3 lines of text to it, and then read and print the content.
# 4. Modify the previous program to append a new line to `notes.txt` without overwriting existing content.

# Solutions
print("\n--- Practice Solutions ---")

# 1. ValueError Handling
try:
    val = int(input("Enter an integer: "))
    print(f"You entered: {val}")
except ValueError:
    print("That's not an integer!")

# 2. FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# 3. Write and Read
with open("notes.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

with open("notes.txt", "r") as f:
    print("Reading notes.txt:\n" + f.read())

# 4. Append
with open("notes.txt", "a") as f:
    f.write("Appended Line 4\n")

print("After append:")
with open("notes.txt", "r") as f:
    print(f.read())

