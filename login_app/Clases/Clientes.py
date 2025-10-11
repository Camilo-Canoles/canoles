from Clases.conector import Conector

class Clientes:
    def __init__(self):
        self.con = Conector()

    def guardarCliente(self, nombre, apellido, email, telefono, direccion, ciudad):
        sql = """INSERT INTO clientes (nombre, apellido, email, telefono, direccion, ciudad)
                VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (nombre, apellido, email, telefono, direccion, ciudad)
        return self.con.ejecutar(sql, valores)

    def obtenerClientes(self):
        sql = "SELECT id, nombre, apellido, email, telefono, direccion, ciudad FROM clientes"
        return self.con.consultar(sql)

    def actualizarCliente(self, id_cliente, nombre, apellido, email, telefono, direccion, ciudad):
        sql = """UPDATE clientes
                SET nombre=%s, apellido=%s, email=%s, telefono=%s, direccion=%s, ciudad=%s
                WHERE id=%s"""
        valores = (nombre, apellido, email, telefono, direccion, ciudad, id_cliente)
        return self.con.ejecutar(sql, valores)

    def eliminarCliente(self, id_cliente):
        sql = "DELETE FROM clientes WHERE id=%s"
        valores = (id_cliente,)
        return self.con.ejecutar(sql, valores)

