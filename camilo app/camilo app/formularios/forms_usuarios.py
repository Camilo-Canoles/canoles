import json
import tkinter as tk
from tkinter import ttk, messagebox

class FormUsuarios(tk.Tk):
    def __init__(self, parent):
        self.tipo_action = "Guardar"
        self.tipo_user = ""
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self.frame, text="Registro de usuarios", font=('Times', 16)).place(x=70, y=30)

        labelcedula = tk.Label(self.frame, text="Cedula", font=('Times', 14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame, text="Nombre", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame, text="Username", font=('Times', 14))
        labelusuario.place(x=70, y=160)
        self.cusuario = tk.Entry(self.frame, width=40)
        self.cusuario.place(x=220, y=160)

        labelcontrasena = tk.Label(self.frame, text="Contraseña", font=('Times', 14))
        labelcontrasena.place(x=500, y=100)
        self.ccontrasena = tk.Entry(self.frame, width=40, show="*")
        self.ccontrasena.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame, text="Correo", font=('Times', 14))
        labelcorreo.place(x=500, y=130)
        self.ccorreo = tk.Entry(self.frame, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame, text="Rol", font=('Times', 14))
        labeltipo.place(x=500, y=160)
        self.ctipo = ttk.Combobox(self.frame, width=40)
        self.ctipo.place(x=600, y=160)
        self.ctipo["values"] = ("Administrador", "Vendedor")

        btn_guardar = tk.Button(self.frame, text="Guardar", font=('Times', 14), command=self.guardar_usuario)
        btn_guardar.place(x=70, y=190)

        self.listar_usuarios()

    def listar_usuarios(self):
        tk.Label(self.frame, text="Listado de usuarios", font=('Times', 16)).place(x=70, y=230)

        self.tablausuarios = ttk.Treeview(self.frame, columns=("id", "nombre", "username", "correo", "rol"), show='headings')
        self.tablausuarios.heading("id", text="id")
        self.tablausuarios.heading("nombre", text="Nombre")
        self.tablausuarios.heading("username", text="username")
        self.tablausuarios.heading("correo", text="Correo")
        self.tablausuarios.heading("rol", text="Rol")

        self.tablausuarios.place(x=70, y=280)

        self.cargar_usuarios()

        btneliminar = tk.Button(self.frame, text="Eliminar", font=('Times', 14), command=self.eliminar_usuario).place(x=70, y=580)
        btnactualizar = tk.Button(self.frame, text="Actualizar", font=('Times', 14), command=self.actualizar_usuario).place(x=170, y=580)

    def cargar_usuarios(self):
        for i in self.tablausuarios.get_children():
            self.tablausuarios.delete(i)
        with open(r"camilo app/db_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                self.tablausuarios.insert("", "end", values=(f'{user["id"]}', f'{user["name"]}', f'{user["username"]}', f'{user["email"]}', f'{user["role"]}'))

    def guardar_usuario(self):
        new_user = {
            "id": self.ccedula.get(),
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }
        with open(r"camilo app/db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["users"].append(new_user)
            file.seek(0)
            json.dump(data, file, indent=4)
        self.cargar_usuarios()
        messagebox.showinfo("Información", "Usuario guardado exitosamente")

    def eliminar_usuario(self):
        selected_item = self.tablausuarios.selection()[0]
        user_id = self.tablausuarios.item(selected_item, "values")[0]
        with open(r"camilo app/db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["users"] = [user for user in data["users"] if user["id"] != user_id]
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
        self.cargar_usuarios()
        messagebox.showinfo("Información", "Usuario eliminado exitosamente")

    def actualizar_usuario(self):
        selected_item = self.tablausuarios.selection()[0]
        user_id = self.tablausuarios.item(selected_item, "values")[0]
        updated_user = {
            "id": self.ccedula.get(),
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }
        with open(r"camilo app/db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            for i, user in enumerate(data["users"]):
                if user["id"] == user_id:
                    data["users"][i] = updated_user
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
        self.cargar_usuarios()
        messagebox.showinfo("Información", "Usuario actualizado exitosamente")