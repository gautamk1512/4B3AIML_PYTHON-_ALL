"""
Topic: Tools (PyCharm, Git) and Database Connectivity (MySQL, MongoDB)

Explanation:
1. PyCharm IDE: Integrated Development Environment with code completion, debugging, and Git integration.
   - Git Integration: VCS menu -> Enable Version Control Integration -> Select Git.
2. PyTests: Framework for writing test cases.
3. Databases:
   - MySQL (Relational): Uses `mysql-connector-python`.
   - MongoDB (NoSQL): Uses `pymongo`.
"""

# Code Breakdown:
# 1. Git Usage (Comments): How to init, add, commit, push.
# 2. PyTest Example: A simple test function.
# 3. MySQL Connection Example (Skeleton code).
# 4. MongoDB Connection Example (Skeleton code).

# --- 1. Git Commands ---
"""
Git Integration in PyCharm / Terminal:
1. Initialize: `git init`
2. Add Files: `git add .`
3. Commit: `git commit -m "Initial commit"`
4. Push: `git push origin master`
"""
print("Git commands explained in comments.")

# --- 2. PyTest ---
def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    print("Test Passed!")

# To run tests: `pytest filename.py`
print("\nPyTest function defined. Run via `pytest`.")

# --- 3. MySQL Connectivity ---
print("\n--- MySQL Connectivity (Example) ---")
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
for x in mycursor:
  print(x)
"""

# --- 4. MongoDB Connectivity ---
print("\n--- MongoDB Connectivity (Example) ---")
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()
print(x)
"""

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. (Conceptual) What is the Git command to check the status of your files?
# 2. Write a PyTest function `test_sub()` to test a `subtract(a, b)` function.
# 3. (Conceptual) Which Python library is commonly used to connect to a MySQL database?
# 4. (Conceptual) What is the difference between SQL (like MySQL) and NoSQL (like MongoDB)?
