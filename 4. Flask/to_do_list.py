from flask import Flask, jsonify,request,render_template

app = Flask(__name__)

# Initial data in the to-do list
items = [
    {'id':1, 'name':'Gym', 'description':'Lift weights in the Gym'},
    {'id':2, 'name':'Job', 'description':'Do well and complete all tasks'}
]

@app.route('/')
def home_page():
    """Root view — simple string response.

    Flask functionality: demonstrates a basic route registration
    (`@app.route`) and returning a plain-string HTTP response.
    """
    return "Welcome to home page"

@app.route('/items')
def get_items():
    """Return a JSON list using Flask's `jsonify` helper.

    Flask functionality: `jsonify` serializes Python objects to JSON
    and returns a `Response` with the `application/json` content type
    ready for API clients.
    """
    return jsonify(items)

@app.route('/items/<int:id>')
def get_item(id):
    """Demonstrate a variable URL segment to fetch a single item.

    Flask functionality: `<int:id>` captures a path parameter and
    passes it as the `id` argument. Views can return JSON or error
    responses depending on application logic.
    """
    for item in items:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({"error":f"No item found with id : {id}"})


@app.route('/items',methods = ['POST'])
def create_item():
    """Create a new resource using POSTed JSON.

    Flask functionality: `request.get_json()` or `request.json` reads
    JSON payloads sent by clients. Using `methods=['POST']` tells
    Flask to accept POST; the view returns JSON confirming the
    operation. For proper APIs also return appropriate HTTP status
    codes (201 for created) — this example keeps it simple.
    """
    if not request.json or 'name' not in request.json:
        return jsonify({"error":"Item not found"})
    new_item = {
        'id':items[-1]["id"] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(new_item)
    return jsonify({"message":"Item appended successfully"})


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """Update an existing resource via PUT.

    Flask functionality: `methods=['PUT']` triggers this view for PUT
    requests. `request.get_json()` parses the JSON body into Python
    data to perform updates; the view should return JSON and proper
    status codes to indicate success or failure.
    """
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])

    return jsonify({
        "message": "Item has been updated successfully",
        "item": item
    }), 200


@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
    """Delete a resource using the DELETE method.

    Flask functionality: `methods=['DELETE']` allows HTTP DELETE
    requests to trigger this view. The view returns a JSON result to
    indicate the outcome; production APIs often return `204 No Content`
    on successful deletion.
    """
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result":"Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)