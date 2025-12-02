# Question:
# A program that creates a web application that uses a template engine to generate dynamic HTML pages.

# Explanation:
# Flask uses Jinja2 as its default template engine.
# This example passes a list of items and a title to the template to render them dynamically.

# Code Breakdown:
# 1. Import Flask and render_template_string.
# 2. Define the HTML template string using Jinja2 syntax:
#    - `{{ title }}`: Variable substitution.
#    - `{% for item in items %}`: Loop structure.
# 3. Define `/` route.
#    - Set `title` variable.
#    - Create `items` list.
#    - Pass `title` and `items` to `render_template_string`.
# 4. Run app.

from flask import Flask, render_template_string

app = Flask(__name__)

# 2. Template with Jinja2 syntax
template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <h2>Items List:</h2>
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

# 3. Home Route
@app.route('/')
def home():
    title = "My Dynamic Page"
    items = ["Apple", "Banana", "Cherry", "Date"]
    # Pass variables to template
    return render_template_string(template, title=title, items=items)

# 4. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
