import sqlite3 
import tkinter as tk
from tkinter import *
from tkinter import Menu,ttk
from tkinter import Tk, Label, Button, Entry, messagebox
import os
from tkinter.font import Font
#from moduloremito import tablaRemito
##CORRECCION DE RUTA DE ARCHIVOS#########################################
##########################################################################
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
###########################################################################



def modiCantidadRem():
    ventanacant=Tk()
    ventanacant.geometry("300x150+40+40")                                                    
    ventanacant.title("CARGA DE PRODUCTOS")
    ventanacant.resizable(width=False,height=False)#BLOQUEO DE REDIMENSION
    ventanacant.configure(background="lightblue")#COLOR DE FONDO DE VENTANA
    spinCant= 0
    ##SPINBOX##########################################################################################
    spinboxcant = ttk.Spinbox(ventanacant, from_=0, to=spinCant, increment=1, width=5)
    spinboxcant.place(x=20,y=60) 
    
    ventanacant.mainloop()
    
#modiCantidadRem()
