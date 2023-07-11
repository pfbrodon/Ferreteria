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
#CONFIGURACION INICIAL VENTANA PRINCIPAL
ventana=Tk()
ventana.geometry("720x780")                                                    
ventana.title("GENERACION DE REMITOS")
ventana.bind('<F1>', lambda event: activarValorizar())
ventana.bind('<F2>', lambda event: activarCargaLPrecios())

#CREACION DE UN MARCO#########################################
cuadro1=Frame(ventana,width=300,height=100,highlightthickness=2)
cuadro1.place(x=200,y=180)

##Crear una fuente con negrita#################################
fuenteNegrita = Font(weight="bold")

cuadro1=Frame(ventana,width=500,height=400)

##FUNCION DE FORMATO DECIMAL Y SEPARADOR DE MILES
def formatoDecimal(value): 
    return "{:,.2f}".format(value)  # Formato con 2 decimales y separadores de miles
##FUNCION DE LISTADO DE PRODUCTOS###########################################################
def mostarTabla():
    tablaFerreteria.delete(*tablaRemito.get_children())#borra el contenido de la tabla
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablaFerreteria.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],formatoDecimal(columna[4]),formatoDecimal(columna[5])))
    limpiarEntry()
def mostarTablaRemito():
    tablaFerreteria.delete(*tablaRemito.get_children())#borra el contenido de la tabla
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablaFerreteria.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],formatoDecimal(columna[4]),formatoDecimal(columna[5])))
    limpiarEntry()

##FUNCIONES DE BUSQUEDA DE PRODUCTOS################################################################
def busquedaCodigo():#POR CODIGO
    tablaFerreteria.delete(*tablaFerreteria.get_children())#borra el contenido de la tabla
    codigoBusq=entradaCodigo.get()
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria WHERE codigo like '{codigoBusq}'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablaFerreteria.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],formatoDecimal(columna[4]),formatoDecimal(columna[5])))
        print(datos)
def busquedaDescripcion():#POR DESCRIPCION
    tablaFerreteria.delete(*tablaFerreteria.get_children())#borra el contenido de la tabla treeview
    codigoBusq=entradaDescripcion.get()
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria WHERE descripcion like '%{codigoBusq}%'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablaFerreteria.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],formatoDecimal(columna[4]),formatoDecimal(columna[5])))

###FUNCION DE BORRADO DE PRODUCTO############################################################################
def borrarProducto():
    varCodigo=int(entradaCodigo.get())
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"DELETE FROM  stockFerreteria WHERE codigo='{varCodigo}'"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    limpiarEntry()
    
#FUNCION DE SELECCION MOUSE#################################################################################
def imprimirSeleccion(event):
    seleccion=tablaFerreteria.selection()
    #print(seleccion)
    for item in seleccion:
        valor=tablaFerreteria.item(item)["values"]
        #print("CODIGO:", tablaFerreteria.item(item)["text"])   #IMPRESION DE AYUDA
        #print(valor)                                        #IMPRESION DE AYUDA
        entradaCategoria.delete(0, tk.END)  # Limpiar el contenido previo
        entradaCategoria.insert(0,valor[0])
        entradaDescripcion.delete(0, tk.END)  # Limpiar el contenido previo
        entradaDescripcion.insert(0,valor[1])
        entradaCantidad.delete(0, tk.END)  # Limpiar el contenido previo
        entradaCantidad.insert(0,valor[2])
        #########################################
        #print (valor[3])#impresion de ayuda
        digitosPrecio= (valor[3]).replace(',','')
        entradaPrecio.delete(0, tk.END)  # Limpiar el contenido previo
        entradaPrecio.insert(0,digitosPrecio)
        #####################################
        #print (valor[4])#impresion de ayuda
        digitosPVP= (valor[4]).replace(',','')
        entradaPrecioVP.delete(0, tk.END)  # Limpiar el contenido previo
        entradaPrecioVP.insert(0,digitosPVP)
        ######################################
        entradaCodigo.delete(0, tk.END)  # Limpiar el contenido previo
        entradaCodigo.insert(0,tablaFerreteria.item(item)["text"])
        #mostrarModificar(ver=True)
###FUNCION PARA INSERTAR EN TABLA REMITO############################################################################
def insertarTablaRemito():
    #tablaFerreteria.delete(*tablaFerreteria.get_children())#borra el contenido de la tabla
    #####ASIGNACION DE VALORES A LAS VARIABLES
    varCodigo=int(entradaCodigo.get())
    varCategoria=entradaCategoria.get()
    varDescripcion=entradaDescripcion.get()
    varCantidad=int(entradaCantidad.get())
    varPrecioUnit=float(entradaPrecio.get())
    varPrecioVPublico=float(entradaPrecioVP.get()) 
    tablaRemito.insert("",0,text=varCodigo, values=(varCategoria,varDescripcion,varCantidad,formatoDecimal(varPrecioUnit),formatoDecimal(varPrecioVPublico)))
    limpiarEntry()
    mostarTabla()
       
