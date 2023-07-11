import tkinter as tk
from tkinter import ttk

# Crear la ventana
ventana = tk.Tk()

# Crear el estilo
style = ttk.Style()

# Configurar el estilo para los botones
style.map("TButton",
          foreground=[('pressed', 'red'), ('active', 'blue')],
          background=[('pressed', '!disabled', 'black'), ('active', 'white')])

# Crear un botón ttk
boton = ttk.Button(ventana, text="Mi botón")
boton.pack()

# Ejecutar la ventana
ventana.mainloop()
