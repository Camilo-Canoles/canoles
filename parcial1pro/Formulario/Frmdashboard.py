import tkinter as tk

class FrmDashboard:
    def __init__(self, root, usuario):
        self.root = root
        self.root.title("Dashboard")

        tk.Label(root, text=f"Bienvenido {usuario.nombre} {usuario.apellidos}").pack(pady=5)
        tk.Label(root, text=f"Email: {usuario.email}").pack(pady=5)
        tk.Label(root, text=f"Nickname: {usuario.nickname}").pack(pady=5)


        tk.Label(root, text="👤 Imagen de usuario por defecto").pack(pady=10)
