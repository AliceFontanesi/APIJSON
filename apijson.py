from flask import Flask, jsonify, request, abort
from product import Product

app = Flask(__name__)

# Rotta per elencare tutti i prodotti
@app.route('/products', methods=['GET'])#fatto
def get_products():
    records = Product.fetchAll()
    # Converti i record in una lista di dizionari
    keys = ["id", "nome", "prezzo", "marca"]
    products_list = []
    for record in records:
        product_dict = {key: value for key, value in zip(keys, record)}
        products_list.append(product_dict)
    
    # Converti la lista di dizionari in JSON utilizzando jsonify e restituiscila come risposta
    return jsonify({'data': products_list})


# Rotta per ottenere un singolo prodotto
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    record = Product.find(product_id)
    keys = ["id", "nome", "prezzo", "marca"]
    product_dict = {key: value for key, value in zip(keys, record)}
    return jsonify(product_dict)
    

if __name__ == '__main__':
    app.run(debug=True)
