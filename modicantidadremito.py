import sqlite3 
import tkinter as tk
from tkinter import *
from tkinter import Menu,ttk
from tkinter import Tk, Label, Button, Entry, messagebox
import os
from tkinter.font import Font

##CORRECCION DE RUTA DE ARCHIVOS#########################################
##########################################################################
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
###########################################################################



def modiCantidadRem():
    ventana=Tk()
    ventana.geometry("300x150+40+40")                                                    
    ventana.title("CARGA DE PRODUCTOS")
    ventana.resizable(width=False,height=False)#BLOQUEO DE REDIMENSION
    ventana.configure(background="lightblue")#COLOR DE FONDO DE VENTANA
    
    
    ventana.mainloop()
    
modiCantidadRem()
