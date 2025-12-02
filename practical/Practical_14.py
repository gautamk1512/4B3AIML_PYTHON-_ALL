# Question:
# A program that reads a CSV file and calculates the average of the values in a specified column.

# Explanation:
# The program uses the `csv` module to read a CSV file.
# It extracts values from a specific column (e.g., 'Score'), converts them to numbers, and calculates the average.

# Code Breakdown:
# 1. Import `csv` and `os` modules.
# 2. Create a dummy CSV file if it doesn't exist (to ensure code runs).
# 3. Initialize `total` and `count` variables.
# 4. Open the CSV file in read mode.
# 5. Use `csv.DictReader` to map columns by header names.
# 6. Loop through each row.
#    - Convert 'Score' column value to float.
#    - Add to `total` and increment `count`.
# 7. Calculate average (Total / Count).
# 8. Print result.

import csv
import os

filename = "data.csv"

# 2. Create Dummy CSV
if not os.path.exists(filename):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Score"])
        writer.writerow(["Alice", "85"])
        writer.writerow(["Bob", "90"])
        writer.writerow(["Charlie", "78"])
    print(f"Created {filename}")

# 3. Initialize Variables
total = 0
count = 0

try:
    # 4. Open CSV
    with open(filename, "r") as file:
        # 5. Read as Dictionary
        reader = csv.DictReader(file)
        
        # 6. Iterate Rows
        for row in reader:
            total += float(row["Score"])
            count += 1
            
    # 7 & 8. Calculate Average and Print
    if count > 0:
        print(f"Average Score: {total / count:.2f}")
    else:
        print("No data found.")

except FileNotFoundError:
    print(f"File {filename} not found.")
