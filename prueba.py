import tkinter as tk

# Función para mostrar el valor seleccionado
def mostrar_valor():
    valor = spinbox.get()
    print(f"Valor seleccionado: {valor}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Spinbox")

# Crear el Spinbox
spinbox = tk.Spinbox(ventana, from_=0, to=100, increment=1, width=10)

# Crear un botón para mostrar el valor seleccionado
boton_mostrar = tk.Button(ventana, text="Mostrar valor", command=mostrar_valor)

# Mostrar el Spinbox y el botón en la ventana
spinbox.pack(pady=10)
boton_mostrar.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
