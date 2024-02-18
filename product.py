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
    
    # Metodi getter e setter per gli attributi id, name, price e brand
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    @staticmethod
    def fetchAll(): #fatto
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
    def find(id): #fatto
        try:
            conn = Product.connector()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            row = cursor.fetchone()
            conn.close()
            return row
        except mysql.connector.Error as e:
            print("Errore durante la ricerca del prodotto:", str(e))

    
    def delete(self): #rivedere
        try:
            conn = self.connector()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = %s", (self.get_id,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print("Errore durante l'eliminazione del prodotto:", str(e))

    @staticmethod
    def create(product_data): #fatto
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

    @classmethod
    def update(cls, id, nome, prezzo, marca): #rivedere
        try:
            conn = cls.connector()
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET nome = %s, prezzo = %s, marca = %s WHERE id = %s", (nome, prezzo, marca, id))
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print("Errore durante l'aggiornamento del prodotto:", str(e))
