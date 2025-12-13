"""
Topic: Conditional Statements and Loops in Python

Explanation:
1. Conditionals (if, elif, else): Used to execute code blocks based on specific conditions.
2. Loops:
   - For Loop: Iterates over a sequence (like a list, range, or string).
   - While Loop: Repeats a block of code as long as a condition is true.
3. Control Statements:
   - break: Exits the loop immediately.
   - continue: Skips the rest of the current iteration and moves to the next.
"""

# Code Breakdown:
# 1. Input a number from the user.
# 2. Use `if-elif-else` to categorize the number (Positive, Negative, Zero).
# 3. Demonstrate a `for` loop using `range()` to print numbers 0 to 4.
# 4. Demonstrate a `while` loop that counts down from 5 to 1.
# 5. Show `break` usage: stop loop when a specific value is reached.
# 6. Show `continue` usage: skip printing even numbers.

# 1. Conditionals
num = int(input("Enter a number: "))

# 2. Logic Check
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# 3. For Loop
print("\nFor Loop (0 to 4):")
for i in range(5):
    print(f"Iteration {i}")

# 4. While Loop
print("\nWhile Loop (Countdown):")
count = 5
while count > 0:
    print(count)
    count -= 1

# 5. Break and Continue
print("\nLoop with Break and Continue:")
for i in range(1, 11):
    if i == 5:
        print("Breaking at 5")
        break  # Stop loop
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Write a program to check if a user's age is greater than 18. Print "Adult" or "Minor".
# 2. Use a for loop to print the multiplication table of 5 (5, 10, 15... 50).
# 3. Write a while loop that keeps asking the user for input until they type "stop".
# 4. Use a loop to sum all numbers from 1 to 100.

# ---------------------------------------------------------
# Solutions
# ---------------------------------------------------------
print("\n--- Practice Solutions ---")

# 1. Age Check
age = int(input("Enter your age: "))
if age > 18:
    print("Adult")
else:
    print("Minor")

# 2. Multiplication Table
print("\nTable of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# 3. While Loop (Input)
print("\nType 'stop' to end:")
while True:
    user_input = input("Input: ")
    if user_input.lower() == "stop":
        break

# 4. Sum 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(f"\nSum of 1 to 100 is: {total}")
