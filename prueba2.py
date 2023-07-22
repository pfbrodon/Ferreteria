import tkinter as tk
from tkinter import ttk

def buscar_elemento(tree, texto_buscado):
    for item in tree.get_children():
        if texto_buscado.lower() in tree.item(item, 'values')[0].lower():
            print ()
            return item
    return None

def seleccionar_elemento():
    texto_buscado = entry_busqueda.get()
    if texto_buscado.strip() == "":
        return

    elemento_encontrado = buscar_elemento(treeview, texto_buscado)
    if elemento_encontrado:
        treeview.selection_set(elemento_encontrado)
        treeview.focus(elemento_encontrado)

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo TreeView")

# Crear el TreeView
treeview = ttk.Treeview(root, columns=("Columna1", "Columna2"))
treeview.heading("#1", text="Columna 1")
treeview.heading("#2", text="Columna 2")

# Agregar algunos datos de ejemplo al TreeView
treeview.insert("", "end", values=("Elemento 1", "Valor 1"))
treeview.insert("", "end", values=("Elemento 2", "Valor 2"))
treeview.insert("", "end", values=("Elemento 3", "Valor 3"))
treeview.insert("", "end", values=("Elemento 4", "Valor 4"))
treeview.insert("", "end", values=("Elemento 5", "Valor 5"))

treeview.pack()

# Crear un cuadro de entrada y un botón para buscar y seleccionar elementos
entry_busqueda = tk.Entry(root)
entry_busqueda.pack()
btn_buscar = tk.Button(root, text="Buscar y Seleccionar", command=seleccionar_elemento)
btn_buscar.pack()

root.mainloop()
