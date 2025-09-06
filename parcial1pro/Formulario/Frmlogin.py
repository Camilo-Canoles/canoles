import tkinter as tk
from tkinter import messagebox
from clases.Usuario import Usuarios
from Formulario.Frmuser import FrmRegUser
from Formulario.Frmdashboard import FrmDashboard

class FrmLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        tk.Label(root, text="Nickname").grid(row=0, column=0)
        tk.Label(root, text="Clave").grid(row=1, column=0)

        self.entry_nickname = tk.Entry(root)
        self.entry_clave = tk.Entry(root, show="*")

        self.entry_nickname.grid(row=0, column=1)
        self.entry_clave.grid(row=1, column=1)

        tk.Button(root, text="Ingresar", command=self.validar).grid(row=2, column=0)
        tk.Button(root, text="Registrar", command=self.abrir_registro).grid(row=2, column=1)

    def validar(self):
        nickname = self.entry_nickname.get()
        clave = self.entry_clave.get()

        usuario = Usuarios.validarUsuario(nickname, clave)
        if usuario:
            messagebox.showinfo("Bienvenido", f"Hola {usuario.nombre}!")
            self.root.destroy()
            self.abrir_dashboard(usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def abrir_registro(self):
        ventana_registro = tk.Toplevel(self.root)
        FrmRegUser(ventana_registro)

    def abrir_dashboard(self, usuario):
        ventana_dashboard = tk.Tk()
        FrmDashboard(ventana_dashboard, usuario)
        ventana_dashboard.mainloop()
