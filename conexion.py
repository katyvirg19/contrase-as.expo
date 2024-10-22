import sqlite3

class Conexion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexion = sqlite3.connect(self.nombre)

    def desconecta(self):
        try:
            self.conexion.close()
        except AttributeError:
            pass
    
    def crear_tablas(self):
        try:
            #CHICAS, EL CURSOR PERMITE NAVEGAR LAS TUPLAS DE LA BD
            cursor = self.conexion.cursor()
            
            #Se debe crear la tabla en caso de que no este creado el regitro
            cursor.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user_username VARCHAR(50) UNIQUE NOT NULL,
                    user_password VARCHAR(50) NOT NULL
                );
                CREATE TABLE IF NOT EXISTS sites (
                    site_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user_id INT NOT NULL,
                    site_name VARCHAR(100) UNIQUE NOT NULL,
                    site_url VARCHAR (100) NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                );
                CREATE TABLE IF NOT EXISTS passwords (
                    password_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    site_id INT NOT NULL,
                    username VARCHAR(50) NOT NULL,
                    password VARCHAR (50) NOT NULL,
                    FOREIGN KEY (site_id) REFERENCES sites (site_id)
                );
                """
            )
        except AttributeError:
            print('Fallo en la conexion de la base de datos antes de crear las tablas')
    
    def registar_usuario(self, username, password):
        try:
            cursor = self.conexion.cursor()

            cursor.execute(
                """
                INSERT INTO users ('user_username', 'user_password') VALUES (?, ?);
                """, username, password)
            
            cursor.connection.commit()
            cursor.close()
        except AttributeError:
            print('Ingreso INCORRECTO DE DATOS')
    
    #COMPLETAR LAS FUNCIONES DE RESTANTES DE DATOS.
    def iniciar_sesion(self, username, password):
        try:
            cursor = self.conexion.cursor()
            #Antes de la consulta utilizo la 'f' para que me permita colocar los parametros USERNAME y PASSWORD en la consulta para verificar si existe el usuario
            cursor.execute(
                f"""
                SELECT user_username, user_password 
                FROM users 
                WHERE user_username like '{username}' AND user_password like '{password};'
            """
            )
            registro = cursor.fetchone()
            
            if registro:
                return True
            else:
                return False
        except ConnectionError:
            print("No se pudo conectar a la BASE DE DATOS")
