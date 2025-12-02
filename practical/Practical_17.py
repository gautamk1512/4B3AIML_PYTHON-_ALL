# Question:
# A program that creates a web application that allows users to register and login.

# Explanation:
# This uses `Flask` to create a web app with routes for registration and login.
# It uses a simple dictionary `users` to store credentials in memory (for demonstration).

# Code Breakdown:
# 1. Import Flask and related functions.
# 2. Create Flask app instance.
# 3. Define `users` dictionary to store username:password pairs.
# 4. Define HTML strings for Home, Register, and Login pages (embedded for simplicity).
# 5. Define `/` route (Home) returning links to Register/Login.
# 6. Define `/register` route (GET/POST).
#    - If POST: Get form data, check existence, save to `users`, redirect to login.
#    - If GET: Show registration form.
# 7. Define `/login` route (GET/POST).
#    - If POST: Check credentials against `users` dict. Return Welcome or Error.
#    - If GET: Show login form.
# 8. Run the app on localhost:5000.

from flask import Flask, request, render_template_string, redirect, url_for

# 2. App Instance
app = Flask(__name__)
# 3. In-memory User Store
users = {}

# 4. HTML Templates
home_html = """
<h1>Welcome</h1>
<a href="/register">Register</a> | <a href="/login">Login</a>
"""

register_html = """
<h1>Register</h1>
<form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Register">
</form>
"""

login_html = """
<h1>Login</h1>
<form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
</form>
"""

# 5. Home Route
@app.route('/')
def home():
    return home_html

# 6. Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "User already exists!"
        users[username] = password
        return redirect(url_for('login'))
    return register_html

# 7. Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            return f"<h1>Welcome back, {username}!</h1>"
        return "Invalid credentials!"
    return login_html

# 8. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
