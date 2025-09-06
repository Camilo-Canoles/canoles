class Usuarios:
    lista_usuarios = []

    def __init__(self, nombre, apellidos, email, nickname, clave):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.nickname = nickname
        self.clave = clave

    @classmethod
    def guardarUsuario(cls, nombre, apellidos, email, nickname, clave):
        usuario = Usuarios(nombre, apellidos, email, nickname, clave)
        cls.lista_usuarios.append(usuario)
        return usuario

    @classmethod
    def validarUsuario(cls, nickname, clave):
        for usuario in cls.lista_usuarios:
            if usuario.nickname == nickname and usuario.clave == clave:
                return usuario
        return None
