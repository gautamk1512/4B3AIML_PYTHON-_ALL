"""
Topic: Flask Authentication (Flask-Login) and Deployment

Explanation:
1. Authentication: Verifying user identity.
   - `Flask-Login`: Manages user sessions (login/logout).
   - `UserMixin`: Provides default implementations for user class.
   - `login_required`: Decorator to protect routes.
2. Authorization: Checking if user has permission (e.g., Admin vs User).
3. Deployment:
   - Production Server: Use WSGI server like Gunicorn or uWSGI (not `app.run()`).
   - Platforms: Heroku, AWS, PythonAnywhere.
"""

# Code Breakdown:
# 1. Setup Flask-Login (`LoginManager`).
# 2. Define User class inheriting `UserMixin`.
# 3. Create `user_loader` callback.
# 4. Create Login route (logs user in).
# 5. Create Protected route (`@login_required`).
# 6. Create Logout route.

try:
    from flask import Flask, redirect, url_for
    from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

    app = Flask(__name__)
    app.secret_key = 'secret'

    # 1. Setup LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # 2. User Model (Mock DB)
    class User(UserMixin):
        def __init__(self, id):
            self.id = id

    # 3. User Loader
    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    # 4. Login Route
    @app.route('/login')
    def login():
        user = User(id=1)
        login_user(user)
        return 'Logged in! <a href="/dashboard">Go to Dashboard</a>'

    # 5. Protected Route
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return f'Hello User {current_user.id}! <a href="/logout">Logout</a>'

    # 6. Logout Route
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return 'Logged out.'

    if __name__ == '__main__':
        app.run(debug=True)

except ImportError:
    print("Flask-Login not installed. Run: pip install flask-login")
