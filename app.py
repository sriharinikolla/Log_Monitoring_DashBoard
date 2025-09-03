from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate API responses
products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Smartphone", "price": 50000},
    {"id": 3, "name": "Headphones", "price": 3000}
]

orders = []

@app.route('/')
def home():
    return "Flask API is running!", 200

# Login API
@app.route('/api/login', methods=['GET'])
def login():
    return jsonify({"message": "User logged in successfully"}), 200

# Logout API
@app.route('/api/logout', methods=['GET'])
def logout():
    return jsonify({"message": "User logged out successfully"}), 200

# Get Products API
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Create Order API
@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    if "product_id" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid order data"}), 400
    new_order = {"id": len(orders) + 1, "product_id": data["product_id"], "quantity": data["quantity"]}
    orders.append(new_order)
    return jsonify({"message": "Order placed successfully", "order": new_order}), 201

# Get Orders API
@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

# Status API
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "API is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
