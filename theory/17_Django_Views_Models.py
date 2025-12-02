"""
Topic: Django Views, URL Mapping, and Templates

Explanation:
1. Views (`views.py`): Functions or classes that process requests and return responses (HTML or JSON).
2. URL Mapping (`urls.py`): Connects URL patterns to View functions.
   - `path('home/', views.home, name='home')`
3. Templates: HTML files with Django Template Language (DTL).
   - Variables: `{{ variable }}`
   - Tags: `{% tag %}` (loops, if-else)
4. Models (`models.py`): Represent database tables.
"""

# Code Breakdown:
# 1. Example View function.
# 2. Example URL configuration.
# 3. Example Template HTML.

print("--- Django MVC (MVT) Components ---")

# --- 1. views.py ---
print("\n# views.py")
print("""
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()  # Fetch all data from DB
    return render(request, 'home.html', {'posts': posts})
""")

# --- 2. urls.py ---
print("\n# urls.py")
print("""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
""")

# --- 3. home.html (Template) ---
print("\n# home.html")
print("""
<h1>Blog Posts</h1>
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
{% endfor %}
""")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Create a view function `about(request)` that renders `about.html`.
# 2. Add a URL pattern in `urls.py` to map `/about/` to the `about` view.
# 3. In a Django template, how would you display the value of a variable named `username`?
# 4. Write a loop in Django Template Language to display a list of items: `['Apple', 'Banana', 'Cherry']`.
