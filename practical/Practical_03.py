# Question:
# A program that generates a random password of a specified length.

# Explanation:
# The program uses the `random` and `string` modules to select characters randomly.
# It combines uppercase, lowercase, digits, and symbols to create a secure password.

# Code Breakdown:
# 1. Import the `random` module to generate random selections.
# 2. Import the `string` module to access character sets (letters, digits, punctuation).
# 3. Ask user for the desired password `length` (integer).
# 4. Create a string `characters` containing all letters, digits, and punctuation.
# 5. Use a list comprehension and `random.choice` to pick `length` characters.
# 6. Join the list of characters into a single string `password`.
# 7. Print the generated password.

import random
import string

# 3. Input Length
length = int(input("Enter password length: "))

# 4. Define Character Set
characters = string.ascii_letters + string.digits + string.punctuation

# 5 & 6. Generate Password
# random.choice(characters) picks one char.
# The loop runs 'length' times.
# ''.join combines them.
password = ''.join(random.choice(characters) for _ in range(length))

# 7. Output
print(f"Generated password: {password}")
