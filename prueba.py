import tkinter as tk

def cambiar_rango():
    nuevo_rango = int(variable.get())  # Obtener el nuevo valor del rango
    spinbox.configure(to=nuevo_rango)  # Configurar el nuevo rango en el Spinbox

# Crear la ventana principal
ventana = tk.Tk()

# Crear una variable de control
variable = tk.StringVar()

# Establecer un valor inicial en la variable de control
variable.set("10")

# Crear el Spinbox y vincularlo con la variable de control
spinbox = tk.Spinbox(ventana, from_=0, to=100)
spinbox.pack()

# Crear un Entry para ingresar el nuevo rango
entry = tk.Entry(ventana, textvariable=variable)
entry.pack()

# Crear un botón para cambiar el rango del Spinbox
boton = tk.Button(ventana, text="Cambiar rango", command=cambiar_rango)
boton.pack()

# Ejecutar la ventana principal
ventana.mainloop()
