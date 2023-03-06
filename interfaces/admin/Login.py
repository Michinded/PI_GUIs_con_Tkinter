import hashlib
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
# import mysql.connector
import interfaces.ConectorBD


# Establecer la conexión con la base de datos

# Obtener el cursor de la conexión
# ConectorBD.cursor
def comprobarData(username, password):
    # Comprobar si el usuario existe
    # Comprobar si la contraseña es correcta
    # Mostrar mensaje de bienvenida y datos del usuario
    # Cerrar ventana actual y volver a la ventana principal
    success = False
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    query = "SELECT adminId, adminName, email, registred_at, active_rol FROM admins WHERE email = %s AND password = %s"
    interfaces.ConectorBD.cursor.execute(query, (username, hashed_password))
    result = interfaces.ConectorBD.cursor.fetchone()
    if result:
        rol = "Activo" if result[4] == 1 else "Inactivo"
        msgbox.showinfo("Bienvenido", f"Bienvenido Administrador!\nid: {result[0]}\nAdmin: {result[1]}\nSu email "
                                      f"registrado es: {result[2]}\nUsted Creo su cuenta en: {result[3]}\nSu rol de "
                                      f"Administrador esta: {rol}")
    else:
        msgbox.showerror("Error", "Usuario o contraseña incorrectos")



# funciion para validar que no haya campos vacios
def validarCampos(username, password):
    if username == "" or password == "":
        return True
    else:
        return False


class LoginWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        # colores
        cbg = "#306AD1"
        #clabel = "#35D38B"
        centry = "#5A87D6"

        # Widgets
        seccion1 = Frame(self, bg=cbg)
        seccion1.pack(expand=True, fill="both")

        username_lbl = tk.Label(seccion1, text="Email:", bg=cbg, fg="white", font=("Arial", 12))
        username_lbl.pack(pady=10)

        self.username_entry = tk.Entry(seccion1, bg=centry, fg="white", font=("Arial", 12))
        self.username_entry.pack()

        password_lbl = tk.Label(seccion1, text="Password:", bg=cbg, fg="white", font=("Arial", 12))
        password_lbl.pack(pady=10)

        self.password_entry = tk.Entry(seccion1, show="*", bg=centry, fg="white", font=("Arial", 12))
        self.password_entry.pack()

        login_btn = tk.Button(seccion1, text="Login", command=self.login, bg="blue", fg="white", font=("Arial", 12))
        login_btn.pack(pady=10)

    def login(self):
        # Implementar la funcionalidad de login
        # Consultar la tabla "users" y verificar si el usuario existe y la contraseña es correcta
        username = self.username_entry.get()
        password = self.password_entry.get()
        if validarCampos(username, password):
            msgbox.showerror("Error", "Usuario o contraseña vacios, por favor llenar los campos")
            return
        else:
            comprobarData(username, password)
        self.destroy()
