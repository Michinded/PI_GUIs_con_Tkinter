import hashlib
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import datetime
import interfaces.ConectorBD


# import mysql.connector


# funcion para registar usuario
def registrar(name, email, password):
    fecha = datetime.datetime.now()
    rol = 1
    if Duplicado(email):
        msgbox.showerror("Error", "El correo ya existe")
        return
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        sql = "INSERT INTO admins (adminName, email, password, registred_at, active_rol ) VALUES (%s, %s, %s, %s, %s)"
        val = (name, email, hashed_password, fecha, rol)
        interfaces.ConectorBD.cursor.execute(sql, val)
        interfaces.ConectorBD.conn.commit()
        msgbox.showinfo("Informacion", "Registro exitoso")


# funcion para comprobar si el usuario ya existe
def Duplicado(email):
    sql = "SELECT * FROM admins WHERE email = %s"
    val = (email,)
    interfaces.ConectorBD.cursor.execute(sql, val)
    result = interfaces.ConectorBD.cursor.fetchall()
    if result:
        return True
    else:
        return False


# funcion para validar que no haya campos vacios
def validarCampos(name, email, password):
    if name == "" or email == "" or password == "":
        return True
    else:
        return False


# validar que el email sea valido
def validarEmail(email):
    if "@" in email:
        return False
    else:
        return True


class SignupWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Signup ADMIN")
        self.geometry("300x400")

        cbg = "#35D38B"
        clabel = "#35D38B"
        centry = "#65D1A0"

        # Widgets
        seccion1 = Frame(self, bg=cbg)
        seccion1.pack(expand=True, fill="both")

        username_lbl = tk.Label(seccion1, text="Nombre:", bg=cbg, fg="white", font=("Arial", 12))
        username_lbl.pack(pady=10)

        self.username_entry = tk.Entry(seccion1, bg=centry, fg="white", font=("Arial", 12))
        self.username_entry.pack()

        email_lbl = tk.Label(seccion1, text="Email:", bg=cbg, fg="white", font=("Arial", 12))
        email_lbl.pack(pady=10)

        self.email_entry = tk.Entry(seccion1, bg=centry, fg="white", font=("Arial", 12))
        self.email_entry.pack()

        password_lbl = tk.Label(seccion1, text="Password (Minimo 8 carácteres):", bg=cbg, fg="white",
                                font=("Arial", 12))
        password_lbl.pack(pady=10)

        self.password_entry = tk.Entry(seccion1, show="*", bg=centry, fg="white", font=("Arial", 12))
        self.password_entry.pack()

        signup_btn = tk.Button(seccion1, text="Signup", command=self.signup, bg="red", fg="white", font=("Arial", 12))
        signup_btn.pack(pady=10)

    def signup(self):
        # Obtener los datos del formulario
        nombre = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Convertir el email a minusculas
        email = email.lower()
        # Validar que no haya campos vacios
        if validarCampos(nombre, email, password):
            msgbox.showerror("Error", "Todos los campos son requeridos")
            return
        else:
            if len(password) < 8:
                msgbox.showerror("Error", "La contraseña debe tener al menos 8 caracteres")
                return
            if validarEmail(email):
                msgbox.showerror("Error", "Formato de Email invalido")
                return
            # Insertar el nuevo usuario en la tabla "users"
            registrar(nombre, email, password)
            # Cerrar ventana actual y volver a la ventana principal
            self.destroy()
