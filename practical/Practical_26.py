# Question:
# A program that creates a simple RESTful API that returns a list of users in JSON format.

# Explanation:
# Uses Flask to create an API endpoint `/users` that returns a JSON list of user objects.

# Code Breakdown:
# 1. Import Flask and `jsonify` (to convert Python objects to JSON response).
# 2. Initialize Flask app.
# 3. Define `users` list containing dictionary objects (Mock Data).
# 4. Define `/users` route with method `GET`.
#    - `get_users` function returns `jsonify(users)`.
# 5. Run app.

from flask import Flask, jsonify

# 2. App Instance
app = Flask(__name__)

# 3. Dummy Data
users = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"},
    {"id": 3, "name": "Charlie", "role": "User"}
]

# 4. API Endpoint
@app.route('/users', methods=['GET'])
def get_users():
    # Convert list to JSON
    return jsonify(users)

# 5. Run App
if __name__ == '__main__':
    print("Running API on http://127.0.0.1:5000/users")
    app.run(debug=True)
