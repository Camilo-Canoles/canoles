import tkinter as tk
from tkinter import messagebox

class Usuarios:
    def __init__(self, cedula, nickname, nombre, apellido, clave):
        self.cedula = cedula
        self.nickname = nickname
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave

    @staticmethod
    def validar(nickname, clave):
        
        usuarios = {
            
            "usuario": Usuarios("1043295736", "usuario", "camilo", "canoles", "clave"),
           
        
        }

        usuario = usuarios.get(nickname)
        if usuario and usuario.clave == clave:
            return True
        return False

class LoginForm:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Login")

        self.nickname_label = tk.Label(self.ventana, text="Nickname:")
        self.nickname_label.pack()
        self.nickname_entry = tk.Entry(self.ventana)
        self.nickname_entry.pack()

        self.clave_label = tk.Label(self.ventana, text="Clave:")
        self.clave_label.pack()
        self.clave_entry = tk.Entry(self.ventana, show="*")
        self.clave_entry.pack()

        self.ingresar_button = tk.Button(self.ventana, text="Ingresar", command=self.validar_login)
        self.ingresar_button.pack()

    def validar_login(self):
        nickname = self.nickname_entry.get()
        clave = self.clave_entry.get()
        if Usuarios.validar(nickname, clave):
            self.ventana.destroy()
            DashboardForm().mostrar()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def mostrar(self):
        self.ventana.mainloop()

class DashboardForm:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Dashboard")

        self.bienvenido_label = tk.Label(self.ventana, text="Bienvenido al sistema")
        self.bienvenido_label.pack()

    def mostrar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    LoginForm().mostrar()
