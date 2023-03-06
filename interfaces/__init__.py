from tkinter import *
import tkinter as tk
import tkinter.messagebox as MessageBox
import users.Login
import users.SigIn
import admin.AdminsMenu


class MainMenu(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Login/Signup")
    self.geometry("250x300")
    seccion1 = Frame(self, bg="blue")
    seccion1.pack(expand=True, fill="both")

    # Widgets
    #Inicio Label
    welcome_label = tk.Label(seccion1, text="Bienvenido elija una opcion:", bg="blue", fg="white", font=("Arial", 12))
    welcome_label.pack(pady=10)

    #Login Button
    login_btn = tk.Button(seccion1, text="Login", command=self.show_login_form,bg="green", fg="white", font=("Arial", 12))
    login_btn.pack(pady=10)

    #Signup Button
    signup_btn = tk.Button(seccion1, text="Signup", command=self.show_signup_form, bg="red", fg="white", font=("Arial", 12))
    signup_btn.pack(pady=10)

    #Iniciar como admin
    admin_btn = tk.Button(seccion1, text="Iniciar como admin", command=self.show_admin_form, bg="yellow", fg="black", font=("Arial", 12))
    admin_btn.pack(pady=10)

    #Cerrar Button
    close_btn = tk.Button(seccion1, text="Cerrar", command=self.destroy, bg="red", fg="white", font=("Arial", 12))
    close_btn.pack(pady=10)

  def show_login_form(self):
    # Implementar la ventana para el Login
    login_window = users.Login.LoginWindow()
    login_window.transient(self)
    login_window.grab_set()
    self.wait_window(login_window)

  def show_signup_form(self):
    # Implementar la ventana para el SignUp
    signup_window = users.SigIn.SignupWindow()
    signup_window.transient(self)
    signup_window.grab_set()
    self.wait_window(signup_window)

  def show_admin_form(self):
    #Conecta al menu de admin
    admin_window = admin.AdminsMenu.MenuAdmin()
    admin_window.transient(self)
    admin_window.grab_set()
    self.wait_window(admin_window)


if __name__ == "__main__":
  app = MainMenu()
  app.mainloop()