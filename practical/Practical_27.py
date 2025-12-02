# Question:
# A program that creates a RESTful API that allows users to create, read, update, and delete resources (CRUD).

# Explanation:
# Implements CRUD operations for a 'books' resource.
# GET /books - List all
# POST /books - Create new
# PUT /books/<id> - Update
# DELETE /books/<id> - Delete

# Code Breakdown:
# 1. Import Flask, jsonify, request.
# 2. Define `books` list (Mock DB).
# 3. GET `/books`: Return all books.
# 4. POST `/books`:
#    - Get JSON from request (`request.get_json()`).
#    - Assign new ID.
#    - Append to list.
#    - Return new book and 201 Created.
# 5. PUT `/books/<id>`:
#    - Find book by ID.
#    - If not found, return 404.
#    - Update fields from request JSON.
#    - Return updated book.
# 6. DELETE `/books/<id>`:
#    - Filter out book with given ID.
#    - Return success message.
# 7. Run app.

from flask import Flask, jsonify, request

app = Flask(__name__)

# 2. Mock DB
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]

# 3. Read (All)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# 4. Create
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# 5. Update
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    # Find book
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    # Update fields
    data = request.get_json()
    book.update(data)
    return jsonify(book)

# 6. Delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    # Filter list
    books = [b for b in books if b['id'] != id]
    return jsonify({"message": "Book deleted"})

# 7. Run App
if __name__ == '__main__':
    print("Running CRUD API on http://127.0.0.1:5000/books")
    app.run(debug=True)
