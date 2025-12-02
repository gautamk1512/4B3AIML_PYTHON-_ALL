# Question:
# A program that calculates the area and perimeter of a rectangle.

# Explanation:
# The area is calculated as Length x Width.
# The perimeter is calculated as 2 x (Length + Width).

# Code Breakdown:
# 1. Take user input for `length` and convert to float.
# 2. Take user input for `width` and convert to float.
# 3. Calculate `area` by multiplying length and width.
# 4. Calculate `perimeter` by adding length and width, then multiplying by 2.
# 5. Print the calculated Area.
# 6. Print the calculated Perimeter.

# 1. Input Length
length = float(input("Enter the length of the rectangle: "))

# 2. Input Width
width = float(input("Enter the width of the rectangle: "))

# 3. Calculate Area
area = length * width

# 4. Calculate Perimeter
perimeter = 2 * (length + width)

# 5. Output Area
print(f"Area: {area}")

# 6. Output Perimeter
print(f"Perimeter: {perimeter}")
