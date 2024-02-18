from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Lista di prodotti (simulazione di un database)
products = [
    {"id": "10", "marca": "Adidas", "nome": "superstar", "prezzo": "10"},
    {"id": "11", "marca": "Adidas", "nome": "Adifoam", "prezzo": "20"}
]

# Funzione di supporto per trovare un prodotto per ID
def find_product_by_id(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

# Listare tutti i prodotti
@app.route('/products', methods=['GET'])
def get_products():
    response = {
        "data": [{"type": "products", "id": product['id'], "attributes": product} for product in products]
    }
    return jsonify(response), 200

# Creare un prodotto
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json.get('data')
    new_product = data['attributes']
    new_product['id'] = str(len(products) + 1)  # Genera un ID univoco
    products.append(new_product)
    location = f"/products/{new_product['id']}"
    response = {
        "data": {"type": "products", "id": new_product['id'], "attributes": new_product}
    }
    return jsonify(response), 201, {'Location': location}

# Modificare un prodotto
@app.route('/products/<string:product_id>', methods=['PATCH'])
def update_product(product_id):
    product = find_product_by_id(product_id)
    if product:
        data = request.json.get('data')
        new_attributes = data['attributes']
        product.update(new_attributes)
        response = {
            "data": {"type": "products", "id": product_id, "attributes": product}
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Prodotto non trovato"}), 404

# Mostrare un prodotto
@app.route('/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    product = find_product_by_id(product_id)
    if product:
        response = {
            "data": {"type": "products", "id": product_id, "attributes": product}
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Prodotto non trovato"}), 404

# Eliminare un prodotto
@app.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = find_product_by_id(product_id)
    if product:
        products.remove(product)
        return '', 204
    else:
        return jsonify({"error": "Prodotto non trovato"}), 404

if __name__ == '__main__':
    app.run(debug=True)
