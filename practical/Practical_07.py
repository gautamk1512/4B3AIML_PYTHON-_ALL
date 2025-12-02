# Question:
# A program that checks if a given string is a palindrome.

# Explanation:
# A palindrome is a string that reads the same forwards and backwards (e.g., "madam", "racecar").
# We can check this by reversing the string and comparing it to the original.

# Code Breakdown:
# 1. Take user input for the string `s`.
# 2. Reverse the string using slicing `[::-1]`.
#    - `s[start:end:step]`: A step of -1 reverses the string.
# 3. Compare the original string `s` with the reversed string.
# 4. If they are equal, print that it IS a palindrome.
# 5. Else, print that it is NOT a palindrome.

# 1. Input String
s = input("Enter a string: ")

# 2 & 3. Compare Original vs Reversed
if s == s[::-1]:
    # 4. True Case
    print(f"{s} is a palindrome.")
else:
    # 5. False Case
    print(f"{s} is not a palindrome.")
