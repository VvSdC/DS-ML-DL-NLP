from flask import Flask, jsonify,request,render_template

app = Flask(__name__)

# Initial data in the to-do list
items = [
    {'id':1, 'name':'Gym', 'description':'Lift weights in the Gym'},
    {'id':2, 'name':'Job', 'description':'Do well and complete all tasks'}
]

@app.route('/')
def home_page():
    return "Welcome to home page"

@app.route('/items')
def get_items():
    return jsonify(items)

@app.route('/items/<int:id>')
def get_item(id):
    for item in items:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({"error":f"No item found with id : {id}"})


@app.route('/items',methods = ['POST'])
def create_item():
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
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result":"Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)