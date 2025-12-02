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
