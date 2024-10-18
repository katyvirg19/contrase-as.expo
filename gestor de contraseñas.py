import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Diccionario para almacenar las aplicaciones, usuarios y contraseñas
credenciales = {}

# Función para agregar una nueva credencial
def agregar_credencial():
    app = entrada_aplicacion.get().strip()
    usuario = entrada_usuario.get().strip()
    contraseña = entrada_contraseña.get().strip()

    if app and usuario and contraseña:
        if app not in credenciales:
            credenciales[app] = {}
        credenciales[app][usuario] = contraseña
        messagebox.showinfo("Éxito", f"Credencial agregada para {app}.")
        limpiar_campos()
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# Función para mostrar todas las credenciales almacenadas
def mostrar_credenciales():
    if credenciales:
        info = ""
        for app, usuarios in credenciales.items():
            info += f"Aplicación: {app}\n"
            for usuario, contraseña in usuarios.items():
                info += f"  - Usuario: {usuario}, Contraseña: {contraseña}\n"
        messagebox.showinfo("Credenciales Guardadas", info)
    else:
        messagebox.showinfo("Sin Datos", "No hay credenciales guardadas.")

# Función para eliminar una credencial específica
def eliminar_credencial():
    app = entrada_aplicacion.get().strip()
    if app in credenciales:
        usuario = simpledialog.askstring("Eliminar Usuario", f"Ingrese el usuario para la aplicación '{app}':")
        if usuario in credenciales[app]:
            del credenciales[app][usuario]
            if not credenciales[app]:  # Eliminar la aplicación si no tiene más usuarios
                del credenciales[app]
            messagebox.showinfo("Éxito", f"Usuario '{usuario}' eliminado de '{app}'.")
        else:
            messagebox.showwarning("Error", f"El usuario '{usuario}' no existe en '{app}'.")
    else:
        messagebox.showwarning("Error", f"No hay datos para la aplicación '{app}'.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_aplicacion.delete(0, tk.END)
    entrada_usuario.delete(0, tk.END)
    entrada_contraseña.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Contraseñas")
ventana.geometry("400x350")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Aplicación:").pack(pady=5)
entrada_aplicacion = tk.Entry(ventana, width=30)
entrada_aplicacion.pack(pady=5)

tk.Label(ventana, text="Usuario:").pack(pady=5)
entrada_usuario = tk.Entry(ventana, width=30)
entrada_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:").pack(pady=5)
entrada_contraseña = tk.Entry(ventana, width=30, show="*")
entrada_contraseña.pack(pady=5)

# Botones para las acciones
tk.Button(ventana, text="Agregar", command=agregar_credencial).pack(pady=5)
tk.Button(ventana, text="Mostrar Credenciales", command=mostrar_credenciales).pack(pady=5)
tk.Button(ventana, text="Eliminar Credencial", command=eliminar_credencial).pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()