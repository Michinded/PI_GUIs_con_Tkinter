import tkinter as tk


class HUB:
    def __init__(self, userId, username, contenido, categoria, posted_at):
        self.userId = userId
        self.username = username
        self.contenido = contenido
        self.categoria = categoria
        self.posted_at = posted_at


class HUBInterfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz para HUB")

        # Crear etiquetas y campos de entrada
        tk.Label(self.master, text="User ID:").grid(row=0, column=0)
        self.userId_entry = tk.Entry(self.master)
        self.userId_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Username:").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Contenido:").grid(row=2, column=0)
        self.contenido_entry = tk.Entry(self.master)
        self.contenido_entry.grid(row=2, column=1)

        tk.Label(self.master, text="Categoria:").grid(row=3, column=0)
        self.categoria_entry = tk.Entry(self.master)
        self.categoria_entry.grid(row=3, column=1)

        tk.Label(self.master, text="Posted at:").grid(row=4, column=0)
        self.posted_at_entry = tk.Entry(self.master)
        self.posted_at_entry.grid(row=4, column=1)

        # Crear botón para guardar los datos
        tk.Button(self.master, text="Guardar", command=self.guardar_datos).grid(row=5, column=1)

    def guardar_datos(self):
        # Obtener los valores de los campos de entrada
        userId = self.userId_entry.get()
        username = self.username_entry.get()
        contenido = self.contenido_entry.get()
        categoria = self.categoria_entry.get()
        posted_at = self.posted_at_entry.get()

        # Crear un objeto HUB con los valores obtenidos
        hub = HUB(userId, username, contenido, categoria, posted_at)

        # Hacer algo con el objeto HUB creado, como imprimirlo en la consola
        print(hub.__dict__)


# Crear la ventana principal y la interfaz de HUB
root = tk.Tk()
HUBInterfaz(root)

root.mainloop()
