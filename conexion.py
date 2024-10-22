import sqlite3

class Conexion:
    def __init__(self, nombre = 'conexion_BD'):
        self.nombre = nombre,
        self.conexion = None

    def conectar(self):
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
            cursor.execute(
                """
                CREATE DATABASE IF NOT EXIST gestor_bd;

                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    usar_name VARCHAR(50) NOT NULL,
                    user_username VARCHAR(50) UNIQUE NOT NULL,
                    user_password VARCHAR(50) NOT NULL,
                    user_email VARCHAR(50) NOT NULL
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
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR (50) NOT NULL,
                    FOREIGN KEY (site_id) REFERENCES sites (site_id)
                );

                """
            )
        except AttributeError:
            print('Falla en la conexion de la base de datos antes de crear las tablas')
    
    def registar_usuario(self, nombre, nombre_usuario, password, email):
        try:
            cursor = self.conexion.cursor()

            cursor.execute("""
                INSERT INTO users  ('user_name', 'user_useraname', 'user_password','user_email') VALUES (?, ?, ?, ?)
            """, nombre, nombre_usuario, password, email)
            cursor.connection.commit();
        
        except AttributeError:
            print('Ingreso INCORRECTO DE DATOS')
    
    #COMPLETAR LAS FUNCIONES DE RESTANTES DE DATOS.