## Función que se ejecuta cuando cambia la selección en el TreeView#################################
def capturaSeleccion(event):
    seleccion = tablaFerreteria.focus()  # Obtener el elemento seleccionado
    for item in seleccion:
        valoresSelec = tablaFerreteria.item(seleccion)['values']  # Obtener los valores del elemento seleccionado
        entradaCategoria.delete(0, tk.END)  # Limpiar el contenido previo
        entradaCategoria.insert(0,valoresSelec[0])
        entradaDescripcion.delete(0, tk.END)  # Limpiar el contenido previo
        entradaDescripcion.insert(0,valoresSelec[1])
        entradaCantidad.delete(0, tk.END)  # Limpiar el contenido previo
        entradaCantidad.insert(0,valoresSelec[2])
        #########################################
        #print (valoresSelec[3])#impresion de ayuda
        digitosPrecio= (valoresSelec[3]).replace(',','')
        entradaPrecio.delete(0, tk.END)  # Limpiar el contenido previo
        entradaPrecio.insert(0,digitosPrecio)
        #####################################
        #print (valoresSelec[4])#impresion de ayuda
        digitosPVP= (valoresSelec[4]).replace(',','')
        entradaPrecioVP.delete(0, tk.END)  # Limpiar el contenido previo
        entradaPrecioVP.insert(0,digitosPVP)
        ######################################
        entradaCodigo.delete(0, tk.END)  # Limpiar el contenido previo
        entradaCodigo.insert(0,tablaFerreteria.item(seleccion)["text"])
        
##FUNCION DE LIMPIEZA DE ENTRY####################################################################
def limpiarEntry():
    entradaCodigo.delete(0, tk.END)
    entradaCategoria.delete(0, tk.END)
    entradaDescripcion.delete(0, tk.END)
    entradaCantidad.delete(0, tk.END)
    entradaPrecio.delete(0, tk.END)
    entradaPrecioVP.delete(0, tk.END)
    
    
################################################################################ 
##FUNCION PARA VALORIZAR EL TOTAL DEL STOCK#####################################
def valorizarStock():
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    sumaStock=0
    for valor in datos:
        (codigo, categoria ,descripcion, cantidad, preciounit, precioVPublico)=valor
        producto=cantidad*preciounit
        sumaStock=producto+sumaStock
        #print(producto)
    print(f"El valor acumulado de todo su Stock es de: ${sumaStock:,.2f} ")##IMPRESION EN CONSOLA PARA REFERNCIA
    lbl10.config(text=f'$ {sumaStock:,}.-', font=fuenteNegrita)
    return sumaStock
##################################################################################################   
#INICIALIZACION DE VARIABLES######################################################################
codigoBusq=int()
descripcionBusq=()
itemTabla=()
sumaStock=()
#ENTRY#############################################################################################
entradaCodigo=ttk.Entry(ventana,font=("Arial",10),width=7 ,justify="right",textvariable=codigoBusq)
entradaCodigo.place(x=110,y=50)
entradaCategoria=ttk.Entry(ventana,font=("Arial",10),width=12, textvariable=itemTabla)
entradaCategoria.place(x=110,y=80)
entradaDescripcion=ttk.Entry(ventana,font=("Arial",10),width=40, textvariable=itemTabla)
entradaDescripcion.place(x=110,y=110)
entradaCantidad=ttk.Entry(ventana,font=("Arial",10),width=5,justify="right",textvariable=itemTabla)
entradaCantidad.place(x=110,y=140)
entradaPrecio=ttk.Entry(ventana,font=("Arial",10),width=10,justify="right", textvariable=itemTabla)
entradaPrecio.place(x=110,y=170)
entradaPrecioVP=ttk.Entry(ventana,font=("Arial",10),width=10,justify="right",textvariable=itemTabla)
entradaPrecioVP.place(x=110,y=200)
#ETIQUETAS#####################################################################################
lbl1=Label(ventana, text='VALOR DE STOCK EXISTENTE:')
lbl1.place(x=10,y=10)
lbl10=Label(ventana, text='')
lbl10.place(x=168,y=8)
########################################################
lblCodigo=ttk.Label(ventana, text='CODIGO:')
lblCodigo.place(x=10,y=50)
lblCategoria=Label(ventana, text='CATEGORIA:')
lblCategoria.place(x=10,y=80)
lblDescripcion=Label(ventana, text='DESCRIPCION:')
lblDescripcion.place(x=10,y=110)
lblCantidad=Label(ventana, text='CANTIDAD:')
lblCantidad.place(x=10,y=140)
lblPrecio=Label(ventana, text='PRECIO COSTO:')
lblPrecio.place(x=10,y=170)
lblPrecioVP=Label(ventana, text='PRECIO VP:')
lblPrecioVP.place(x=10,y=200)
#FUNCION PARA ASIGNAR TECLA F A UN BOTON
def activarValorizar():
    btn1.invoke()
