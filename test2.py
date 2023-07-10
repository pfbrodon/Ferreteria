import tkinter as tk
from tkinter import ttk

# Función que se ejecuta cuando cambia la selección en el TreeView
def on_treeview_select(event):
    item = tree.focus()  # Obtener el elemento seleccionado
    values = tree.item(item)['values']  # Obtener los valores del elemento seleccionado
    print("Elemento seleccionado:", values)
    print(values[0])
    print(values[1])

# Crear la ventana
ventana = tk.Tk()

# Crear el TreeView
tree = ttk.Treeview(ventana, show="headings")
tree.pack()

# Agregar columnas
tree['columns'] = ('Nombre', 'Edad', 'Correo')

# Establecer etiquetas de las columnas
tree.heading('Nombre', text='Nombre')
tree.heading('Edad', text='Edad')
tree.heading('Correo', text='Correo')

# Agregar filas de datos
tree.insert('', 'end', values=('Juan', '25', 'juan@example.com'))
tree.insert('', 'end', values=('Maria', '30', 'maria@example.com'))
tree.insert('', 'end', values=('Pedro', '28', 'pedro@example.com'))

# Asociar el evento de selección al TreeView
tree.bind("<<TreeviewSelect>>", on_treeview_select)

# Ejecutar la ventana
ventana.mainloop()
