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
                    user_username VARCHAR(50) NOT NULL,
                    user_password VARCHAR(50) NOT NULL,
                    user_pin INTEGER NOT NULL
                );
                CREATE TABLE IF NOT EXISTS sites (
                    site_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user_id INT NOT NULL,
                    site_name VARCHAR(100) UNIQUE NOT NULL,
                    site_username VARCHAR(50) NOT NULL,
                    site_password VARCHAR (50) NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                );
                """
            )
        except AttributeError:
            print('Fallo en la conexion de la base de datos antes de crear las tablas')
    
    def registar_usuario(self, username, password, pin):
        try:
            cursor = self.conexion.cursor()

            cursor.execute(
                """
                INSERT INTO users ('user_username', 'user_password', 'user_pin') VALUES (?, ?, ?);
                """, (username, password, pin)
            )

            cursor.connection.commit()
            cursor.close()
            print("Usuario creado con exito!")
        except AttributeError:
            print('Ingreso INCORRECTO DE DATOS')
    
    #COMPLETAR LAS FUNCIONES DE RESTANTES DE DATOS.
    def login_db(self, username, password):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
            """
                SELECT user_id, user_username, user_password
                FROM users 
                WHERE user_username = ? AND user_password = ?;
            """, (username, password)
            )
            global registro
            registro = cursor.fetchone()
            
            if registro:
                print("Se encontro una tupla que coincide")
                print(registro)
                return registro
            else:
                print("No se encontro el usuario")
                return None
        except ConnectionError:
            print("No se pudo conectar a la BASE DE DATOS")
    
    def recuperar_pass(self, username, pin):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
            """
                SELECT user_username, user_pin, user_password
                FROM users 
                WHERE user_username = ? AND user_pin = ?;
            """, (username, pin)
            )
            registro = cursor.fetchone()
            print(registro)
            cursor.close()
            if registro:
                return registro[2]
            else:
                return None
        except ConnectionError:
            print("No se pudo conectar a la BASE DE DATOS")\
    
    def registrar_credenciales (self,usuario_id, sitio_nombre, usuario_sitio, password_sitio):
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                """
                INSERT INTO sites ('user_id','site_name', 'site_username', 'site_password') VALUES (?, ?, ?,?);
                """, (usuario_id, sitio_nombre, usuario_sitio, password_sitio) 
            )
            
            cursor.connection.commit()
            cursor.close()

            print("Credenciales guardads con exito")
        except AttributeError:
            print("Error en el registro de credenciales")

    def ver_credenciales(self, user_id, pin):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                """
                SELECT *
                FROM sites s
                INNER JOIN users u
                ON s.user_id = ?
                WHERE u.user_pin = ?
                """, (user_id,pin) 
            )
            respuesta = cursor.fetchall()
            print(respuesta)
            return respuesta
        except sqlite3.Error as e:  
            print(f"Error en la visualización de credenciales: {e}")
            return None