from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory storage
users = []
id_counter = 1


@app.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    return jsonify(users)


@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    global id_counter

    if not request.json:
        abort(400, description="Request body must be JSON")

    if 'name' not in request.json or 'email' not in request.json:
        abort(400, description="Name and email are required")

    user = {
        'id': id_counter,
        'name': request.json['name'],
        'email': request.json['email'],
        'phone': request.json.get('phone', ""),
        'password': request.json.get('password', ""),
        'address': request.json.get('address', "")
    }

    users.append(user)
    id_counter += 1

    return jsonify(user), 201


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    user = next((u for u in users if u['id'] == user_id), None)

    if user is None:
        abort(404, description="User not found")

    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user details"""
    user = next((u for u in users if u['id'] == user_id), None)

    if user is None:
        abort(404, description="User not found")

    if not request.json:
        abort(400, description="Invalid request body")

    user['name'] = request.json.get('name', user['name'])
    user['email'] = request.json.get('email', user['email'])
    user['phone'] = request.json.get('phone', user['phone'])
    user['password'] = request.json.get('password', user['password'])
    user['address'] = request.json.get('address', user['address'])

    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    global users

    user = next((u for u in users if u['id'] == user_id), None)

    if user is None:
        abort(404, description="User not found")

    users = [u for u in users if u['id'] != user_id]

    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
