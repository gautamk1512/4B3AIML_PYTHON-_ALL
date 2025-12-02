# Question:
# A program that reads an Excel file and prints the data in a tabular format.

# Explanation:
# The program uses `pandas` to read an Excel file easily and print it.
# Note: Requires `pandas` and `openpyxl` installed (`pip install pandas openpyxl`).

# Code Breakdown:
# 1. Import `pandas` and `os`.
# 2. Create a dummy Excel file using a DataFrame if it doesn't exist.
# 3. Use `try...except` to catch errors (like missing libraries).
# 4. Check if file exists using `os.path.exists`.
# 5. Use `pd.read_excel()` to load data into a DataFrame.
# 6. Print the DataFrame (Pandas formats it as a table automatically).

import pandas as pd
import os

filename = "data.xlsx"

# 2. Create Dummy Excel
if not os.path.exists(filename):
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 22], 'City': ['NY', 'LA', 'SF']}
    df = pd.DataFrame(data)
    try:
        # Requires openpyxl
        df.to_excel(filename, index=False)
        print(f"Created {filename}")
    except Exception as e:
        print(f"Error creating Excel file (need openpyxl): {e}")

# 3. Read and Print
try:
    # 4. Check Existence
    if os.path.exists(filename):
        # 5. Read Excel
        df = pd.read_excel(filename)
        print("Excel Data:")
        # 6. Print Table
        print(df)
    else:
        print("Excel file creation failed or file missing.")
except Exception as e:
    print(f"Error reading Excel file: {e}")
    print("Ensure pandas and openpyxl are installed: pip install pandas openpyxl")
