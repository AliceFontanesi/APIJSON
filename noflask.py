import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from product import Product

class RequestHandler(BaseHTTPRequestHandler):
    
    def _set_response(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/products':
            self.get_products()
        elif self.path.startswith('/products/'):
            parts = self.path.split('/')
            product_id = int(parts[2])
            self.get_product(product_id)
        else:
            self.send_error(404, 'Not Found')

    def get_products(self):
        records = Product.fetchAll()
        keys = ["id", "nome", "prezzo", "marca"]
        products_list = [{key: value for key, value in zip(keys, record)} for record in records]
        
        self._set_response()
        self.wfile.write(json.dumps({'data': products_list}).encode('utf-8'))

    def get_product(self, product_id):
        record = Product.find(product_id)
        if record:
            keys = ["id", "nome", "prezzo", "marca"]
            product_dict = {key: value for key, value in zip(keys, record)}
            self._set_response()
            self.wfile.write(json.dumps(product_dict).encode('utf-8'))
        else:
            self.send_error(404, 'Product Not Found')

    def do_POST(self):
        if self.path == '/products':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            self.create_product(post_data)
        else:
            self.send_error(404, 'Not Found')

    def create_product(self, post_data):
        try:
            data = json.loads(post_data.decode('utf-8'))
            if 'nome' not in data or 'prezzo' not in data or 'marca' not in data:
                self.send_error(400, 'Bad Request - Incomplete Data')
                return
            new_product = {
                'nome': data['nome'],
                'prezzo': data['prezzo'],
                'marca': data['marca']
            }
            product = Product.create(new_product)
            self._set_response(status_code=201)
            self.wfile.write(json.dumps(product).encode('utf-8'))
        except json.JSONDecodeError:
            self.send_error(400, 'Bad Request - Invalid JSON')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
