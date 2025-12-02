# Question:
# A program that checks if a given year is a leap year.

# Explanation:
# A leap year is divisible by 4.
# However, if it is divisible by 100, it must also be divisible by 400 to be a leap year.

# Code Breakdown:
# 1. Take user input for `year` and convert to integer.
# 2. Check if year is divisible by 4 AND (not divisible by 100 OR divisible by 400).
#    - `year % 4 == 0`: Basic leap year check.
#    - `year % 100 != 0`: Excludes century years like 1900.
#    - `year % 400 == 0`: Includes quad-century years like 2000.
# 3. If condition is true, print that it IS a leap year.
# 4. Else, print that it is NOT a leap year.

# 1. Input Year
year = int(input("Enter a year: "))

# 2. Check Conditions
# (Divisible by 4 AND NOT 100) OR (Divisible by 400)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # 3. True case
    print(f"{year} is a leap year.")
else:
    # 4. False case
    print(f"{year} is not a leap year.")
