import tkinter as tk
from tkinter import ttk

def modificar_datos_seleccionados():
    # Obtener el índice del elemento seleccionado
    seleccion = tree.selection()
    if seleccion:
        indice = tree.index(seleccion)
        print(indice)
        # Obtener los valores del elemento seleccionado
        item = tree.item(seleccion)
        valores = item["values"]
        
        # Modificar los valores del elemento seleccionado
        nuevos_valores = (valores[0] + " (modificado)", valores[1] + " (modificado)")
        
        # Actualizar el elemento en el TreeView
        tree.item(seleccion, values=nuevos_valores)

# Crear la ventana principal
ventana = tk.Tk()

# Crear el TreeView
tree = ttk.Treeview(ventana)
tree["columns"] = ("columna1", "columna2")  # Definir las columnas del TreeView
tree.heading("#0", text="Dato")  # Encabezado de la primera columna
tree.heading("columna1", text="Columna 1")  # Encabezado de la segunda columna
tree.heading("columna2", text="Columna 2")  # Encabezado de la tercera columna
tree.pack()

# Agregar algunos datos al TreeView
datos = [
    ("Dato 1", "Valor 1"),
    ("Dato 2", "Valor 2"),
    ("Dato 3", "Valor 3")
]
for dato in datos:
    tree.insert("", "end", values=dato)

# Botón para modificar los datos seleccionados
boton_modificar = tk.Button(ventana, text="Modificar", command=modificar_datos_seleccionados)
boton_modificar.pack()

ventana.mainloop()
