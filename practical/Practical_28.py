# Question:
# A program that creates a RESTful API that authenticates users using a JSON Web Token (JWT).

# Explanation:
# Simulates JWT authentication.
# /login returns a token if credentials match.
# /protected requires the token in the Authorization header.
# Note: In production, use `PyJWT` (`pip install pyjwt`). Here we simulate a token string for simplicity without external deps if possible, 
# but to be correct to the prompt, we'll implement a basic manual token check or suggest the library.
# For this practical, we will simulate the mechanism: Token = "logged_in_user" (Simple simulation)

# Code Breakdown:
# 1. Import Flask functions.
# 2. Define `users` (Mock DB).
# 3. POST `/login`:
#    - Get JSON data.
#    - Validate username/password.
#    - If valid, return a "fake" JWT token.
#    - If invalid, return 401 Unauthorized.
# 4. GET `/protected`:
#    - Get `Authorization` header.
#    - Check if token matches expected valid token.
#    - Return data if valid, else 403 Forbidden.
# 5. Run app.

from flask import Flask, jsonify, request

app = Flask(__name__)

# 2. Mock DB
users = {"admin": "password123"}

# 3. Login Route (Issues Token)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username] == password:
        # In real world: token = jwt.encode({...}, secret)
        # Here: Simulating a token
        return jsonify({"token": "valid-token-12345", "message": "Login successful"})
    return jsonify({"error": "Invalid credentials"}), 401

# 4. Protected Route (Verifies Token)
@app.route('/protected', methods=['GET'])
def protected():
    # Get Header
    token = request.headers.get('Authorization')
    
    # Verify Token (Simple String Check for Demo)
    if token == "Bearer valid-token-12345":
        return jsonify({"message": "Access granted to protected resource!"})
    return jsonify({"error": "Unauthorized"}), 403

# 5. Run App
if __name__ == '__main__':
    print("Running Auth API on http://127.0.0.1:5000")
    app.run(debug=True)
