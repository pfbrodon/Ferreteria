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
    ventana.geometry("450x250+40+40")                                                    
    ventana.title("CARGA DE PRODUCTOS")
    ventana.resizable(width=False,height=False)#BLOQUEO DE REDIMENSION
    ventana.configure(background="lightblue")#COLOR DE FONDO DE VENTANA
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
    ####DEFINIR ESTILOS DE BOTONES###################################################################
    style= ttk.Style()
    style.configure("EstiloBoton1Carga.TButton", background="grey", foreground="black", font=("Arial", 10, "bold"))
    style.configure("EstiloBoton2Carga.TButton", background="red", foreground="black", font=("Arial", 10, "bold"))
    style.configure("EstiloBoton3Carga.TButton", background="blue", foreground="black", font=("Arial", 10, "bold"))
    style.configure("EstiloBoton4Carga.TButton", background="green", foreground="black", font=("Arial", 11, "bold"))
    style.configure("EstiloBoton5Carga.TButton", background="yellow", foreground="black", font=("Arial", 10, "bold"))

    #BOTONES####################################################################################################################################################
    botonAltaCodigo=ttk.Button(ventana,text='ALTA CODIGO', command=validarCodigo,style="EstiloBoton3Carga.TButton",width=25)
    botonAltaCodigo.place(x=230,y=23)
    botonGuardar=ttk.Button(ventana,state=DISABLED,text='GUARDAR', command=guardarProducto,style="EstiloBoton4Carga.TButton",width=25)
    botonGuardar.place(x=220,y=180)
    #mostrarGuardar(False)
    

    #ENTRY#############################################################################################
    entradaCodigo=ttk.Entry(ventana,font=("Arial",10),width=7 ,justify="right",textvariable=codigoBusq)
    entradaCodigo.place(x=110,y=25)
    entradaCodigo.focus()

    ###
    entradaCategoria=ttk.Entry(ventana,font=("Arial",10),width=12, textvariable=itemTabla)
    entradaCategoria.place(x=110,y=90)
    entradaCategoria['state'] = tk.DISABLED
    ###
    entradaDescripcion=ttk.Entry(ventana,font=("Arial",10),width=40, textvariable=itemTabla)
    entradaDescripcion.place(x=110,y=120)
    entradaDescripcion['state'] = tk.DISABLED
    ##
    entradaCantidad=ttk.Entry(ventana,font=("Arial",10),width=5,justify="right",textvariable=itemTabla)
    entradaCantidad.place(x=110,y=150)
    entradaCantidad['state'] = tk.DISABLED
    ##
    entradaPrecio=ttk.Entry(ventana,font=("Arial",10),width=10,justify="right", textvariable=itemTabla)
    entradaPrecio.place(x=110,y=180)
    entradaPrecio['state'] = tk.DISABLED
    ##
    entradaPrecioVP=ttk.Entry(ventana,font=("Arial",10),width=10,justify="right",textvariable=itemTabla)
    entradaPrecioVP.place(x=110,y=210)
    entradaPrecioVP['state'] = tk.DISABLED
    
    #ETIQUETAS#####################################################################################
    lbl2=ttk.Label(ventana, text='CODIGO:',background='lightblue')
    lbl2.place(x=10,y=25)
    lbl3=ttk.Label(ventana, text='CATEGORIA:',background='lightblue')
    lbl3.place(x=10,y=90)
    lbl4=ttk.Label(ventana, text='DESCRIPCION:',background='lightblue')
    lbl4.place(x=10,y=120)
    lbl5=ttk.Label(ventana, text='CANTIDAD:',background='lightblue')
    lbl5.place(x=10,y=150)
    lbl6=ttk.Label(ventana, text='PRECIO COSTO:',background='lightblue')
    lbl6.place(x=10,y=180)
    lbl7=ttk.Label(ventana, text='PRECIO VP:',background='lightblue')
    lbl7.place(x=10,y=210)


    mainloop()
#moduloCarga()