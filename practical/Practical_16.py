# Question:
# A program that creates a simple web server and serves a static HTML page.

# Explanation:
# This program uses Python's built-in `http.server` module to serve files from the current directory.
# It creates a simple `index.html` file and starts a server on port 8000.

# Code Breakdown:
# 1. Import `http.server` for server logic, `socketserver` for TCP handling, and `os`.
# 2. Define port (8000) and filename ("index.html").
# 3. Check if `index.html` exists; if not, create it with simple content.
# 4. Set the handler to `SimpleHTTPRequestHandler` (serves files from current dir).
# 5. Print instructions to the user.
# 6. Create a TCPServer object binding to localhost ("") and the defined PORT.
# 7. Use `httpd.serve_forever()` to start the loop waiting for requests.
# 8. Wrap in `try...except KeyboardInterrupt` to allow clean exit with Ctrl+C.

import http.server
import socketserver
import os

PORT = 8000
HTML_FILE = "index.html"

# 3. Create Dummy HTML
if not os.path.exists(HTML_FILE):
    with open(HTML_FILE, "w") as f:
        f.write("<h1>Hello! This is a static HTML page served by Python.</h1>")

# 4. Set Handler
Handler = http.server.SimpleHTTPRequestHandler

# 5. Print Instructions
print(f"Serving at port {PORT}")
print(f"Open http://localhost:{PORT} in your browser")

# 6, 7 & 8. Start Server
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
