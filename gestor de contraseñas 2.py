import tkinter as tk
from tkinter import messagebox
from conexion import Conexion



usuarios = {}
credenciales_guardadas = {}

def registrar():
    username = entry_username_registro.get()
    password = entry_password_registro.get()
    pin = entry_pin_registro.get()
    
    if username in usuarios:
        messagebox.showerror("Error", "El usuario ya existe.")
    elif username == "" or password == "" or pin == "":
        messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
    elif len(pin) != 4 or not pin.isdigit():
        messagebox.showerror("Error", "El PIN debe tener 4 números.")
    else:
        usuarios[username] = {'password': password, 'pin': pin}
        messagebox.showinfo("Registro", "Usuario registrado con éxito.")
        entry_username_registro.delete(0, tk.END)
        entry_password_registro.delete(0, tk.END)
        entry_pin_registro.delete(0, tk.END)

def iniciar_sesion():
    username = entry_username_login.get()
    password = entry_password_login.get()
    
    if username in usuarios and usuarios[username]['password'] == password:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
        abrir_ventana_principal(username)  
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def recuperar_contraseña():
    username = entry_username_recuperar.get()
    pin = entry_pin_recuperar.get()
    
    if username in usuarios and usuarios[username]['pin'] == pin:
        password = usuarios[username]['password']
        messagebox.showinfo("Recuperar Contraseña", f"La contraseña es: {password}")
    else:
        messagebox.showerror("Error", "Usuario o PIN incorrectos.")

def mostrar_frame_recuperar():
    frame_recuperar.pack(pady=10)


def abrir_ventana_principal(username):
    
    root.withdraw()

    
    ventana_principal = tk.Toplevel(root)
    ventana_principal.title("Gestor de Sitios y Credenciales")

    
    def guardar_credenciales():
        sitio = entry_sitio.get()
        usuario_sitio = entry_usuario_sitio.get()
        password_sitio = entry_password_sitio.get()

        if sitio and usuario_sitio and password_sitio:
            if username not in credenciales_guardadas:
                credenciales_guardadas[username] = {}
            credenciales_guardadas[username][sitio] = {'usuario': usuario_sitio, 'password': password_sitio}
            messagebox.showinfo("Guardado", "Credenciales guardadas con éxito.")
            entry_sitio.delete(0, tk.END)
            entry_usuario_sitio.delete(0, tk.END)
            entry_password_sitio.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    
    def mostrar_credenciales():
        pin = entry_pin_ver_credenciales.get()

        if pin == usuarios[username]['pin']:
            ventana_credenciales = tk.Toplevel(ventana_principal)
            ventana_credenciales.title("Credenciales Guardadas")
            if username in credenciales_guardadas:
                row = 0
                for sitio, datos in credenciales_guardadas[username].items():
                    tk.Label(ventana_credenciales, text=f"Sitio: {sitio}").grid(row=row, column=0)
                    tk.Label(ventana_credenciales, text=f"Usuario: {datos['usuario']}").grid(row=row, column=1)
                    tk.Label(ventana_credenciales, text=f"Contraseña: {datos['password']}").grid(row=row, column=2)
                    boton_eliminar = tk.Button(ventana_credenciales, text="Eliminar", command=lambda sitio=sitio: eliminar_credencial(sitio, ventana_credenciales))
                    boton_eliminar.grid(row=row, column=3)
                    row += 1
            else:
                messagebox.showinfo("Sin credenciales", "No hay credenciales guardadas para este usuario.")
        else:
            messagebox.showerror("Error", "PIN incorrecto.")

    
    def eliminar_credencial(sitio, ventana_credenciales):
        if sitio in credenciales_guardadas[username]:
            del credenciales_guardadas[username][sitio]
            messagebox.showinfo("Eliminado", f"Credenciales de {sitio} eliminadas.")
            ventana_credenciales.destroy()

    
    def cerrar_sesion():
        ventana_principal.destroy()  
        root.deiconify()  

    
    label_sitio = tk.Label(ventana_principal, text="Sitio:")
    label_sitio.grid(row=0, column=0)
    entry_sitio = tk.Entry(ventana_principal)
    entry_sitio.grid(row=0, column=1)

    label_usuario_sitio = tk.Label(ventana_principal, text="Usuario del sitio:")
    label_usuario_sitio.grid(row=1, column=0)
    entry_usuario_sitio = tk.Entry(ventana_principal)
    entry_usuario_sitio.grid(row=1, column=1)

    label_password_sitio = tk.Label(ventana_principal, text="Contraseña del sitio:")
    label_password_sitio.grid(row=2, column=0)
    entry_password_sitio = tk.Entry(ventana_principal, show='*')
    entry_password_sitio.grid(row=2, column=1)

    boton_guardar_credenciales = tk.Button(ventana_principal, text="Guardar Credenciales", command=guardar_credenciales)
    boton_guardar_credenciales.grid(row=3, columnspan=2)

    
    label_pin_ver_credenciales = tk.Label(ventana_principal, text="Ingrese PIN para ver credenciales:")
    label_pin_ver_credenciales.grid(row=4, column=0)
    entry_pin_ver_credenciales = tk.Entry(ventana_principal, show='*')
    entry_pin_ver_credenciales.grid(row=4, column=1)

    boton_mostrar_credenciales = tk.Button(ventana_principal, text="Ver Credenciales", command=mostrar_credenciales)
    boton_mostrar_credenciales.grid(row=5, columnspan=2)

    
    boton_cerrar_sesion = tk.Button(ventana_principal, text="Cerrar Sesión", command=cerrar_sesion)
    boton_cerrar_sesion.grid(row=6, columnspan=2, pady=10)


