from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory storage
customers = []
id_counter = 1


@app.route('/customers', methods=['GET'])
def get_customers():
    """Get all customers"""
    return jsonify(customers)


@app.route('/customers', methods=['POST'])
def create_customer():
    """Create a new customer"""
    global id_counter

    if not request.json:
        abort(400, description="Request body must be JSON")

    if 'name' not in request.json or 'email' not in request.json:
        abort(400, description="Name and email are required")

    customer = {
        'id': id_counter,
        'name': request.json['name'],
        'email': request.json['email'],
        'phone': request.json.get('phone', ""),
        'password': request.json.get('password', ""),
        'address': request.json.get('address', "")
    }

    customers.append(customer)
    id_counter += 1

    return jsonify(customer), 201


@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get customer by ID"""
    customer = next((u for u in customers if u['id'] == customer_id), None)

    if customer is None:
        abort(404, description="customer not found")

    return jsonify(customer)


@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update customer details"""
    customer = next((u for u in customers if u['id'] == customer_id), None)

    if customer is None:
        abort(404, description="customer not found")

    if not request.json:
        abort(400, description="Invalid request body")

    customer['name'] = request.json.get('name', customer['name'])
    customer['email'] = request.json.get('email', customer['email'])
    customer['phone'] = request.json.get('phone', customer['phone'])
    customer['password'] = request.json.get('password', customer['password'])
    customer['address'] = request.json.get('address', customer['address'])

    return jsonify(customer)


@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Delete a customer"""
    global customers

    customer = next((u for u in customers if u['id'] == customer_id), None)

    if customer is None:
        abort(404, description="customer not found")

    customers = [u for u in customers if u['id'] != customer_id]

    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
