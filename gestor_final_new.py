import tkinter
from tkinter import font
from tkinter import ttk
#from ttkthemes import ThemedStyle #->> pip installa ttkthemes
from tkinter import messagebox
import os
import sqlite3 as lite

#Para abrir o cerrar todas las funciones. Cntrl+K+1, Cntrl+K+2
#https://icons8.com/icon/set/network/fluency

connection = None
cursor = None
db_name = "final_database.db"
place = ""
config_window_frame = None
rol = None


def main_app_admin(session_rol):
	if connection and session_rol == "admin":
		print(XD)





##########################################################
def reset_db_fn():
	global connection, cursor
	if connection:
		print("La base de datos esta conectada")
		messagebox.showwarning("Advertencia", "La base de datos está en uso")
		stop_question=messagebox.askyesno("Detener", "Desea detener la conexión?")
		if stop_question:
			connection.close()
			connection=None
			#LLAMAR A FUNCION STOP??
			root_window_login_footer_connection_label.config(text=f"Base de datos: Desconectado", fg="red")
			print("LA BASE DE DATOS HA SIDO DETENIDA")
			try:
				if os.path.exists(db_name):
					question=messagebox.askyesno("Confirmar", "Esta seguro que desea eliminar la base de datos? Esta acción no tiene retroceso")
					if question:
						os.remove("final_database.db")
						print("EXITO: Archivo removido exitosamente")
						messagebox.showinfo("Eliminado", "se ha eliminado la base de datos")
						question2=messagebox.askyesno("Finalizado", "Desea volver a crear la base y la conexión?")
						if question2:
							print("Volviendo a crear...")
							start()
							if connection:
								root_window_login_footer_connection_label.config(fg="#3b80b1")
								messagebox.showinfo("Exito", "Nueva base creada")
								conf
						else:
							config_window_frame.lift()
					else:
						print("DECISION: El usuario no quiso eliminar el archivo")
						question3=messagebox.askyesno("Saliendo", "Presionde Si para volver a conectar o No para salir")
		#Bugeado
						if question:
							start()
							config_window_frame.lift()
						else:
							config_window_frame.destroy()
							root_window_login_frame.destroy()
				else:
					print(f"ERROR: No se encuentra la base de datos. El archivo {db_name} no existe.")
			except:
				print(f"ERROR: No se eliminó el archivo {db_name}. No se puede desconectar.")
		else:
			config_window_frame.lift()
			print("Accion cancelada por el usuario")

def insert_data_button_fn():
	if connection:
		try:
			cursor.execute("INSERT INTO usuarios (nombre, contr, rol) VALUES (?, ?, ?)", ("admin", "admin", "admin"))
			connection.commit()
			print("SE HA INSERTADO EL USUARIO admin EXITOSAMENTE")
			messagebox.showinfo("", "Se ha insertado el usuario admin, admin, admin")
			config_window_frame.lift()
		except lite.Error as e:
			print("ERROR INSERTANDO DATOS. ERROR FUNCTION: insert_data_button_fn ERROR CODE: {e}")
			messagebox.showerror("Error", "No se pudo insertar la data")
			config_window_frame.lift()
	else:
		print("NO SE PUDO CONECTAR CON LA BASE DE DATOS. ERROR FUNCTION:insert_data_button_fn")

def login_autentication(user_entry, pass_entry):
	user_name=user_entry.get()
	user_pass=pass_entry.get()

	if connection:
		try:
			cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contr = ?", (user_name, user_pass))
			success=cursor.fetchone()
			if success:
				print("SE ENCONTRO EL USUARIO!")
				
				cursor.execute("SELECT * FROM usuarios WHERE rol = 'admin'")
				session_rol=cursor.fetchone()
				if session_rol:
					print("BIENVENIDO ADMIN!")
					main_app_admin(session_rol)
			else:
				print("NO SE ENCONTRO EL USUARIO")
		except lite.Error as e:
			print("NO SE PUDO ENCONTRAR EL USUARIO. ERROR CODE: ", e)
			
			messagebox.showwarning("Error", "No se encontró el usuario")




			# No funciona
			if e=="no such table: usuarios":
				print("no existe la tabla usuarios")
	else:
		print("NO SE PUDO CONECTAR")

def close_config_window():
	global config_window_frame
	config_window_frame.destroy()
	config_window_frame=None



def create_tables_button_fn():
	if connection:
		try:
			cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id integer PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) NOT NULL, contr VARCHAR(100) NOT NULL, rol VARCHAR(6) NOT NULL)")
			connection.commit()
			print("TABLA usuarios CREADA EXITOSAMENTE")
			messagebox.showinfo("", "Se ha creado la tabla usuarios")
			config_window_frame.lift()
		except lite.Error as e:
			print("NO SE PUDO CREAR LA TABLA usuarios", e)
			messagebox.showerror("Error", "No se pudo crear la tabla ")
			config_window_frame.lift()
	else:
		print("NO SE PUDO CONECTAR CON LA BASE DE DATOS ERROR:create_tables_button_fn")

