# Question:
# A program that creates a web application that integrates with third-party APIs to provide additional functionality.

# Explanation:
# This app connects to a public API (e.g., `api.github.com`) to fetch and display user data.
# Requires `requests` library: `pip install requests`

# Code Breakdown:
# 1. Import `requests` (for HTTP calls) and Flask.
# 2. Define HTML template.
#    - Includes form for username.
#    - Displays user data (`data.login`, `data.name`, etc.) if available.
#    - Displays error if any.
# 3. Define `/` route.
#    - If POST: Get username.
#    - Call `requests.get(url)` to fetch GitHub user data.
#    - Check status code (200 = OK).
#    - Parse JSON response.
#    - Render template with data or error.
# 4. Run app.

import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# 2. HTML Template
html = """
<h1>GitHub User Info Fetcher</h1>
<form method="POST">
    Enter GitHub Username: <input type="text" name="username">
    <input type="submit" value="Get Info">
</form>
{% if data %}
    <h2>User: {{ data.login }}</h2>
    <p>Name: {{ data.name }}</p>
    <p>Public Repos: {{ data.public_repos }}</p>
    <img src="{{ data.avatar_url }}" width="100">
{% elif error %}
    <p style="color:red">{{ error }}</p>
{% endif %}
"""

# 3. Home Route
@app.route('/', methods=['GET', 'POST'])
def home():
    data = None
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            # Call Third-Party API
            response = requests.get(f"https://api.github.com/users/{username}")
            if response.status_code == 200:
                data = response.json()
            else:
                error = "User not found!"
    return render_template_string(html, data=data, error=error)

# 4. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
