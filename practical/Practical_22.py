# Question:
# A program that creates a web application that supports AJAX requests and updates the page without reloading.

# Explanation:
# This app uses JavaScript (fetch API) on the client side to send an AJAX request to the Flask server.
# The server returns JSON data, and the JavaScript updates the DOM without a page reload.

# Code Breakdown:
# 1. Import Flask and `jsonify`.
# 2. Define HTML template with JavaScript.
#    - `getData()` function calls `fetch('/data')`.
#    - Updates `<div id="result">` with response JSON.
# 3. Define `/` route to serve HTML.
# 4. Define `/data` route.
#    - Returns a JSON response: `{"message": "..."}`.
# 5. Run app.

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# 2. HTML with JavaScript (AJAX)
html = """
<!DOCTYPE html>
<html>
<body>
    <h1>AJAX Demo</h1>
    <button onclick="getData()">Get Data</button>
    <div id="result"></div>

    <script>
        function getData() {
            // Call Server Asynchronously
            fetch('/data')
                .then(response => response.json())
                .then(data => {
                    // Update DOM
                    document.getElementById('result').innerHTML = "Server says: " + data.message;
                });
        }
    </script>
</body>
</html>
"""

# 3. Index Route
@app.route('/')
def index():
    return render_template_string(html)

# 4. Data Route (JSON API)
@app.route('/data')
def data():
    return jsonify({"message": "Hello from the server via AJAX!"})

# 5. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
