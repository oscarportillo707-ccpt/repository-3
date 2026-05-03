import tkinter as tk


def saludar():
    print("¡Hola! Hiciste clic en el botón")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de botón")

# Crear botón
boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)

# Mostrar botón
boton.pack()

# Ejecutar aplicación
ventana.mainloop()
