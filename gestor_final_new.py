import tkinter
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3 as lite

connection = None
cursor = None
db_name = "final_database.db"
place = ""




def footer_config_button_fn():
	config_window_frame=tkinter.Toplevel()
	config_window_frame.geometry("400x200")


	config_window_header_label=tkinter.Label(config_window_frame, text="Herramientas", bg="#9cb7d3", font="Arial 15")
	config_window_header_label.place(x=0, y=0, width=400, height=40)


	#DB_Button(login.TButton)
	db_button=ttk.Button(config_window_frame, text="Base de datos")
	db_button.place(x=20, y=50, width=100, height=30)



def exit(place):
	global connection

	if place == "login":
		connection.close()
		root_window_login_frame.destroy()
		print("Conexion cerrada. Saliendo...")

def start():
	global connection, cursor

	connection = lite.connect(db_name)
	cursor = connection.cursor()
	if connection:
		print("Conexión exitosa")
		root_window_login_footer_connection_label.config(text=f"Base de datos: Conectado ✔")
	else:
		messagebox.showerror("Error", "No se pudo conectar a la base de datos")
		print("Error de conexion. Saliendo...")
		root_window_login_frame.destroy()

root_window_login_frame=tkinter.Tk()
root_window_login_frame.geometry("400x300")
root_window_login_frame.resizable(0,0)
root_window_login_frame.title("")
root_window_login_frame.protocol("WM_DELETE_WINDOW", lambda:exit(place="login"))
root_window_login_frame.config(bg="Grey91")
#Header
root_window_login_header=tkinter.Label(root_window_login_frame, text="Iniciar Sesión", font=("Segoe UI", 20), bg="#9cb7d3", fg="black")
root_window_login_header.place(x=0, y=0, width=400, height=50)
#User
user_entry_label=tkinter.Label(root_window_login_frame, text="Nombre: ", font=("Segoe UI", 10), bg="Grey91")
user_entry_label.place(x=50, y=90)
user_entry=tkinter.Entry(root_window_login_frame, font=("Segoe UI", 10))
user_entry.place(x=120, y=90,  width=230, height=23)
#Pass
pass_entry_label=tkinter.Label(root_window_login_frame, text="Contraseña: ", font=("Segoe UI", 10), bg="Grey91")
pass_entry_label.place(x=34, y=140)
pass_entry=tkinter.Entry(root_window_login_frame, font=("Segoe UI", 10))
pass_entry.place(x=120, y=140, width=230, height=23)
#Login Button
login_button=ttk.Button(root_window_login_frame, text='Iniciar',style="login.TButton")
login_button.place(x=125, y=190, width=150, height=50)
#Footer
root_window_login_footer_label=tkinter.Label(root_window_login_frame, bg="#9cb7d3")
root_window_login_footer_label.place(x=0, y=270, width=400, height=30)
#Footer connection
root_window_login_footer_connection_label=tkinter.Label(root_window_login_frame, text="Base de datos: Desconectado", font="Calibri 8", bg="#9cb7d3", fg="black")
root_window_login_footer_connection_label.place(x=10, y=275, width=150, height=20)
#Footer-config-button
footer_config_button=tkinter.Button(root_window_login_frame, text="Herramientas", bg="#9cb7d3", fg="black", bd=0, command=footer_config_button_fn)
footer_config_button.place(x=310, y=272, width=80, height=25)
start()

style = ttk.Style()
style.theme_use('vista')
style.configure('login.TButton', font=('Arial', 20))





root_window_login_frame.mainloop()