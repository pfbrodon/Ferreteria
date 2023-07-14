import tkinter as tk
from tkinter import ttk

def modificar_valor():
    # Obtén la selección actual del treeview
    seleccion = treeview.selection()

    # Verifica que se haya seleccionado un elemento
    if seleccion:
        # Obtiene el identificador del elemento seleccionado
        item = seleccion[0]

        # Modifica los valores de las columnas
        nuevos_valores = ("Nuevo Valor 1", "Nuevo Valor 2", "Nuevo Valor 3")
        treeview.item(item, values=nuevos_valores)

# Crear ventana
ventana = tk.Tk()

# Crear Treeview
treeview = ttk.Treeview(ventana)
treeview.pack()

# Agregar columnas
treeview["columns"] = ("Columna 1", "Columna 2", "Columna 3")
treeview.column("#0", width=0, stretch=tk.NO)
treeview.column("Columna 1", width=100)
treeview.column("Columna 2", width=100)
treeview.column("Columna 3", width=100)

# Agregar encabezados de columnas
treeview.heading("#0", text="", anchor=tk.W)
treeview.heading("Columna 1", text="Columna 1", anchor=tk.W)
treeview.heading("Columna 2", text="Columna 2", anchor=tk.W)
treeview.heading("Columna 3", text="Columna 3", anchor=tk.W)

# Agregar datos
treeview.insert("", tk.END, text="Elemento 1", values=("Valor 1", "Valor 2", "Valor 3"))
treeview.insert("", tk.END, text="Elemento 2", values=("Valor 4", "Valor 5", "Valor 6"))

# Botón para modificar valor
boton_modificar = tk.Button(ventana, text="Modificar Valor", command=modificar_valor)
boton_modificar.pack()

ventana.mainloop()
