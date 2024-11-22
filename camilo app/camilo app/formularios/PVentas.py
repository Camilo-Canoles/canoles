import tkinter as tk
import json
from tkinter import messagebox, ttk
import webbrowser
import util.generic as utl
from PIL import Image, ImageTk
class PVentas(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        self.tipo_action ="Guardar"
        self.tipo_user = ""
        super().__init__()
        self.title("Panel Ventas")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Administracion de Cliente")  
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        self.config(menu=menubar)