root = tk.Tk()
root.title("Registro y Login")


frame_registro = tk.Frame(root)
frame_registro.pack(pady=10)

label_username_registro = tk.Label(frame_registro, text="Usuario:")
label_username_registro.grid(row=0, column=0)
entry_username_registro = tk.Entry(frame_registro)
entry_username_registro.grid(row=0, column=1)

label_password_registro = tk.Label(frame_registro, text="Contraseña:")
label_password_registro.grid(row=1, column=0)
entry_password_registro = tk.Entry(frame_registro, show='*')
entry_password_registro.grid(row=1, column=1)

label_pin_registro = tk.Label(frame_registro, text="PIN (4 números):")
label_pin_registro.grid(row=2, column=0)
entry_pin_registro = tk.Entry(frame_registro, show='*')
entry_pin_registro.grid(row=2, column=1)

boton_registrar = tk.Button(frame_registro, text="Registrar", command=registrar)
boton_registrar.grid(row=3, columnspan=2)


frame_login = tk.Frame(root)
frame_login.pack(pady=10)

label_username_login = tk.Label(frame_login, text="Usuario:")
label_username_login.grid(row=0, column=0)
entry_username_login = tk.Entry(frame_login)
entry_username_login.grid(row=0, column=1)

label_password_login = tk.Label(frame_login, text="Contraseña:")
label_password_login.grid(row=1, column=0)
entry_password_login = tk.Entry(frame_login, show='*')
entry_password_login.grid(row=1, column=1)

boton_login = tk.Button(frame_login, text="Iniciar Sesión", command=iniciar_sesion)
boton_login.grid(row=2, columnspan=2)


boton_mostrar_recuperar = tk.Button(root, text="¿Olvidaste tu contraseña?", command=mostrar_frame_recuperar)
boton_mostrar_recuperar.pack(pady=10)

frame_recuperar = tk.Frame(root)

label_username_recuperar = tk.Label(frame_recuperar, text="Usuario:")
label_username_recuperar.grid(row=0, column=0)
entry_username_recuperar = tk.Entry(frame_recuperar)
entry_username_recuperar.grid(row=0, column=1)

label_pin_recuperar = tk.Label(frame_recuperar, text="PIN (4 números):")
label_pin_recuperar.grid(row=1, column=0)
entry_pin_recuperar = tk.Entry(frame_recuperar, show='*')
entry_pin_recuperar.grid(row=1, column=1)

boton_recuperar = tk.Button(frame_recuperar, text="Recuperar Contraseña", command=recuperar_contraseña)
boton_recuperar.grid(row=2, columnspan=2)

root.mainloop()

