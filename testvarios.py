import tkinter as tk

ventana = tk.Tk()

# Crear un cuadro principal
cuadro_principal = tk.Frame(ventana, width=400, height=300, bg="gray")
cuadro_principal.pack()

# Crear marcos internos dentro del cuadro principal
marco1 = tk.Frame(cuadro_principal, width=200, height=100, bg="blue",highlightthickness=3)
marco1.pack(side="left")

marco2 = tk.Frame(cuadro_principal, width=200, height=100, bg="green",highlightthickness=2,highlightbackground='gray')
marco2.pack(side="right")

ventana.mainloop()
