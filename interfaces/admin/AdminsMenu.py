import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
from .Login import LoginWindow
from .SigIn import SignupWindow


class MenuAdmin(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.signup = None
        self.title("MODO ADMINISTRADOR")
        self.geometry("200x200")
        self.resizable(0, 0)
        seccion1 = Frame(self, bg="blue")
        seccion1.pack(expand=True, fill="both")

        # Widgets
        # Inicio Label
        welcome_label = tk.Label(seccion1, text="Bienvenido elija una opcion:", bg="blue", fg="white",
                                 font=("Arial", 12))
        welcome_label.pack(pady=10)

        login_btn = tk.Button(seccion1, text="Login", command=self.show_login_form, bg="blue", fg="white",
                              font=("Arial", 12))
        login_btn.pack(pady=10)

        signup_btn = tk.Button(seccion1, text="Signup", command=self.show_singup_form, bg="blue", fg="white", font=("Arial", 12))
        signup_btn.pack(pady=10)

        close_btn = tk.Button(seccion1, text="Cerrar", command=self.destroy, bg="red", fg="white", font=("Arial", 12))
        close_btn.pack(pady=10)

    def show_login_form(self):
        # Crear instancia de la clase LoginWindow y hacerla visible
        login_window = LoginWindow()
        login_window.transient(self)
        login_window.grab_set()
        self.wait_window(login_window)

    def show_singup_form(self):
        # Crear instancia de la clase LoginWindow y hacerla visible
        sigIn_window = SignupWindow()
        sigIn_window.transient(self)
        sigIn_window.grab_set()
        self.wait_window(sigIn_window)




