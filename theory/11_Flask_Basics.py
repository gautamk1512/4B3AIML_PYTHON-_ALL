"""
Topic: Introduction to Flask and Web Development

Explanation:
1. Flask: A micro web framework for Python. It is lightweight and easy to use.
2. Virtual Environment: A self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.
   - Why? To avoid dependency conflicts between projects.
   - Create: `python -m venv venv`
   - Activate: `venv\\Scripts\\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Installation: `pip install Flask`
"""

# Code Breakdown:
# 1. Import Flask class.
# 2. Create an instance of the Flask class (`app`).
# 3. Define a route `/` using the `@app.route` decorator.
# 4. Define the function `home()` that returns a string (Response).
# 5. Run the app using `app.run()`.

# Note: You need to install Flask first: `pip install flask`

try:
    from flask import Flask

    # 2. Create App Instance
    app = Flask(__name__)

    # 3. Define Route
    @app.route('/')
    def home():
        # 4. Return Response
        return "Hello! This is my first Flask App."

    # 5. Run App
    if __name__ == '__main__':
        print("Starting Flask Server...")
        # debug=True enables auto-reload on code changes
        app.run(debug=True)

except ImportError:
    print("Flask not installed. Please run: pip install flask")
