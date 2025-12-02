# Question:
# A program that sorts a list of numbers in ascending or descending order.

# Explanation:
# The program takes a list of numbers and a sorting order preference.
# It uses the list method `.sort()` to organize the numbers in place.

# Code Breakdown:
# 1. Take user input for numbers as a space-separated string, split it, and map to float.
# 2. Convert the map object to a list `numbers`.
# 3. Ask user for `order` ("asc" or "desc").
# 4. Check if order is "asc" (Ascending).
#    - Call `numbers.sort()` (default is ascending).
#    - Print result.
# 5. Check if order is "desc" (Descending).
#    - Call `numbers.sort(reverse=True)`.
#    - Print result.
# 6. Handle invalid input.

# 1 & 2. Input Numbers
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

# 3. Input Sort Order
order = input("Enter sort order (asc/desc): ").lower()

# 4. Ascending Check
if order == "asc":
    numbers.sort()
    print("Sorted list (Ascending):", numbers)

# 5. Descending Check
elif order == "desc":
    numbers.sort(reverse=True)
    print("Sorted list (Descending):", numbers)

# 6. Invalid Input
else:
    print("Invalid sort order!")