def activarCargaLPrecios():
    btn4.invoke()
#BOTONES#########################################################################################
style= ttk.Style()
style.configure("EstiloBoton1.TButton", background="red", foreground="black", font=("Arial", 12, "bold"))
style.configure("EstiloBoton2.TButton", background="blue", foreground="black", font=("Arial", 12, "bold"))

btn1=ttk.Button(ventana,text='INSERTAR',command=insertarTablaRemito,style='EstiloBoton1.TButton')
btn1.place(x=520,y=10)
#######################################
btn2=ttk.Button(ventana,  text='BUSCAR CODIGO', command=busquedaCodigo,style='EstiloBoton2.TButton')
btn2.place(x=520,y=90)
#######################################
btn3=ttk.Button(ventana, text='BUSCAR DESCRIPCION', command=busquedaDescripcion)
btn3.place(x=520,y=50)
#######################################
btn4=ttk.Button(ventana,  text='F2-CARGAR LISTA DE PRECIOS', command=mostarTabla)
btn4.place(x=520,y=170)
# #mostrarModificar(False)
#######################################
btn7=ttk.Button(ventana ,text='BAJA PRODUCTO', command=borrarProducto)
btn7.place(x=320,y=210)
#######################################
btn8=ttk.Button(ventana,  text='LIMPIAR ENTRADA', command=limpiarEntry)
btn8.place(x=520,y=210)
#######################################
#btn10=Button(ventana, font=("Arial",9), fg="black",border= 3,width=25,  text='TEST', command=print('SIN FUNCION'))
#btn10.place(x=520,y=210)
################################################################################

################################################################################
###TREE VIEW- TABLA#############################################################
tablaFerreteria=ttk.Treeview(height=20,show='tree headings',columns=('#0', '#1','#2','#3','#4'))
tablaFerreteria.place(x=10,y=250,width=700,height=150)
tablaFerreteria.column('#0', width=20,anchor='e')
tablaFerreteria.heading('#0',text="CODIGO",anchor='center',)
tablaFerreteria.column('#1', width=40)
tablaFerreteria.heading('#1',text="CATEGORIA",anchor="center")
tablaFerreteria.column('#2', width=250)
tablaFerreteria.heading('#2',text="DESCRIPCION",anchor="center")
tablaFerreteria.column('#3', width=20,anchor='e')
tablaFerreteria.heading('#3',text="CANTIDAD",anchor="center")
tablaFerreteria.column('#4', width=20,anchor='e')
tablaFerreteria.heading('#4',text="PRECIO",anchor="center")
tablaFerreteria.column('#5', width=20,anchor='e')
tablaFerreteria.heading('#5',text="PVP",anchor='center')
tablaFerreteria.bind("<ButtonRelease-1>", imprimirSeleccion)
tablaFerreteria.bind("<<TreeviewSelect>>", capturaSeleccion)

################################################################################
###TREE VIEW- TABLA#############################################################
tablaRemito=ttk.Treeview(height=20,show='tree headings',columns=('#0', '#1','#2','#3','#4'))
tablaRemito.place(x=10,y=400,width=700,height=250)
tablaRemito.column('#0', width=20,anchor='e')
tablaRemito.heading('#0',text="CODIGO",anchor='center',)
tablaRemito.column('#1', width=40)
tablaRemito.heading('#1',text="CATEGORIA",anchor="center")
tablaRemito.column('#2', width=250)
tablaRemito.heading('#2',text="DESCRIPCION",anchor="center")
tablaRemito.column('#3', width=20,anchor='e')
tablaRemito.heading('#3',text="CANTIDAD",anchor="center")
tablaRemito.column('#4', width=20,anchor='e')
tablaRemito.heading('#4',text="PRECIO",anchor="center")
tablaRemito.column('#5', width=20,anchor='e')
tablaRemito.heading('#5',text="PVP",anchor='center')
tablaRemito.bind("<ButtonRelease-1>", imprimirSeleccion)
tablaRemito.bind("<<TreeviewSelect>>", capturaSeleccion)


ventana.mainloop()