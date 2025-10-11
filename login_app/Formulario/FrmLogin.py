import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from Clases.Usuarios import Usuarios
from Formulario.FrmDashboard import FrmDashboard

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("INGRESO AL SISTEMA")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f2f2f2")

        ruta_base = os.path.join(os.path.dirname(__file__), "../image")

        lbl_titulo = tk.Label(self.root, text="INGRESO AL SISTEMA", font=("Times New Roman", 22, "bold"), bg="#f2f2f2")
        lbl_titulo.place(x=450, y=50)

        img_logo = Image.open(os.path.join(ruta_base, "logo.png")).resize((220, 160))
        self.logo = ImageTk.PhotoImage(img_logo)
        lbl_logo = tk.Label(self.root, image=self.logo, bg="#f2f2f2")
        lbl_logo.place(x=60, y=160)

        img_user = Image.open(os.path.join(ruta_base, "login.png")).resize((70, 70))
        self.img_user = ImageTk.PhotoImage(img_user)
        lbl_user = tk.Label(self.root, image=self.img_user, bg="#f2f2f2")
        lbl_user.place(x=590, y=100)

        tk.Label(self.root, text="Usuario:", font=("Times New Roman", 14), bg="#f2f2f2").place(x=450, y=200)
        self.txt_usuario = tk.Entry(self.root, font=("Arial", 12), width=25)
        self.txt_usuario.place(x=450, y=230)

        tk.Label(self.root, text="Clave:", font=("Times New Roman", 14), bg="#f2f2f2").place(x=450, y=270)
        self.txt_clave = tk.Entry(self.root, show="*", font=("Arial", 12), width=25)
        self.txt_clave.place(x=450, y=300)

        tk.Button(
            self.root, text="Iniciar sesión", font=("Arial", 12, "bold"),
            bg="white", relief="raised", cursor="hand2", command=self.validar_credenciales
        ).place(x=450, y=350, width=200, height=40)

        self.root.mainloop()

    def validar_credenciales(self):
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        if not usuario or not clave:
            messagebox.showwarning("Campos incompletos", "Por favor ingresa tu usuario y contraseña para continuar.")
            return

        db = Usuarios()
        datos = db.validar_usuario(usuario, clave)

        if datos:
            datos_usuario = {
                "nombre": f"{datos[1]} {datos[2]}",
                "email": datos[3],
                "rol": datos[6]
            }

            messagebox.showinfo("¡Bienvenido!", f"Hola {datos_usuario['nombre']}, has iniciado sesión correctamente.")
            self.root.destroy()
            FrmDashboard(datos_usuario)
        else:
            messagebox.showerror("Acceso denegado", "Las credenciales ingresadas no coinciden con ningún usuario registrado. Revisa e inténtalo nuevamente.")
