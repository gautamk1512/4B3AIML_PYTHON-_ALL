# Question:
# A program that generates a multiplication table for a given number.

# Explanation:
# The program calculates the product of the given number with integers from 1 to 10.
# It uses a loop to iterate and print each step.

# Code Breakdown:
# 1. Take user input for the number `num` (integer).
# 2. Print a header message.
# 3. Start a `for` loop with `i` ranging from 1 to 10 (range(1, 11)).
# 4. Inside the loop, calculate product `num * i`.
# 5. Print the multiplication statement in format "num x i = result".

# 1. Input Number
num = int(input("Enter a number: "))

# 2. Header
print(f"Multiplication Table for {num}:")

# 3. Loop 1 to 10
for i in range(1, 11):
    # 4 & 5. Calculate and Print
    print(f"{num} x {i} = {num * i}")
