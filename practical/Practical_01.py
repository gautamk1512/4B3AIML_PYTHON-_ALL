# Question:
# A program that converts temperatures from Fahrenheit to Celsius and vice versa.

# Explanation:
# This program defines two functions to handle the conversion formulas.
# It asks the user to choose the direction of conversion and then performs the calculation.

# Code Breakdown:
# 1. Define function `fahrenheit_to_celsius(f)` taking Fahrenheit input.
# 2. Return calculated Celsius value: (F - 32) * 5/9.
# 3. Define function `celsius_to_fahrenheit(c)` taking Celsius input.
# 4. Return calculated Fahrenheit value: (C * 9/5) + 32.
# 5. Ask user for input `choice` (1 or 2).
# 6. Check if choice is '1'.
# 7. If yes, take float input for Fahrenheit.
# 8. Print result calling `fahrenheit_to_celsius`.
# 9. Check if choice is '2'.
# 10. If yes, take float input for Celsius.
# 11. Print result calling `celsius_to_fahrenheit`.
# 12. Handle invalid input with an `else` block.

def fahrenheit_to_celsius(f):
    # Convert Fahrenheit to Celsius formula
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    # Convert Celsius to Fahrenheit formula
    return (c * 9/5) + 32

# Get user choice
choice = input("Convert (1) Fahrenheit to Celsius or (2) Celsius to Fahrenheit? Enter 1 or 2: ")

if choice == '1':
    # Get Fahrenheit input
    f = float(input("Enter temperature in Fahrenheit: "))
    # Print formatted result
    print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
elif choice == '2':
    # Get Celsius input
    c = float(input("Enter temperature in Celsius: "))
    # Print formatted result
    print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
else:
    # Handle invalid menu choice
    print("Invalid choice.")
