"""
Topic: Flask Routing, Templates, Forms, and Static Files

Explanation:
1. Routing: Mapping URLs to functions using `@app.route('/path')`.
2. URL Building: Generating URLs dynamically using `url_for()`.
3. HTTP Methods: Handling GET (retrieve data) and POST (send data).
4. Templates: Using Jinja2 to render HTML files (`render_template`).
   - Folder structure: `templates/` for HTML.
5. Static Files: CSS, JS, Images.
   - Folder structure: `static/`
6. Form Data: Accessing input using `request.form`.
"""

# Code Breakdown:
# 1. Import required functions (Flask, render_template_string, request, url_for).
# 2. Define a route with a variable `<name>` (Dynamic Routing).
# 3. Define a route that handles Methods (GET/POST).
# 4. Demonstrate Form Handling inside the route.

try:
    from flask import Flask, request, render_template_string, url_for

    app = Flask(__name__)

    # --- 1. Routing & URL Building ---
    @app.route('/')
    def index():
        return 'Home Page'

    @app.route('/user/<name>')
    def user(name):
        return f'Hello, {name}!'

    # --- 2. HTTP Methods & Forms ---
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            # Access Form Data
            username = request.form['username']
            return f'Logged in as {username}'
        
        # Simple HTML Form (Usually in a separate .html file in templates/)
        return '''
            <form method="post">
                Username: <input type="text" name="username">
                <input type="submit" value="Login">
            </form>
        '''

    if __name__ == '__main__':
        app.run(debug=True)

except ImportError:
    print("Flask not installed.")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Create a route `/square/<int:number>` that takes a number from the URL and returns its square.
# 2. Create a contact form with fields "Email" and "Message". Handle the POST request to print the data.
# 3. (Conceptual) What is the difference between GET and POST methods?
# 4. (Conceptual) Where should you place your CSS files in a Flask project?

# Solutions
print("\n--- Practice Solutions ---")

# 1. Square Route
# @app.route('/square/<int:number>')
# def square(number):
#     return f"Square of {number} is {number**2}"

# 2. Contact Form
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         email = request.form['email']
#         msg = request.form['message']
#         return f"Sent from {email}: {msg}"
#     return '<form method="post"><input name="email"><input name="message"><input type="submit"></form>'

# 3. GET vs POST
print("GET: Retrieve data (params in URL). POST: Submit data (body).")

# 4. CSS Location
print("CSS files go in the 'static' folder.")

