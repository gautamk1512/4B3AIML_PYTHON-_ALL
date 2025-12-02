# Question:
# A program that creates a web application that implements user authentication and authorization.

# Explanation:
# Implements a simple login system using Flask-Login (simulated here with session for simplicity in one file).
# Authorization: Only logged-in users can access the 'dashboard'.

# Code Breakdown:
# 1. Import Flask, session, and related functions.
# 2. Set `app.secret_key` (required for session security).
# 3. Define `USERS` dict (mock database).
# 4. Define HTML templates for Login and Dashboard.
# 5. Define `/` (Login) route.
#    - If POST: Validate username/password.
#    - If valid: Store username in `session['user']` and redirect to Dashboard.
# 6. Define `/dashboard` route (Protected).
#    - Check if 'user' is in `session`.
#    - If yes: Show dashboard.
#    - If no: Redirect to Login.
# 7. Define `/logout` route.
#    - Remove 'user' from `session`.
#    - Redirect to Login.
# 8. Run app.

from flask import Flask, session, redirect, url_for, request, render_template_string
import os

app = Flask(__name__)
# 2. Secret Key
app.secret_key = os.urandom(24)

# 3. Mock User DB
USERS = {"admin": "secret"}

# 4. Templates
login_html = """
<h1>Login</h1>
<form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
</form>
"""

dashboard_html = """
<h1>Dashboard</h1>
<p>Welcome, {{ username }}!</p>
<p>This is a protected area.</p>
<a href="/logout">Logout</a>
"""

# 5. Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate
        if username in USERS and USERS[username] == password:
            # Authorize (Set Session)
            session['user'] = username
            return redirect(url_for('dashboard'))
        return "Invalid credentials"
    return login_html

# 6. Dashboard Route (Protected)
@app.route('/dashboard')
def dashboard():
    # Check Authorization
    if 'user' in session:
        return render_template_string(dashboard_html, username=session['user'])
    return redirect(url_for('login'))

# 7. Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# 8. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    print("Use username: 'admin' and password: 'secret'")
    app.run(debug=True)
