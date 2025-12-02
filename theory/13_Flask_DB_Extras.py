"""
Topic: Flask DB Connectivity, Exceptions, Mail, and Flash Messages

Explanation:
1. Database:
   - SQLite: Built-in, good for dev.
   - MySQL: Production-ready.
   - Connectivity: Use `flask_sqlalchemy` (ORM) or raw SQL connectors.
2. Flash Messages: Temporary messages (e.g., "Login Successful") stored in session.
   - Requires `secret_key`.
3. Mail: Sending emails using `flask-mail`.
4. Error Handling: Custom error pages (404, 500).
"""

# Code Breakdown:
# 1. Configure `secret_key` for session/flash.
# 2. Define Error Handler for 404.
# 3. Demonstrate Flash messaging.
# 4. DB Connection concept (SQLAlchemy).

try:
    from flask import Flask, flash, redirect, url_for, render_template_string

    app = Flask(__name__)
    app.secret_key = 'super_secret_key'

    # --- 1. Flash Messages ---
    @app.route('/')
    def index():
        return '<a href="/success">Click me</a>'

    @app.route('/success')
    def success():
        flash('Operation Successful!')
        return redirect(url_for('show_message'))

    @app.route('/message')
    def show_message():
        # Render template showing flashed messages
        return '''
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            <ul>
            {% for message in messages %}
              <li>{{ message }}</li>
            {% endfor %}
            </ul>
          {% endif %}
        {% endwith %}
        '''

    # --- 2. Error Handling ---
    @app.errorhandler(404)
    def page_not_found(e):
        return "<h1>404 - Page Not Found</h1>", 404

    # --- 3. Database (Conceptual Code) ---
    """
    from flask_sqlalchemy import SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db = SQLAlchemy(app)
    
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
    """

    if __name__ == '__main__':
        app.run(debug=True)

except ImportError:
    print("Flask not installed.")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Create a route that flashes an error message "Invalid Password" and redirects to a login page.
# 2. Write a custom error handler for 500 (Internal Server Error).
# 3. (Conceptual) Which Flask extension is commonly used for database ORM?
# 4. (Conceptual) Why is a `secret_key` required for flash messages?
