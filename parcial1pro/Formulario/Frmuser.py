import tkinter as tk
from tkinter import messagebox
from clases.Usuario import Usuarios

class FrmRegUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Usuario")

        tk.Label(root, text="Nombre").grid(row=0, column=0)
        tk.Label(root, text="Apellidos").grid(row=1, column=0)
        tk.Label(root, text="Email").grid(row=2, column=0)
        tk.Label(root, text="Nickname").grid(row=3, column=0)
        tk.Label(root, text="Clave").grid(row=4, column=0)

        self.entry_nombre = tk.Entry(root)
        self.entry_apellidos = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_nickname = tk.Entry(root)
        self.entry_clave = tk.Entry(root, show="*")

        self.entry_nombre.grid(row=0, column=1)
        self.entry_apellidos.grid(row=1, column=1)
        self.entry_email.grid(row=2, column=1)
        self.entry_nickname.grid(row=3, column=1)
        self.entry_clave.grid(row=4, column=1)

        tk.Button(root, text="Guardar", command=self.guardar).grid(row=5, columnspan=2)

    def guardar(self):
        nombre = self.entry_nombre.get()
        apellidos = self.entry_apellidos.get()
        email = self.entry_email.get()
        nickname = self.entry_nickname.get()
        clave = self.entry_clave.get()

        if not all([nombre, apellidos, email, nickname, clave]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        Usuarios.guardarUsuario(nombre, apellidos, email, nickname, clave)
        messagebox.showinfo("Éxito", "Usuario registrado con éxito")
        self.root.destroy()

