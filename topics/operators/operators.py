# Topic 04: Operators

# Questions
# 1. List all arithmetic operators in Python.
# 2. What is the difference between `==` and `is`?
# 3. How do you use bitwise operators?
# 4. Give examples of logical operators.
# 5. What are membership and identity operators?
# 6. Explain operator precedence with a code example.

# Notes
# Arithmetic: +, -, *, /, //, %, **
# Comparison: ==, !=, >, <, >=, <=
# Assignment: =, +=, -=, etc.
# Bitwise: &, |, ^, ~, <<, >>
# Logical: and, or, not
# Membership: in, not in
# Identity: is, is not
# Precedence:
# result = 2 + 3 * 4  # result is 14

# Solutions
add = 2 + 3
sub = 5 - 2
mul = 4 * 3
div = 8 / 2
floordiv = 9 // 2
mod = 7 % 3
exp = 2 ** 3
x = [1, 2]
y = [1, 2]
print(x == y)  # True
print(x is y)  # False
bit_and = 5 & 3
bit_or = 5 | 3
bit_xor = 5 ^ 3
bit_not = ~5
bit_lshift = 5 << 1
bit_rshift = 5 >> 1
print(True and False)
print(True or False)
print(not True)
print(2 in [1, 2, 3])
print(2 not in [4, 5, 6])
print(x is y)
print(x is not y)
result = 2 + 3 * 4 # result is 14