def config_button_fn():
	global config_window_frame

	if config_window_frame is not None and config_window_frame.winfo_exists():
		config_window_frame.lift()
		return

	config_window_frame=tkinter.Toplevel()
	config_window_frame.geometry("400x230")
	config_window_frame.iconbitmap("config.ico")

	#Header
	config_window_header_label=tkinter.Label(config_window_frame, text="Herramientas", bg="black", fg="white", font=("Segoe UI", 16))
	config_window_header_label.place(x=0, y=0, width=400, height=40)

	#bg="#9cb7d3"


	#DB_Button_Reset
	db_reset_button=ttk.Button(config_window_frame, text="Reiniciar base", command=reset_db_fn)
	db_reset_button.place(x=20, y=50, width=100, height=30)

	#DB_Button_Reset_Description
	db_reset_button_des=ttk.Label(config_window_frame, text="Restablece la base de datos", style="config_description.TLabel")
	db_reset_button_des.place(x=140, y=50, width=200, height=30)

	#1-Separator
	config_window_separator1=ttk.Separator(config_window_frame, orient="horizontal")
	config_window_separator1.place(x=0, y=90, width=400)

	#DB_Button_Tables
	db_tables_button=ttk.Button(config_window_frame, text="Crear tablas", command=create_tables_button_fn)
	db_tables_button.place(x=20, y=100, width=100, height=30)

	#DB_Button_Tables_Description
	db_tables_button_des=ttk.Label(config_window_frame, text="Crea las tablas necesarias", style="config_description.TLabel")
	db_tables_button_des.place(x=140, y=100, width=200, height=30)

	#2-Separator
	config_window_separator2=ttk.Separator(config_window_frame, orient="horizontal")
	config_window_separator2.place(x=0, y=140, width=400)

	#DB_Button_Data
	db_data_button=ttk.Button(config_window_frame, text="Insertar datos", command=insert_data_button_fn)
	db_data_button.place(x=20, y=150, width=100, height=30)

	#DB_Button_Data_Description
	db_data_button_des=ttk.Label(config_window_frame, text="Inserta los datos necesarios", style="config_description.TLabel")
	db_data_button_des.place(x=140, y=150, width=200, height=30)

	#Close_Button
	close_button=ttk.Button(config_window_frame, text="Cerrar", command=close_config_window)
	close_button.place(x=280, y=190, width=100, height=30)


	#DB_

def exit(place):
	global connection

	if place == "login":
		if connection:
			connection.close()
			print("Conexion cerrada. Saliendo...")
		root_window_login_frame.destroy()
		
def start():
	global connection, cursor
	###############################################      Start-sqlite3-connection
	connection = lite.connect(db_name)
	cursor = connection.cursor()
	if connection:
		print("Conexión exitosa")
		root_window_login_footer_connection_label.config(text=f"Base de datos: Conectado ✔")
	else:
		messagebox.showerror("Error", "No se pudo conectar a la base de datos")
		#print("Error de conexion. Saliendo...")
		#root_window_login_frame.destroy()
	return connection

root_window_login_frame=tkinter.Tk()
root_window_login_frame.geometry("400x300")
root_window_login_frame.resizable(0,0)
root_window_login_frame.title("Gestor")
root_window_login_frame.protocol("WM_DELETE_WINDOW", lambda:exit(place="login"))
root_window_login_frame.config(bg="Grey91")
root_window_login_frame.iconbitmap("icon.ico")
#Header
root_window_login_header=tkinter.Label(root_window_login_frame, text="Iniciar Sesión", font=("Segoe UI", 22), bg="black", fg="white")
root_window_login_header.place(x=0, y=0, width=400, height=50)
#Header_happy cloud
cloudy=tkinter.PhotoImage(file=("smiley_cloud.png"))
cloudy_label=tkinter.Label(root_window_login_frame, image=cloudy, bd=0)
cloudy_label.place(x=15, y=1, width=49, height=49)
#User
user_entry_label=tkinter.Label(root_window_login_frame, text="Nombre: ", font=("Segoe UI", 10), bg="Grey91")
user_entry_label.place(x=50, y=90)
user_entry=tkinter.Entry(root_window_login_frame, font=("Segoe UI", 10))
user_entry.place(x=120, y=90,  width=230, height=23)
#Pass
pass_entry_label=tkinter.Label(root_window_login_frame, text="Contraseña: ", font=("Segoe UI", 10), bg="Grey91")
pass_entry_label.place(x=34, y=140)
pass_entry=tkinter.Entry(root_window_login_frame, font=("Segoe UI", 10), show="*")
pass_entry.place(x=120, y=140, width=230, height=23)
#Login Button
login_button=ttk.Button(root_window_login_frame, text='Iniciar',style="login.TButton", command=lambda:login_autentication(user_entry, pass_entry))
login_button.place(x=125, y=190, width=150, height=50)
#Footer
root_window_login_footer_label=tkinter.Label(root_window_login_frame, bg="black")
root_window_login_footer_label.place(x=0, y=270, width=400, height=30)
#Footer connection
root_window_login_footer_connection_label=tkinter.Label(root_window_login_frame, text="Base de datos: Desconectado", font=("Segoe UI", 8, "bold"), bg="black", fg="#3b80b1")
root_window_login_footer_connection_label.place(x=10, y=275, width=150, height=20)
#Footer-config-button
footer_config_button=tkinter.Button(root_window_login_frame, text="Herramientas", bg="black", fg="#3b80b1", bd=0, command=config_button_fn, font=("Segoe UI", 8))
footer_config_button.place(x=310, y=272, width=80, height=25)
start()

#style = ThemedStyle()

style = ttk.Style()

style.theme_use('vista')
print(style.theme_names())  # Lista de temas disponibles
style.configure('login.TButton', font=('Segoe UI', 20, "bold"))


style.configure('config_description.TLabel', font=('Segoe UI', 9))



root_window_login_frame.mainloop()