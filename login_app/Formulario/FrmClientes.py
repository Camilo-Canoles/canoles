import tkinter as tk
from tkinter import ttk, messagebox
from Clases.Clientes import Clientes

class FrmClientes:
    def __init__(self, root):
        self.root = tk.Frame(root, bg="#f2f2f2")
        self.root.pack(fill="both", expand=True)
        self.db = Clientes()
        self.id_cliente = None

        tk.Label(self.root, text="ADMINISTRACIÓN DE CLIENTES", font=("Times New Roman", 18, "bold"), bg="#f2f2f2").pack(pady=15)

        frame = tk.Frame(self.root, bg="#f2f2f2")
        frame.pack(pady=10)

        campos = ["Nombre:", "Apellido:", "Email:", "Teléfono:", "Dirección:", "Ciudad:"]
        self.entries = []
        for i, texto in enumerate(campos):
            tk.Label(frame, text=texto, bg="#f2f2f2").grid(row=i, column=0, sticky="e", padx=10, pady=5)
            entrada = tk.Entry(frame, width=30)
            entrada.grid(row=i, column=1, pady=5)
            self.entries.append(entrada)

        botones = tk.Frame(self.root, bg="#f2f2f2")
        botones.pack(pady=10)

        tk.Button(botones, text="Guardar", bg="lightgreen", command=self.guardarCliente).grid(row=0, column=0, padx=5)
        tk.Button(botones, text="Actualizar", bg="lightblue", command=self.actualizarCliente).grid(row=0, column=1, padx=5)
        tk.Button(botones, text="Eliminar", bg="tomato", command=self.eliminarCliente).grid(row=0, column=2, padx=5)
        tk.Button(botones, text="Cargar", bg="white", command=self.cargarSeleccion).grid(row=0, column=3, padx=5)

        self.tabla = ttk.Treeview(self.root, columns=("ID","Nombre","Apellido","Email","Teléfono","Dirección","Ciudad"), show="headings", height=10)
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=120)
        self.tabla.pack(fill="both", expand=True, pady=10)

        self.cargarClientes()

    def guardarCliente(self):
        datos = [e.get().strip() for e in self.entries]
        if all(datos):
            if self.db.guardarCliente(*datos):
                messagebox.showinfo("Éxito", "Cliente guardado correctamente.")
                self.cargarClientes()
                self.limpiar()
            else:
                messagebox.showerror("Error", "No se pudo guardar el cliente.")
        else:
            messagebox.showwarning("Campos vacíos", "Debes llenar todos los campos.")

    def cargarClientes(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for c in self.db.obtenerClientes():
            self.tabla.insert("", "end", values=c)

    def cargarSeleccion(self):
        seleccion = self.tabla.focus()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Debes seleccionar un cliente.")
            return
        valores = self.tabla.item(seleccion, "values")
        self.id_cliente = valores[0]
        for i, e in enumerate(self.entries):
            e.delete(0, tk.END)
            e.insert(0, valores[i+1])

    def actualizarCliente(self):
        if not self.id_cliente:
            messagebox.showwarning("Atención", "Primero carga un cliente para actualizar.")
            return
        datos = [e.get().strip() for e in self.entries]
        if self.db.actualizarCliente(self.id_cliente, *datos):
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
            self.cargarClientes()
            self.limpiar()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el cliente.")

    def eliminarCliente(self):
        if not self.id_cliente:
            messagebox.showwarning("Atención", "Primero carga un cliente para eliminar.")
            return
        if messagebox.askyesno("Confirmar", "¿Deseas eliminar este cliente?"):
            if self.db.eliminarCliente(self.id_cliente):
                messagebox.showinfo("Eliminado", "Cliente eliminado correctamente.")
                self.cargarClientes()
                self.limpiar()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el cliente.")

    def limpiar(self):
        for e in self.entries:
            e.delete(0, tk.END)
        self.id_cliente = None
