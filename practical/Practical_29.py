# Question:
# A program that creates a RESTful API that paginates the results of a query to improve performance.

# Explanation:
# The API endpoint accepts `page` and `limit` query parameters to slice the data returned.
# Default is page 1, limit 5.

# Code Breakdown:
# 1. Import Flask.
# 2. Generate dummy data (list of 100 dicts).
# 3. Define `/items` route.
#    - Get `page` arg (default 1).
#    - Get `limit` arg (default 10).
#    - Calculate `start` index: `(page - 1) * limit`.
#    - Calculate `end` index: `start + limit`.
#    - Slice list `items[start:end]`.
#    - Return JSON with metadata (total items, total pages) and data.
# 4. Run app.

from flask import Flask, jsonify, request

app = Flask(__name__)

# 2. Generate dummy data (100 items)
items = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]

# 3. Paginated Endpoint
@app.route('/items', methods=['GET'])
def get_items():
    # Get query parameters
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    
    # Calculate indices
    start = (page - 1) * limit
    end = start + limit
    
    # Slice data
    paginated_items = items[start:end]
    
    # Return Response
    return jsonify({
        "page": page,
        "limit": limit,
        "total_items": len(items),
        "total_pages": (len(items) + limit - 1) // limit,
        "data": paginated_items
    })

# 4. Run App
if __name__ == '__main__':
    print("Running Pagination API on http://127.0.0.1:5000/items")
    print("Try: http://127.0.0.1:5000/items?page=2&limit=5")
    app.run(debug=True)
