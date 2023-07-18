import tkinter as tk
from tkinter import ttk

def buscar_valor(tree, valor_buscado):
    for item in tree.get_children():
        # Obtener los valores de la fila actual en el treeview
        fila = tree.item(item)['values']
        # Comprobar si el valor buscado está en la fila actual
        if valor_buscado in fila:
            return item  # Devuelve el identificador del elemento en el treeview
    return None  # Si no se encuentra el valor, devuelve None

# Crear la ventana principal
root = tk.Tk()
root.title("Buscar en Treeview")

# Crear el Treeview con algunas filas
tree = ttk.Treeview(root, columns=('columna1', 'columna2'))
tree.heading('#0', text='ID')
tree.heading('columna1', text='Nombre')
tree.heading('columna2', text='Edad')

tree.insert('', 'end', text='1', values=('Juan', 25))
tree.insert('', 'end', text='2', values=('María', 30))
tree.insert('', 'end', text='3', values=('Carlos', 22))

tree.pack()

# Valor que queremos buscar
valor_buscado = 'María'

# Buscar el valor en el Treeview
item_encontrado = buscar_valor(tree, valor_buscado)
if item_encontrado is not None:
    print(f"Valor encontrado en el ítem: {item_encontrado}")
else:
    print("Valor no encontrado en el Treeview.")

root.mainloop()
