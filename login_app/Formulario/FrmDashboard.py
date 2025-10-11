import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser
from Formulario.FrmUserRegistro import FrmUserRegistro


class FrmDashboard:

    def __init__(self, datos_usuario):
        self.datos_usuario = datos_usuario

        self.root = tk.Tk()
        self.root.title("Panel Administrativo")
        self.root.geometry("1200x600")
        self.root.resizable(True, True)
        self.root.configure(bg="#f2f2f2")


        ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "image"))


        tk.Label(self.root, text="PANEL ADMINISTRATIVO",
                font=("Times New Roman", 22, "bold"), bg="#f2f2f2").place(x=20, y=20)
        tk.Label(self.root, text="BIENVENIDO AL SISTEMA",
                font=("Times New Roman", 20, "bold"), bg="#f2f2f2").place(x=850, y=20)


        self.img_userinfo = self._cargar_imagen(os.path.join(ruta_base, "userinfo.png"), (120, 120))
        if self.img_userinfo:
            tk.Label(self.root, image=self.img_userinfo, bg="#f2f2f2").place(x=150, y=100)
        else:
            tk.Label(self.root, text="[No image]", bg="#f2f2f2").place(x=150, y=140)

        tk.Label(self.root, text=datos_usuario.get("nombre", "Sin nombre"),
                font=("Times New Roman", 14, "bold"), bg="#f2f2f2").place(x=130, y=240)
        tk.Label(self.root, text=datos_usuario.get("email", ""),
                font=("Arial", 12), bg="#f2f2f2").place(x=80, y=270)
        tk.Label(self.root, text=datos_usuario.get("rol", ""),
                font=("Arial", 12, "bold"), bg="#f2f2f2").place(x=160, y=300)


        self.agregar_icono(ruta_base, "face.png", 70,
                        lambda: webbrowser.open_new_tab("https://www.facebook.com/"))
        self.agregar_icono(ruta_base, "linkedin.png", 120,
                        lambda: webbrowser.open_new_tab("https://www.linkedin.com/"))
        self.agregar_icono(ruta_base, "website.png", 170,
                        lambda: webbrowser.open_new_tab("https://www.unitecnar.edu.co/"))
        self.agregar_icono(ruta_base, "logout.png", 220, self.cerrar_sesion)


        self.frame_contenido = tk.Frame(self.root, bg="#f2f2f2")
        self.frame_contenido.place(x=400, y=100, width=770, height=450)

        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        menu_clientes = tk.Menu(barra_menu, tearoff=0)
        menu_clientes.add_command(label="Administración de clientes", command=self.mostrar_formulario_clientes)
        barra_menu.add_cascade(label="Clientes", menu=menu_clientes)

        barra_menu.add_command(label="Categorías")
        barra_menu.add_command(label="Productos")
        barra_menu.add_command(label="Ventas")

        tk.Label(self.root, text="Desarrollado por: Camilo Canoles",
        font=("Arial", 10, "italic"), bg="#f2f2f2").place(x=20, y=570)

        self.root.mainloop()


    def _cargar_imagen(self, ruta, size):

        try:
            imagen = Image.open(ruta).resize(size)
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"No se pudo cargar la imagen '{ruta}': {e}")
            return None

    def agregar_icono(self, ruta_base, nombre, pos_x, comando):

        ruta = os.path.join(ruta_base, nombre)
        icon = self._cargar_imagen(ruta, (30, 30))
        if icon:
            btn = tk.Button(self.root, image=icon, bg="white", relief="flat",
                            cursor="hand2", command=comando)
            btn.image = icon 
            btn.place(x=pos_x, y=350)
        else:
            tk.Button(self.root, text=nombre.split('.')[0], bg="white", relief="flat",
                    cursor="hand2", command=comando).place(x=pos_x, y=350)

    def mostrar_formulario_usuarios(self):

        for widget in self.frame_contenido.winfo_children():
            widget.destroy()
        FrmUserRegistro(self.frame_contenido, self.datos_usuario.get("rol"))

    def cerrar_sesion(self):

        from Formulario.FrmLogin import Login
        self.root.destroy()
        Login()

    def mostrar_formulario_clientes(self):

        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        from Formulario.FrmClientes import FrmClientes
        FrmClientes(self.frame_contenido)

