import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label, Button, Entry, messagebox
import os
from tkinter.font import Font

###########################################################################
#CONFIGURACION INICIAL VENTANA PRINCIPAL
ventana=Tk()
ventana.geometry("720x500")                                                    
ventana.title("PRUEBA DE VENTANAS Y FRAMES")

#CREACION DE UN MARCO#########################################
cuadro1=tk.Frame(ventana,width=300,height=300,borderwidth=2,
        highlightthickness=2,
        highlightbackground="black",padx=10,pady=10)
cuadro1.pack(padx=1,pady=10)

rotulo_titulo=tk.Label(cuadro1,
        text="CONVERSOR DE TEMPERATURAS",
        bg="lightblue",fg="black",
        font="consolas 20 bold",
        relief=tk.GROOVE,bd=2,
        padx=10,pady=10)
rotulo_titulo.pack(padx=20,pady=20)

mainloop()