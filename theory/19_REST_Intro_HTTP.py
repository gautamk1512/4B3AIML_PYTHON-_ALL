"""
Topic: Introduction to RESTful APIs and HTTP Protocol

Explanation:
1. REST (Representational State Transfer): An architectural style for designing networked applications.
   - Constraints: Client-Server, Stateless, Cacheable, Layered System, Uniform Interface.
2. API (Application Programming Interface): Allows two software programs to communicate.
3. HTTP Protocol: The foundation of data communication on the web.
   - Request-Response Cycle: Client sends request -> Server processes -> Server sends response.
   - Components: URL, Method (Verb), Headers, Body, Status Code.

"""

# Code Breakdown:
# 1. Conceptual explanation of Client-Server interaction.
# 2. Demonstration of an HTTP Request structure (Conceptual).
# 3. Demonstration of an HTTP Response structure (Conceptual).

print("--- REST API Concepts ---")
print("REST is not a protocol (like HTTP), but a set of architectural constraints.")
print("Resources are identified by URLs (e.g., https://api.example.com/users).")

print("\n--- HTTP Request Structure ---")
print("""
METHOD /path HTTP/1.1
Host: api.example.com
Authorization: Bearer token
Content-Type: application/json

{
    "name": "Alice",
    "age": 25
}
""")

print("\n--- HTTP Response Structure ---")
print("""
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "status": "success"
}
""")

# ---------------------------------------------------------
# Practice Questions
# ---------------------------------------------------------
# 1. (Conceptual) What does "Stateless" mean in the context of REST?
# 2. (Conceptual) Which HTTP method is commonly used to update an existing resource?
# 3. (Conceptual) What status code represents "Resource Not Found"?
# 4. (Conceptual) Explain the difference between `Authentication` and `Authorization`.

# Solutions
print("\n--- Practice Solutions ---")

# 1. Stateless
print("Stateless: The server does not keep track of the client's state between requests. Each request must contain all necessary info.")

# 2. Update Method
print("Method: PUT (for full update) or PATCH (for partial update).")

# 3. Not Found Code
print("Status Code: 404")

# 4. Auth vs Auth
print("Authentication: Verifying identity (Who are you?).")
print("Authorization: Verifying permissions (What can you do?).")

