from dbmanager import DbManager
import mysql.connector
import json

class Product:

    @staticmethod
    def connector():
        try:
            db_manager = DbManager("localhost", 3306, "alice", "pass_db1616!", "ecommerce5E")
            conn = db_manager.connect()
            return conn
        except mysql.connector.Error as e:
            print("Errore durante la connessione al database:", str(e))
            
    def __init__(self, id, nome, prezzo, marca):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.marca = marca
    
    @property
    def id(self):
        return self._id

    @id.setter #togliere
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, value):
        self._prezzo = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @staticmethod
    def fetchAll(): #ok
        try: 
            conn = Product.connector()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            records = cursor.fetchall()
            cursor.close()
            return records
        except mysql.connector.Error as e:
            print("Errore durante la ricerca dei prodotti:", str(e))

    @staticmethod
    def find(id): #ok
        try:
            conn = Product.connector()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return Product(id=row[0], nome=row[1], prezzo=row[2], marca=row[3])
            else:
                return None
        except mysql.connector.Error as e:
            print("Errore durante la ricerca del prodotto:", str(e))
            

    @staticmethod
    def create(product_data): #ok
        try:
            conn = Product.connector()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (nome, prezzo, marca) VALUES (%s, %s, %s)", (product_data['nome'], product_data['prezzo'], product_data['marca']))
            conn.commit()
            product_id = cursor.lastrowid
            conn.close()
            product_data['id'] = product_id
            return product_data
        except mysql.connector.Error as e:
            print("Errore durante la creazione del prodotto:", str(e))

    def update(self, product_data): #ok
        try:
            conn = Product.connector()
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET marca = %s, nome = %s, prezzo = %s WHERE id = %s", (product_data['marca'], product_data['nome'], product_data['prezzo'], self.id,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print("Errore durante l'aggiornamento del prodotto:", str(e))
            
    def delete(self): #ok
        try:
            conn = Product.connector()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = %s", (self.id,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print("Errore durante l'eliminazione del prodotto:", str(e))

