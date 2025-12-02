# Question:
# A program that calculates the average of a list of numbers.

# Explanation:
# The average is the sum of all elements divided by the count of elements.
# The program takes a space-separated string, splits it, converts items to floats, and computes the average.

# Code Breakdown:
# 1. Ask user to input numbers separated by spaces.
# 2. Split the input string into a list of strings.
# 3. Use a list comprehension to convert each string in the list to a float.
# 4. Calculate the sum of the numbers using `sum()`.
# 5. Calculate the count of numbers using `len()`.
# 6. Divide sum by count to get `average`.
# 7. Print the result.

# 1 & 2. Input and Split
numbers_str = input("Enter numbers separated by space: ").split()

# 3. Convert to Floats
numbers = [float(num) for num in numbers_str]

# 4, 5 & 6. Calculate Average
# Check if list is not empty to avoid division by zero
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    # 7. Output
    print(f"Average: {average}")
else:
    print("No numbers entered.")
