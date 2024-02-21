import mysql.connector

class DbManager:

    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.username,
                password=self.password,
                database=self.database
            )
            return connection
        except mysql.connector.Error as e:
            print("Errore di connessione al database:", str(e))
            

# Esempio di utilizzo
#db_manager = DbManager("localhost", 3306, "alice", "pass_db1616!", "ecommerce5E")
#conn = db_manager.connect()

#db_manager = DbManager("192.168.2.200", 3306, "fontanesi_alice", "Sevastopol.immodesty.Floyd.", "fontanesi_alice_ecommerce")
#conn = db_manager.connect()

    
