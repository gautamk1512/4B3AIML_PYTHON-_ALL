# Topic 06: Numbers

# Questions
# 1. What are the different number systems in Python?
# 2. How do you convert between number systems?

# Notes
# Decimal, Binary, Octal, Hexadecimal
# Conversion: bin(), oct(), hex(), int()

# Solutions
n = 42
binary = bin(n)
octal = oct(n)
hexadecimal = hex(n)
print(binary, octal, hexadecimal)
binary_str = '101010'
decimal = int(binary_str, 2)
print(decimal)
