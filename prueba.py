import tkinter as tk
import tkinter.ttk as ttk

def imprimir_treeview(treeview):
    # Obtener todas las columnas del TreeView
    columnas = treeview['columns']
    
    # Imprimir los encabezados de las columnas
    encabezados = [treeview.heading(column)['text'] for column in columnas]
    encabezados_str = '\t'.join(encabezados)
    print(encabezados_str)
    
    # Recorrer los elementos y subelementos del TreeView
    for item in treeview.get_children():
        # Obtener los valores de cada columna para el elemento actual
        valores = [treeview.item(item, 'values')[column] for column in columnas]
        valores_str = '\t'.join(valores)
        print(valores_str)

# Crear la ventana principal
ventana = tk.Tk()

# Crear el TreeView
treeview = ttk.Treeview(ventana)

# Agregar columnas al TreeView
treeview['columns'] = ('columna1', 'columna2', 'columna3')
treeview.heading('#0', text='Elemento')
treeview.heading('columna1', text='Columna 1')
treeview.heading('columna2', text='Columna 2')
treeview.heading('columna3', text='Columna 3')

# Agregar elementos y subelementos al TreeView
treeview.insert('', 'end', text='Elemento 1', values=('Valor 1.1', 'Valor 1.2', 'Valor 1.3'))
treeview.insert('', 'end', text='Elemento 2', values=('Valor 2.1', 'Valor 2.2', 'Valor 2.3'))
subelemento = treeview.insert('Elemento 2', 'end', text='Subelemento', values=('Valor sub.1', 'Valor sub.2', 'Valor sub.3'))

# Imprimir el contenido del TreeView
imprimir_treeview(treeview)

# Mostrar la ventana
ventana.mainloop()
