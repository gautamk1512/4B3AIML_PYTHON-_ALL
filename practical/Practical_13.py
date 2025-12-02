# Question:
# A program that reads a text file and counts the number of words in it.

# Explanation:
# The program opens a text file in read mode, reads its content, splits the text into words, and counts them.
# Note: This script creates a dummy file 'sample.txt' first if it doesn't exist.

# Code Breakdown:
# 1. Import `os` module to check for file existence.
# 2. Define the `filename`.
# 3. Check if file exists. If not, create it and write sample text so the program can run.
# 4. Use `try...except` block to handle `FileNotFoundError`.
# 5. Open file in 'read' mode (`"r"`).
# 6. Read entire content into a string variable `content`.
# 7. Split content by whitespace into a list of words using `.split()`.
# 8. Print content and the length of the words list.

import os

filename = "sample.txt"

# 3. Create Dummy File (if missing)
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("This is a sample text file used for counting words.")
    print(f"Created {filename}")

# 4. Read and Count
try:
    # 5. Open File
    with open(filename, "r") as file:
        # 6. Read Content
        content = file.read()
        # 7. Split into Words
        words = content.split()
        
        # 8. Output
        print(f"Content: {content}")
        print(f"Total word count: {len(words)}")

except FileNotFoundError:
    print(f"File {filename} not found.")
