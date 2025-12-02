"""
Topic: Introduction to Popular Python Libraries

Explanation:
Python has a vast ecosystem of libraries. Here are a few key ones:
1. Data Analysis: pandas, numpy, matplotlib.
2. Web Development: Flask, Django.
3. Game Development: Pygame.
"""

# Code Breakdown:
# 1. NumPy Example: Creating an array and performing math.
# 2. Pandas Example: Creating a DataFrame (Table).
# 3. Matplotlib Example: Plotting a simple graph code (commented out as it requires GUI).

# Note: These libraries must be installed via pip (e.g., `pip install numpy pandas`)
# We wrap imports in try-except blocks so this script runs even if they aren't installed.

print("--- Popular Libraries Demo ---")

# 1. NumPy
try:
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy Array: {arr}")
    print(f"Mean: {np.mean(arr)}")
except ImportError:
    print("NumPy not installed. Run `pip install numpy`")

# 2. Pandas
try:
    import pandas as pd
    data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
    df = pd.DataFrame(data)
    print("\nPandas DataFrame:")
    print(df)
except ImportError:
    print("\nPandas not installed. Run `pip install pandas`")

# 3. Game Dev (Conceptual)
print("\nFor Game Dev, use Pygame:")
print("import pygame\npygame.init()\n# Game loop code...")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. (Conceptual) What command do you run in the terminal to install the `pandas` library?
# 2. Use `numpy` to create a 2x2 matrix of ones.
# 3. Use `pandas` to create a Series from a list of numbers `[10, 20, 30]`.
# 4. (Conceptual) Name three Python libraries used for data science.
