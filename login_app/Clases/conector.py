import mysql.connector

class Conector:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",         
                password="",          
                database="login_app1"   
            )
            self.cursor = self.conn.cursor()
            print(" Conexión a la base de datos establecida correctamente.")
        except mysql.connector.Error as e:
            print(f" Error al conectar con la base de datos: {e}")

    def ejecutar(self, sql, valores=None):

        try:
            self.cursor.execute(sql, valores)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f" Error al ejecutar SQL: {e}")
            return False

    def consultar(self, sql, valores=None):
    
        try:
            self.cursor.execute(sql, valores)
            resultados = self.cursor.fetchall()
            return resultados
        except mysql.connector.Error as e:
            print(f" Error al consultar datos: {e}")
            return []

    def __del__(self):

        try:
            if hasattr(self, "conn") and self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print("Conexión cerrada correctamente.")
        except:
            pass
