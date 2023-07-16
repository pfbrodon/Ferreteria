import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring

def modificar_elemento():
    # Obtén el elemento seleccionado en el Treeview
    seleccion = treeview.focus()
    
    if seleccion:
        # Obtén los datos actuales del elemento seleccionado
        datos_actuales = treeview.item(seleccion)['values']
        
        # Solicitar al usuario ingresar el nuevo valor
        nuevo_valor = askstring("Modificar valor", "Ingrese el nuevo valor", initialvalue=datos_actuales[0])
        
        if nuevo_valor:
            # Actualizar el elemento en el Treeview con el nuevo valor
            treeview.set(seleccion, column='#0', value=nuevo_valor)

# Crear una ventana
ventana = tk.Tk()

# Crear un Treeview con una columna
treeview = ttk.Treeview(ventana)
treeview.pack()

# Agregar algunos datos al Treeview
treeview.insert('', 'end', text='Dato 1', values=('Valor 1'))
treeview.insert('', 'end', text='Dato 2', values=('Valor 2'))
treeview.insert('', 'end', text='Dato 3', values=('Valor 3'))

# Botón para modificar el elemento seleccionado
boton_modificar = tk.Button(ventana, text="Modificar", command=modificar_elemento)
boton_modificar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
