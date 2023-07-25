import tkinter as tk
from tkinter import ttk

def hacer_foco_y_mover_scroll(treeview, index):
    # Hacer foco en el elemento deseado
    treeview.focus_set()  # Establecer el foco en el TreeView
    treeview.selection_set(index)  # Seleccionar el elemento por su índice
    treeview.focus(index)  # Establecer el foco en el elemento seleccionado

    # Mover el scroll para mostrar el elemento seleccionado
    treeview.see(index)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo TreeView")

# Crear el TreeView
mi_treeview = ttk.Treeview(ventana)
mi_treeview.pack()

# Agregar algunos elementos de ejemplo al TreeView
for i in range(1, 21):
    mi_treeview.insert("", "end", text=f"Elemento {i}")

# Índice del elemento que deseas mostrar (puede ser cualquier número válido)
indice_deseado = 15

# Hacer foco y mover el scroll para mostrar el elemento deseado
hacer_foco_y_mover_scroll(mi_treeview, indice_deseado)

# Ejecutar la ventana
ventana.mainloop()
