# Question:
# A program that converts a given number from one base to another.

# Explanation:
# Base conversion involves changing the representation of a number (e.g., Decimal to Binary).
# Python provides built-in functions like `bin()`, `oct()`, `hex()` and `int(x, base)` for this.

# Code Breakdown:
# 1. Define function `convert_base` taking number string, current base, and target base.
# 2. Convert the input string `num_str` to a decimal integer using `int(num_str, from_base)`.
# 3. Check `to_base` to decide conversion method.
#    - If 10: Return string of decimal.
#    - If 2: Return binary string (sliced to remove '0b').
#    - If 8: Return octal string (sliced to remove '0o').
#    - If 16: Return hex string (sliced to remove '0x').
# 4. Handle unsupported bases.
# 5. Take user inputs for number, current base, and target base.
# 6. Call function and print result.

def convert_base(num_str, from_base, to_base):
    # 2. Convert to Decimal (Base 10)
    try:
        decimal_num = int(num_str, from_base)
    except ValueError:
        return "Invalid number for the given base."

    # 3. Convert to Target Base
    if to_base == 10:
        return str(decimal_num)
    elif to_base == 2:
        return bin(decimal_num)[2:] # Remove '0b' prefix
    elif to_base == 8:
        return oct(decimal_num)[2:] # Remove '0o' prefix
    elif to_base == 16:
        return hex(decimal_num)[2:] # Remove '0x' prefix
    else:
        # 4. Error Case
        return "Target base not supported in this simple example (use 2, 8, 10, 16)"

# 5. User Inputs
num_str = input("Enter the number: ")
from_base = int(input("Enter current base (e.g., 10, 2, 16): "))
to_base = int(input("Enter target base (e.g., 10, 2, 16): "))

# 6. Execution and Output
result = convert_base(num_str, from_base, to_base)
print(f"Result: {result}")
