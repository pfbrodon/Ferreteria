import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()

# Variable para almacenar el valor
variable = tk.StringVar()
variable.set("Hola Mundo")

# Crear el Label ttk y enlazarlo con la variable
label = ttk.Label(root, textvariable=variable)
label.pack()

# Actualizar el valor de la variable
variable.set("Nuevo Valor")

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
