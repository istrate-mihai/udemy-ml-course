from flask import Flask, jsonify, request

app = Flask(__name__)

itemList = [
    {'id': 1, 'name': 'Item 1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'This is item 2'},
]

@app.route('/')
def home():
    return 'Welcome to the sample To Do List'

# Get all items
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(itemList)

# Retrieve a specific item by id
@app.route('/items/<int:item_id>', methods = ['GET'])
def get_item(item_id):
    item = next((item for item in itemList if item['id'] == item_id), None)

    if item is None:
        return jsonify({'error': 'item not found'})

    return jsonify(item)

# Post: create a new item
@app.route('/items', methods = ['POST'])
def create_item():

    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'item not found'})

    new_item = {
        'id': itemList[-1]['id'] + 1 if itemList else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }

    itemList.append(new_item)
    return jsonify(new_item)

# Put: update a specific item by id
@app.route('/items/<int:item_id>', methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in itemList if item['id'] == item_id), None)

    if item is None:
        return jsonify({'error': 'item not found'})

    item['name']        = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete: delete a specific item based on it's id
@app.route('/items/<int:item_id>', methods = ['DELETE'])
def delete_item(item_id):
    global itemList
    itemList = [item for item in itemList if item['id'] != item_id]

    return jsonify({'result': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug = True)
