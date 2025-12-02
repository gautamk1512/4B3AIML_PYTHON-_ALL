# Question:
# A program that calculates the factorial of a number.

# Explanation:
# The factorial of a number n (n!) is the product of all positive integers less than or equal to n.
# E.g., 5! = 5 * 4 * 3 * 2 * 1 = 120.

# Code Breakdown:
# 1. Take user input for `num` and convert to integer.
# 2. Initialize variable `fact` to 1 (since multiplying by 0 would zero out the result).
# 3. Use a `for` loop ranging from 1 to `num + 1`.
# 4. In each iteration, multiply `fact` by the current number `i`.
# 5. After the loop finishes, print the calculated factorial.

# 1. Input Number
num = int(input("Enter a number: "))

# 2. Initialize Result
fact = 1

# 3. Loop from 1 to num
for i in range(1, num + 1):
    # 4. Multiply current i with accumulated fact
    fact *= i

# 5. Output Result
print(f"Factorial of {num} is {fact}")
