"""
Topic: Data Structures (Lists, Sets, Tuples, Dictionaries)

Explanation:
1. List (`[]`): Ordered, mutable collection. Allows duplicates.
2. Tuple (`()`): Ordered, immutable collection. Allows duplicates.
3. Set (`{}`): Unordered, mutable collection. Unique elements only.
4. Dictionary (`{k:v}`): Key-Value pairs. Keys must be unique and immutable.

"""

# Code Breakdown:
# 1. Create a List, add an item, remove an item.
# 2. Create a Tuple, attempt to modify (show error handling).
# 3. Create a Set, add duplicate items (show uniqueness).
# 4. Create a Dictionary, access values, add new key-value pair.

# --- 1. Lists ---
print("--- Lists ---")
my_list = [1, 2, 3, "Apple"]
my_list.append("Banana")      # Add
my_list.remove(2)             # Remove
print(f"List: {my_list}")
print(f"First Item: {my_list[0]}")

# --- 2. Tuples ---
print("\n--- Tuples ---")
my_tuple = (10, 20, 30)
print(f"Tuple: {my_tuple}")
# my_tuple[0] = 15  # This would raise TypeError (Immutable)

# --- 3. Sets ---
print("\n--- Sets ---")
my_set = {1, 2, 2, 3, 4}  # Duplicate '2' will be removed
my_set.add(5)
print(f"Set (Unique): {my_set}")

# --- 4. Dictionaries ---
print("\n--- Dictionaries ---")
student = {
    "name": "John",
    "age": 21,
    "course": "CS"
}
print(f"Student Name: {student['name']}")
student["grade"] = "A"  # Add new pair
print(f"Updated Dict: {student}")
