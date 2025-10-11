from Clases.conector import Conector

class Usuarios:
    def __init__(self):
        self.con = Conector()

    def registrar_usuario(self, nombre, apellido, email, username, clave, rol):
        sql = "INSERT INTO usuarios (nombre, apellido, email, username, clave, rol) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, email, username, clave, rol)
        return self.con.ejecutar(sql, valores)

    def validar_usuario(self, usuario, clave):
        sql = "SELECT id, nombre, apellido, email, username, clave, rol FROM usuarios WHERE username=%s AND clave=%s"
        valores = (usuario, clave)
        resultado = self.con.consultar(sql, valores)
        return resultado[0] if resultado else None

    def eliminar_usuario(self, username):
        sql = "DELETE FROM usuarios WHERE username=%s"
        valores = (username,)
        return self.con.ejecutar(sql, valores)

    def obtener_usuarios(self):
        sql = "SELECT nombre, apellido, email, username, rol FROM usuarios"
        return self.con.consultar(sql)

    def editar_usuario(self, nombre, apellido, email, username, rol):
        sql = """UPDATE usuarios
                SET nombre=%s, apellido=%s, email=%s, rol=%s
                WHERE username=%s"""
        valores = (nombre, apellido, email, rol, username)
        return self.con.ejecutar(sql, valores)
