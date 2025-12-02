"""
Topic: Django Forms, Static Files, and Deployment

Explanation:
1. Forms (`forms.py`): Handling user input securely.
   - `ModelForm`: Creates a form automatically from a Model.
2. Static Files: CSS, JavaScript, Images.
   - `STATIC_URL`: URL prefix.
   - `STATICFILES_DIRS`: Locations of static files.
   - `{% load static %}` in templates.
3. Deployment:
   - `DEBUG = False` in production.
   - Use `ALLOWED_HOSTS`.
   - Use WSGI (Gunicorn) + Nginx/Apache.
"""

# Code Breakdown:
# 1. Example `forms.py`.
# 2. Example View handling the form.
# 3. Static file usage in template.

print("--- Django Forms & Extras ---")

# --- 1. forms.py ---
print("\n# forms.py")
print("""
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
""")

# --- 2. views.py (Form Handling) ---
print("\n# views.py")
print("""
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
""")

# --- 3. Template with Static Files ---
print("\n# base.html")
print("""
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
""")
