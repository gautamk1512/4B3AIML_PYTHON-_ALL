"""
Topic: Django Apps and Admin Console

Explanation:
1. Apps: Django projects are built from "apps". An app is a web application that does something, e.g., a blog, a poll, or a forum.
   - Command: `python manage.py startapp myapp`
2. Structure of an App:
   - `models.py`: Database schema.
   - `views.py`: Logic.
   - `urls.py`: App-specific URLs.
   - `admin.py`: Admin panel config.
3. Admin Console: Built-in interface to manage data.
   - Create Superuser: `python manage.py createsuperuser`
   - Register Models: In `admin.py`, use `admin.site.register(MyModel)`.
"""

# Code Breakdown:
# 1. Example of `models.py`.
# 2. Example of `admin.py` registering the model.

print("--- Django App Structure & Admin ---")

# --- 1. models.py Example ---
print("\n# models.py")
print("""
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
""")

# --- 2. admin.py Example ---
print("\n# admin.py")
print("""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
""")

print("\nTo access admin: Run server and go to http://127.0.0.1:8000/admin")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Create a Django model `Product` with fields `name` (CharField) and `price` (DecimalField).
# 2. Register the `Product` model in `admin.py` so it appears in the Admin interface.
# 3. (Conceptual) How do you create a superuser to access the Django Admin?
# 4. (Conceptual) What method should you override in a model to return a readable string representation?
