"""
Topic: Working with Strings in Python

Explanation:
1. Strings: Sequences of characters enclosed in single, double, or triple quotes.
2. Indexing & Slicing: Accessing individual characters or substrings.
3. String Methods: Built-in functions to manipulate strings (e.g., upper(), lower(), strip(), replace(), split()).
4. Formatting: Using f-strings (Python 3.6+) to embed expressions inside string literals.
"""

# Code Breakdown:
# 1. Define a sample string.
# 2. Demonstrate indexing (first/last char) and slicing (substrings).
# 3. Use string methods:
#    - `upper()`: Convert to uppercase.
#    - `replace()`: Swap parts of the string.
#    - `split()`: Break string into a list based on a delimiter.
# 4. Use f-strings for dynamic formatting.

# 1. Define String
text = "  Python Programming  "

# 2. Indexing and Slicing
print(f"Original: '{text}'")
print(f"First char: {text.strip()[0]}")  # Strip removes spaces first
print(f"Slice (first 6 chars): {text.strip()[:6]}")

# 3. String Methods
clean_text = text.strip()  # Remove leading/trailing whitespace
print(f"Stripped: '{clean_text}'")
print(f"Uppercase: {clean_text.upper()}")
print(f"Replaced: {clean_text.replace('Python', 'Java')}")

# Splitting
words = clean_text.split(' ')
print(f"Split into list: {words}")

# 4. String Formatting (f-strings)
lang = "Python"
version = 3.12
info = f"{lang} version {version} is powerful."
print(f"\nFormatted Info: {info}")
