# Question:
# A program that creates a RESTful API that supports data validation and error handling.

# Explanation:
# The API validates input data (e.g., checks if 'email' is valid, 'age' is positive).
# Returns appropriate HTTP status codes and error messages.

# Code Breakdown:
# 1. Import Flask.
# 2. Define `/register` route (POST).
#    - Get JSON.
#    - Validate presence of data.
#    - Validate `username` length.
#    - Validate `email` format.
#    - Validate `age` (type and value).
#    - If all pass, add to list and return 201.
#    - If any fail, return JSON error and 400 Bad Request.
# 3. Define Error Handlers.
#    - 404: Resource Not Found.
#    - 500: Internal Server Error.
# 4. Run app.

from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

# 2. Register Route with Validation
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validation 1: Check Data Existence
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    username = data.get("username")
    email = data.get("email")
    age = data.get("age")
    
    # Validation 2: Username
    if not username or len(username) < 3:
        return jsonify({"error": "Username must be at least 3 chars"}), 400
    
    # Validation 3: Email
    if not email or "@" not in email:
        return jsonify({"error": "Invalid email address"}), 400
        
    # Validation 4: Age
    if not isinstance(age, int) or age < 18:
        return jsonify({"error": "Age must be 18+"}), 400
    
    # Success
    new_user = {"username": username, "email": email, "age": age}
    users.append(new_user)
    return jsonify({"message": "User registered successfully", "user": new_user}), 201

# 3. Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# 4. Run App
if __name__ == '__main__':
    print("Running Validation API on http://127.0.0.1:5000/register")
    app.run(debug=True)
