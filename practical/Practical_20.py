# Question:
# A program that creates a web application that accepts user input and sends it to a server-side script for processing.

# Explanation:
# Uses Flask. The user inputs a number, and the server processes it (squares it) and returns the result.

# Code Breakdown:
# 1. Import Flask.
# 2. Define HTML form.
#    - Method POST.
#    - Input field named `number`.
#    - Conditional block `{% if result ... %}` to display output.
# 3. Define `/` route.
#    - Initialize `result` to None.
#    - If POST request:
#      - Get `number` from form.
#      - Convert to float and calculate square.
#      - Handle `ValueError` if input is not a number.
#    - Render template with `result`.
# 4. Run app.

from flask import Flask, request, render_template_string

app = Flask(__name__)

# 2. HTML Template
html = """
<h1>Number Processor</h1>
<form method="POST">
    Enter a number: <input type="number" name="number">
    <input type="submit" value="Process">
</form>
{% if result is not none %}
    <h2>Result: {{ result }}</h2>
{% endif %}
"""

# 3. Index Route
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Process Input
            number = float(request.form['number'])
            result = f"The square of {number} is {number ** 2}"
        except ValueError:
            result = "Please enter a valid number."
            
    # Render
    return render_template_string(html, result=result)

# 4. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
