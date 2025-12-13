"""
Topic: Introduction to Django Framework

Explanation:
1. Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design. "Batteries included" (Auth, Admin, DB ORM included).
2. Installation:
   - Virtual Env: `python -m venv venv` -> Activate.
   - Install: `pip install django`
3. Project Creation Phases:
   - Create Project: `django-admin startproject myproject`
   - Run Server: `python manage.py runserver`
   - Create App: `python manage.py startapp myapp`
4. Structure:
   - `manage.py`: Command-line utility.
   - `settings.py`: Configuration (DB, Apps, Middleware).
   - `urls.py`: URL declarations.
"""

# Code Breakdown:
# This file contains command-line instructions and an example of `settings.py` configuration.
# Since Django is project-based, we cannot run it as a single script.

print("--- Django Setup Instructions ---")
print("1. Install: pip install django")
print("2. Start Project: django-admin startproject mysite")
print("3. Enter Directory: cd mysite")
print("4. Run Server: python manage.py runserver")

print("\n--- settings.py Snippet (Configuration) ---")
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'myapp',  # Add your app here
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. (Conceptual) What is the command to create a new Django app named `store`?
# 2. (Conceptual) In which file do you register your installed apps?
# 3. (Conceptual) What is the purpose of `manage.py`?
# 4. Create a new Django project `my_portfolio` and run the server.

# Solutions
print("\n--- Practice Solutions ---")

# 1. Create App
print("Command: python manage.py startapp store")

# 2. Register Apps
print("File: settings.py (INSTALLED_APPS list)")

# 3. manage.py
print("Purpose: CLI utility to interact with the Django project (run server, make migrations, etc.).")

# 4. New Project
print("Commands:\n1. django-admin startproject my_portfolio\n2. cd my_portfolio\n3. python manage.py runserver")

