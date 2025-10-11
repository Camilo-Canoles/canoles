import tkinter as tk
from tkinter import ttk, messagebox
from Clases.Clientes import Clientes


class FrmUserRegistro:
    def __init__(self, root, rol_actual):
        self.root = tk.Frame(root, bg="#f2f2f2")
        self.root.pack(fill="both", expand=True)
        self.rol_actual = rol_actual.strip().lower()
        self.usuario_seleccionado = None

        tk.Label(self.root, text="GESTIÓN DE USUARIOS", font=("Times New Roman", 18, "bold"), bg="#f2f2f2").pack(pady=15)

        frame = tk.Frame(self.root, bg="#f2f2f2")
        frame.pack(pady=10)

        campos = ["Nombre:", "Apellido:", "Email:", "Usuario:", "Clave:", "Rol:"]
        for i, texto in enumerate(campos):
            tk.Label(frame, text=texto, bg="#f2f2f2").grid(row=i, column=0, sticky="e", padx=10, pady=5)

        self.txt_nombre = tk.Entry(frame, width=30)
        self.txt_apellido = tk.Entry(frame, width=30)
        self.txt_email = tk.Entry(frame, width=30)
        self.txt_usuario = tk.Entry(frame, width=30)
        self.txt_clave = tk.Entry(frame, width=30, show="*")

        self.rol_var = tk.StringVar()
        self.combo_rol = ttk.Combobox(frame, textvariable=self.rol_var, values=["admin", "Vendedor"], state="readonly", width=27)
        self.combo_rol.set("Seleccionar Rol")

        self.txt_nombre.grid(row=0, column=1, pady=5)
        self.txt_apellido.grid(row=1, column=1, pady=5)
        self.txt_email.grid(row=2, column=1, pady=5)
        self.txt_usuario.grid(row=3, column=1, pady=5)
        self.txt_clave.grid(row=4, column=1, pady=5)
        self.combo_rol.grid(row=5, column=1, pady=5)

        if self.rol_actual == "admin":
            tk.Button(self.root, text="Registrar Usuario", bg="white", font=("Arial", 12, "bold"),
                    cursor="hand2", command=self.registrar_usuario).pack(pady=15)

        self.frame_tabla = tk.Frame(self.root, bg="#f2f2f2")
        self.frame_tabla.pack(pady=10, fill="both", expand=True)

        self.tabla = ttk.Treeview(self.frame_tabla, columns=("Nombre", "Apellido", "Email", "Usuario", "Rol"), show="headings", height=8)
        for col in ("Nombre", "Apellido", "Email", "Usuario", "Rol"):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150)
        self.tabla.pack(fill="both", expand=True)

        if self.rol_actual == "admin":
            btn_frame = tk.Frame(self.root, bg="#f2f2f2")
            btn_frame.pack(pady=10)

            self.btn_editar = tk.Button(btn_frame, text="Editar Usuario", command=self.editar_usuario, bg="lightblue", width=18, state="disabled")
            self.btn_editar.grid(row=0, column=0, padx=10)

            self.tabla.bind("<<TreeviewSelect>>", self.activar_botones)

        self.cargar_usuarios()

    def activar_botones(self, event):
        seleccion = self.tabla.focus()
        if seleccion:
            self.btn_editar.config(state="normal")
        else:
            self.btn_editar.config(state="disabled")

    def registrar_usuario(self):
        nombre = self.txt_nombre.get().strip()
        apellido = self.txt_apellido.get().strip()
        email = self.txt_email.get().strip()
        username = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()
        rol = self.rol_var.get().strip()

        if not (nombre and apellido and email and username and clave and rol != "Seleccionar Rol"):
            messagebox.showwarning("Campos incompletos", "Debes rellenar todos los campos antes de continuar.")
            return

        db = Clientes()
        if db.registrar_usuario(nombre, apellido, email, username, clave, rol):
            messagebox.showinfo("Registro Exitoso", f"El usuario '{username}' se agregó correctamente.")
            self.cargar_usuarios()
            self.limpiar_campos()
        else:
            messagebox.showerror("Fallo en el registro", "Hubo un problema al intentar agregar el usuario.")

    def cargar_usuarios(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        db = Clientes()
        for usuario in db.obtener_usuarios():
            self.tabla.insert("", "end", values=usuario)

    def editar_usuario(self):
        seleccion = self.tabla.focus()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Debes seleccionar un usuario para editar.")
            return

        datos = self.tabla.item(seleccion, "values")
        nombre, apellido, email, username, rol = datos

        self.txt_nombre.delete(0, tk.END)
        self.txt_apellido.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_usuario.delete(0, tk.END)
        self.txt_clave.delete(0, tk.END)
        self.combo_rol.set(rol)

        self.txt_nombre.insert(0, nombre)
        self.txt_apellido.insert(0, apellido)
        self.txt_email.insert(0, email)
        self.txt_usuario.insert(0, username)

        if messagebox.askyesno("Confirmación", f"¿Deseas guardar los cambios en '{username}'?"):
            db = Clientes()
            if db.editar_usuario(self.txt_nombre.get(), self.txt_apellido.get(),
                                self.txt_email.get(), self.txt_usuario.get(), self.combo_rol.get()):
                messagebox.showinfo("Actualización exitosa", f"Los datos del usuario '{username}' fueron modificados correctamente.")
            else:
                messagebox.showerror("Error al actualizar", "No se pudo guardar la información del usuario.")
            self.cargar_usuarios()
            self.limpiar_campos()

    def limpiar_campos(self):
        self.txt_nombre.delete(0, tk.END)
        self.txt_apellido.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_usuario.delete(0, tk.END)
        self.txt_clave.delete(0, tk.END)
        self.combo_rol.set("Seleccionar Rol")
