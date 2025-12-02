# Question:
# A program that creates a web application that uses Django's built-in debugging features to troubleshoot errors and exceptions.

# Explanation:
# Since this is a single-file script, we will simulate this using Flask's debugger, which is very similar in concept (interactive traceback).
# Django projects typically require multiple files/folders.
# To see the debugger, run this script and visit http://127.0.0.1:5000/error

# Code Breakdown:
# 1. Import Flask.
# 2. Enable Debug Mode: `app.config['DEBUG'] = True`.
#    - This shows detailed tracebacks in the browser on error.
# 3. Define `/` route.
#    - Links to the error page.
# 4. Define `/error` route.
#    - Intentionally raises a `ZeroDivisionError` (`1 / 0`).
# 5. Run app.

from flask import Flask

app = Flask(__name__)

# 2. Enable Debugger
app.config['DEBUG'] = True

# 3. Home Route
@app.route('/')
def home():
    return "<h1>Go to <a href='/error'>/error</a> to see the debugger in action.</h1>"

# 4. Error Trigger Route
@app.route('/error')
def error():
    # This division by zero will cause an exception
    # The debugger will appear in the browser
    x = 1 / 0
    return "This will never be reached"

# 5. Run App
if __name__ == '__main__':
    print("Running with Debugger ON. Visit /error to test.")
    app.run(debug=True)
