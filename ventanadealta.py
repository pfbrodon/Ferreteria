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

#mostrarBotones = False#INICIALIZAR VARIABLES
####VENTANA DE MODULO DE CARGA#######################################
def moduloCarga():
    ventana=Tk()
    ventana.geometry("450x250")                                                    
    ventana.title("CARGA DE PRODUCTOS")
    #cuadro1=Frame(ventana,width=300,height=100,highlightthickness=2)
    ##HABILITA EL BOTON DE GUARDADO
    def mostrarGuardar(ver):
        print("Mostrar",ver)
        if ver:
            botonGuardar.place(x=230,y=170)
        else:
            botonGuardar.place_forget()
    
    ##LIMPIEZA DE LAS ENTRADAS
    def limpiarEntry():
        entradaCodigo.delete(0, tk.END)
        entradaCategoria.delete(0, tk.END)
        entradaDescripcion.delete(0, tk.END)
        entradaCantidad.delete(0, tk.END)
        entradaPrecio.delete(0, tk.END)
        entradaPrecioVP.delete(0, tk.END)


    
    ##INICIALIZAR VARIABLES
    codigoBusq=()
    itemTabla=()
    ###########################################################################################################################################################    
    ##VALIDACION DE CODIGO########################################################################################################################################################
    def validarCodigo():          
        try:    
            codigoProducto=int(entradaCodigo.get())
        except:
            print('el codigo debe ser un numero')
            entradaCodigo.delete(0, tk.END)
        print (codigoProducto)
        mi_conexion= sqlite3.connect("basededatosPrueba.db")  
        cursor=mi_conexion.cursor() 
        instruccion= f"SELECT * FROM stockFerreteria WHERE codigo='{codigoProducto}' "
        cursor.execute(instruccion)
        datos=cursor.fetchall()
        mi_conexion.commit()
        mi_conexion.close()
        for fila in datos:
            if fila[0]==codigoProducto:
                entradaCodigo.delete(0, tk.END)
                messagebox.showwarning( "",f"EL CODIGO {fila[0]} YA EXISTE")
                ventana.lift()#TRAE AL FRENTE LA VENTANA DE ALTA DESPUES DEL SHOWWARNING
                print(f"El codigo:{fila[0]}, ya esxite")
                break

        else:
            #mostrarGuardar(ver=True)
            entradaCategoria['state'] = tk.NORMAL
            entradaDescripcion['state'] = tk.NORMAL
            entradaCantidad['state'] = tk.NORMAL
            entradaPrecio['state'] = tk.NORMAL
            entradaPrecioVP['state'] = tk.NORMAL
            entradaCategoria.focus()
            botonGuardar.config(state=NORMAL)
    #GUARDADO DE PRODUCTO#################
    def guardarProducto():
        varCodigo=entradaCodigo.get()
        print(varCodigo)
        varCategoria=entradaCategoria.get()
        print(varCategoria)
        varDescripcion=entradaDescripcion.get()
        print(varDescripcion)
        try:
            varCantidad=int(entradaCantidad.get())
            print(varCantidad)
        except:
            print('la cantidad debe ser un numero')
            entradaCantidad.delete(0, tk.END)
        try:
            varPrecioUnit=float(entradaPrecio.get())
            print(varPrecioUnit)
        except:
            print('el Precio debe ser un numero')
            entradaPrecio.delete(0, tk.END)
        try:
            varPrecioVPublico=float(entradaPrecioVP.get())
            print(varPrecioVPublico)
        except:
            print('el PVP debe ser un numero')
            entradaPrecioVP.delete(0, tk.END)
        ###CONEXION Y EJECUCION DE INSTRUCCION SQLITE#########################    
        mi_conexion= sqlite3.connect("basededatosPrueba.db")  
        cursor=mi_conexion.cursor() 
        instruccion= f"INSERT INTO stockFerreteria VALUES({varCodigo},'{varCategoria.upper()}','{varDescripcion.upper()}', {varCantidad}, {varPrecioUnit:.2f},{varPrecioVPublico:.2f})"
        cursor.execute(instruccion)
        instruccion=f"SELECT * FROM stockFerreteria WHERE codigo='{varCodigo}'"
        cursor.execute(instruccion)
        datos=cursor.fetchall()
        mi_conexion.commit()
        mi_conexion.close()
        limpiarEntry()
        entradaCategoria['state'] = tk.DISABLED
        entradaDescripcion['state'] = tk.DISABLED
        entradaCantidad['state'] = tk.DISABLED
        entradaPrecio['state'] = tk.DISABLED
        entradaPrecioVP['state'] = tk.DISABLED
        messagebox.showinfo( "",f"El PRODUCTO SE INGRESO CORRECTAMENTE")
        botonGuardar.config(state=DISABLED)
        #mostrarGuardar(ver=False)
        entradaCodigo.focus()
        ventana.lift()#TRAE AL FRENTE LA VENTANA DE ALTA DESPUES DEL SHOWWARNING

    #BOTONES####################################################################################################################################################
    botonAltaCodigo=Button(ventana, font=("Arial",9,'bold'), fg="black",border= 2,width=25,height=2  ,text='ALTA CODIGO', command=validarCodigo)
    botonAltaCodigo.place(x=190,y=12)
    botonGuardar=Button(ventana,state=DISABLED ,font=("Arial",9,'bold'), fg="black",border= 2,width=25,height=3,background="light green" ,text='GUARDAR', command=guardarProducto)
    botonGuardar.place(x=230,y=170)
    #mostrarGuardar(False)
    

    #ENTRY#############################################################################################
    entradaCodigo=Entry(ventana,font=("Arial",10),width=7 ,justify="right",textvariable=codigoBusq)
    entradaCodigo.place(x=110,y=25)
    entradaCodigo.focus()

    ###
    entradaCategoria=Entry(ventana,font=("Arial",10),width=12, textvariable=itemTabla)
    entradaCategoria.place(x=110,y=90)
    entradaCategoria['state'] = tk.DISABLED
    ###
    entradaDescripcion=Entry(ventana,font=("Arial",10),width=40, textvariable=itemTabla)
    entradaDescripcion.place(x=110,y=120)
    entradaDescripcion['state'] = tk.DISABLED
    ##
    entradaCantidad=Entry(ventana,font=("Arial",10),width=5,justify="right",textvariable=itemTabla)
    entradaCantidad.place(x=110,y=150)
    entradaCantidad['state'] = tk.DISABLED
    ##
    entradaPrecio=Entry(ventana,font=("Arial",10),width=10,justify="right", textvariable=itemTabla)
    entradaPrecio.place(x=110,y=180)
    entradaPrecio['state'] = tk.DISABLED
    ##
    entradaPrecioVP=Entry(ventana,font=("Arial",10),width=10,justify="right",textvariable=itemTabla)
    entradaPrecioVP.place(x=110,y=210)
    entradaPrecioVP['state'] = tk.DISABLED
    
    #ETIQUETAS#####################################################################################
    lbl2=Label(ventana, text='CODIGO:')
    lbl2.place(x=10,y=25)
    lbl3=Label(ventana, text='CATEGORIA:')
    lbl3.place(x=10,y=90)
    lbl4=Label(ventana, text='DESCRIPCION:')
    lbl4.place(x=10,y=120)
    lbl5=Label(ventana, text='CANTIDAD:')
    lbl5.place(x=10,y=150)
    lbl6=Label(ventana, text='PRECIO COSTO:')
    lbl6.place(x=10,y=180)
    lbl7=Label(ventana, text='PRECIO VP:')
    lbl7.place(x=10,y=210)


    mainloop()
#oduloCarga()