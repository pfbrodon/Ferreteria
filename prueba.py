import tkinter as tk

# Función para obtener el valor seleccionado
def obtener_valor():
    valor = spinbox_var.get()
    print("Valor seleccionado:", valor)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Spinbox")

# Crear una variable para el Spinbox
spinbox_var= 10
#spinbox_var.set(10)  # Valor inicial

# Crear el Spinbox
spinbox = tk.Spinbox(ventana, from_=0, to=spinbox_var, increment=1, width=10)
spinbox.pack(pady=10)

# Crear un botón para obtener el valor seleccionado
boton_obtener = tk.Button(ventana, text="Obtener valor", command=obtener_valor)
boton_obtener.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
