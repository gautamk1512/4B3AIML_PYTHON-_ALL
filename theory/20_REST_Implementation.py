"""
Topic: RESTful Implementation, Methods, and Best Practices

Explanation:
1. HTTP Methods (Verbs):
   - GET: Retrieve resource(s). (Safe, Idempotent)
   - POST: Create a new resource. (Not Idempotent)
   - PUT: Update/Replace a resource completely. (Idempotent)
   - PATCH: Update a resource partially.
   - DELETE: Remove a resource. (Idempotent)
2. Resource Naming: Use Nouns, not Verbs.
   - Good: `/users`, `/users/123`
   - Bad: `/getUsers`, `/createUser`
3. Status Codes:
   - 2xx: Success (200 OK, 201 Created)
   - 3xx: Redirection
   - 4xx: Client Error (400 Bad Request, 401 Unauthorized, 404 Not Found)
   - 5xx: Server Error (500 Internal Server Error)
"""

# Code Breakdown:
# 1. Python code using `requests` library to demonstrate how a client calls these methods.
# 2. (Note: This script acts as a Client calling a hypothetical API).

import requests

print("--- REST API Client Demo ---")
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 1. GET (Read)
response = requests.get(BASE_URL)
print(f"GET Status: {response.status_code}")
print(f"Data (First Item): {response.json()[0]}")

# 2. POST (Create)
new_data = {"title": "My New Post", "body": "Content here", "userId": 1}
response = requests.post(BASE_URL, json=new_data)
print(f"\nPOST Status: {response.status_code} (201 = Created)")
print(f"Response: {response.json()}")

# 3. PUT (Update)
update_url = f"{BASE_URL}/1"
updated_data = {"title": "Updated Title", "body": "New content", "userId": 1}
response = requests.put(update_url, json=updated_data)
print(f"\nPUT Status: {response.status_code}")
print(f"Response: {response.json()}")

# 4. DELETE
response = requests.delete(update_url)
print(f"\nDELETE Status: {response.status_code}")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. Use Python `requests` to send a GET request to `https://api.github.com` and print the JSON response.
# 2. Write a script to POST JSON data `{"name": "John", "job": "Developer"}` to `https://reqres.in/api/users`.
# 3. Modify your script to check if the status code is 201 (Created) before printing the response.
# 4. (Conceptual) Why is the DELETE method considered "idempotent"?

# Solutions
print("\n--- Practice Solutions ---")

# 1. GET Request
# import requests
# response = requests.get('https://api.github.com')
# print(response.json())

# 2. POST Request
# payload = {"name": "John", "job": "Developer"}
# response = requests.post('https://reqres.in/api/users', json=payload)
# print(response.json())

# 3. Status Check
# if response.status_code == 201:
#     print(response.json())

# 4. Idempotent
print("Idempotent: Making the same request multiple times has the same effect as making it once (e.g., deleting a resource twice results in the same state: resource is gone).")

