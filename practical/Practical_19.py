# Question:
# A program that creates a web application that displays data from a database in a tabular format.

# Explanation:
# Uses Flask and SQLite to display data.
# It creates a dummy database 'test.db', inserts data, and renders it in an HTML table.

# Code Breakdown:
# 1. Import `sqlite3` and Flask functions.
# 2. Initialize Flask app and DB name.
# 3. Define `init_db` function to setup database.
#    - Connect to SQLite DB.
#    - Create table `students` if not exists.
#    - Check if empty; if so, insert dummy data.
#    - Commit and close.
# 4. Call `init_db()` to ensure DB is ready.
# 5. Define HTML template with a loop `{% for row in rows %}` to generate table rows.
# 6. Define `/` route.
#    - Connect to DB.
#    - Select all records from `students`.
#    - Pass records (`rows`) to template.
# 7. Run app.

import sqlite3
from flask import Flask, render_template_string

app = Flask(__name__)
DB_NAME = "test.db"

# 3. Database Setup
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Create Table
    c.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade TEXT)''')
    # Insert Dummy Data
    c.execute('SELECT count(*) FROM students')
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO students (name, grade) VALUES ('Alice', 'A')")
        c.execute("INSERT INTO students (name, grade) VALUES ('Bob', 'B')")
        c.execute("INSERT INTO students (name, grade) VALUES ('Charlie', 'A-')")
        conn.commit()
    conn.close()

# 4. Run Setup
init_db()

# 5. HTML Template
html = """
<h1>Student Database</h1>
<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Grade</th>
    </tr>
    {% for row in rows %}
    <tr>
        <td>{{ row[0] }}</td>
        <td>{{ row[1] }}</td>
        <td>{{ row[2] }}</td>
    </tr>
    {% endfor %}
</table>
"""

# 6. Index Route
@app.route('/')
def index():
    # Fetch Data
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    conn.close()
    # Render
    return render_template_string(html, rows=rows)

# 7. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
