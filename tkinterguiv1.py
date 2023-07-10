import sqlite3 
import tkinter as tk
# from tkinter import *
from tkinter import Menu,ttk
from tkinter import Tk, Label, Button, Entry, messagebox
import os
##CORRECCION DE RUTA DE ARCHIVOS#########################################
##########################################################################
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
###########################################################################
ventana=Tk()
ventana.geometry("1024x680")                                                    
ventana.title("Prueba Carga de Datos en SQLite")

##FUNCION DE FORMATO DECIMAL 
def format_decimal(value):
    return "{:.2f}".format(value)  # Formato con 2 decimales

# Habilita la baja o la modif de un producto mostrado
mostrarBotones = False
def mostrarAcciones(ver):
    print("Mostrar",ver)
    if ver:
        btnModificar.place(x=370,y=210)
    else:
        btnModificar.place_forget()

##FUNCION DE LISTADO DE PRODUCTOS
def mostarTabla():
    tablavagones.delete(*tablavagones.get_children())#borra el contenido de la tabla
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    #instruccion= f"SELECT * FROM stockFerreteria WHERE descripcion like '%{criterioBusq}%'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
    instruccion= f"SELECT * FROM stockFerreteria"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablavagones.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],format_decimal(columna[4]),format_decimal(columna[5])))


##FUNCIONES DE BUSQUEDA DE PRODUCTOS################################################################


def busquedaCodigo():
    tablavagones.delete(*tablavagones.get_children())#borra el contenido de la tabla
    codigoBusq=entrada2.get()
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria WHERE codigo like '{codigoBusq}'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablavagones.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],columna[4],columna[5]))
        print(datos)

def busquedaDescripcion():
    tablavagones.delete(*tablavagones.get_children())#borra el contenido de la tabla
    codigoBusq=entrada4.get()
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria WHERE descripcion like '%{codigoBusq}%'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablavagones.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],columna[4],columna[5]))
#FUNCION PARA INSERTAR PRODUCTOS############################################################################

def insertarProducto():          
    
    varCodigo=int(entrada2.get())
    varCategoria=entrada3.get()
    varDescripcion=entrada4.get()
    varCantidad=int(entrada5.get())
    varPrecioUnit=float(entrada6.get())
    varPrecioVPublico=float(entrada7.get())
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"INSERT INTO stockFerreteria VALUES({varCodigo},'{varCategoria.upper()}','{varDescripcion.upper()}', {varCantidad}, {varPrecioUnit:.2f},{varPrecioVPublico:.2f})"
    cursor.execute(instruccion)
    mi_conexion.commit()
    mi_conexion.close()
    mostarTabla()
    
###FUNCION PARA MODIFICAR PRODUCTO############################################################################
def modificarProducto():
    varCodigo=int(entrada2.get())
    varCategoria=entrada3.get()
    varDescripcion=entrada4.get()
    varCantidad=int(entrada5.get())
    varPrecioUnit=float(entrada6.get())
    varPrecioVPublico=float(entrada7.get())    
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"UPDATE stockFerreteria SET 'categoria' = '{varCategoria.upper()}', 'descripcion'='{varDescripcion.upper()}', 'cantidad'='{varCantidad}', 'precioUnit'='{varPrecioUnit:.2f}', 'precioVPublico'='{varPrecioVPublico}' WHERE codigo='{varCodigo}'"
    cursor.execute(instruccion)
    #instruccion= f"SELECT * FROM stockFerreteria WHERE codigo='{codigoProducto}'"
    #cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    limpiarEntry()
    mostarTabla()

###FUNCION DE BORRADO DE PRODUCTO############################################################################

def borrarProducto():
    varCodigo=int(entrada2.get())
    mi_conexion= sqlite3.connect("basededatosPrueba.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"DELETE FROM  stockFerreteria WHERE codigo='{varCodigo}'"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    limpiarEntry()
    mostarTabla()
    
#FUNCION DE SELECCION MOUSE#################################################################################

def imprimirSeleccion(event):
    seleccion=tablavagones.selection()
    print(">>>>",seleccion)
    for item in seleccion:
        print(item)
        valor=tablavagones.item(item)["values"]
        print(valor)
        #print("CODIGO:", tablavagones.item(item)["text"])   #IMPRESION DE AYUDA
        #print(valor)                                        #IMPRESION DE AYUDA
        entrada3.delete(0, tk.END)  # Limpiar el contenido previo
        entrada3.insert(0,valor[0])
        entrada4.delete(0, tk.END)  # Limpiar el contenido previo
        entrada4.insert(0,valor[1])
        entrada5.delete(0, tk.END)  # Limpiar el contenido previo
        entrada5.insert(0,valor[2])
        entrada6.delete(0, tk.END)  # Limpiar el contenido previo
        entrada6.insert(0,valor[3])
        entrada7.delete(0, tk.END)  # Limpiar el contenido previo
        entrada7.insert(0,valor[4])
        entrada2.delete(0, tk.END)  # Limpiar el contenido previo
        entrada2.insert(0,tablavagones.item(item)["text"])
        mostrarAcciones(ver=True)
        
##FUNCION DE LIMPIEZA DE ENTRY####################################################################
def limpiarEntry():
    entrada2.delete(0, tk.END)
    entrada3.delete(0, tk.END)
    entrada4.delete(0, tk.END)
    entrada5.delete(0, tk.END)
    entrada6.delete(0, tk.END)
    entrada7.delete(0, tk.END)
    mostrarAcciones(ver=False)

##################################################################################################   
#INICIALIZACION DE VARIABLES######################################################################
codigoBusq=int()
descripcionBusq=()
itemTabla=()

#ENTRY#############################################################################################
entrada2=Entry(ventana,font="Arial", width=10, textvariable=codigoBusq)
entrada2.place(x=100,y=60)
entrada3=Entry(ventana,font="Arial",width=12, textvariable=itemTabla)
entrada3.place(x=100,y=90)
entrada4=Entry(ventana,font="Arial",width=50, textvariable=itemTabla)
entrada4.place(x=100,y=120)
entrada5=Entry(ventana,font="Arial",width=8, textvariable=itemTabla)
entrada5.place(x=100,y=150)
entrada6=Entry(ventana,font="Arial",width=8, textvariable=itemTabla)
entrada6.place(x=100,y=180)
entrada7=Entry(ventana,font="Arial",width=8 ,textvariable=itemTabla)
entrada7.place(x=100,y=210)




#ETIQUETAS#####################################################################################

lbl2=Label(ventana, text='CODIGO:')
lbl2.place(x=10,y=60)
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

#BOTONES#########################################################################################

btn=Button(ventana, font="Arial", fg="black",background="light blue" ,border= 3,  text='BUSCAR CODIGO', command=busquedaCodigo)
btn.place(x=300,y=54)
btn=Button(ventana, font="Arial", fg="black",background="light blue",border= 3 ,text='BUSCAR DESCRIPCION', command=busquedaDescripcion)
btn.place(x=660,y=113)
btn=Button(ventana, font="Arial", fg="black",border= 3,  text='CARGAR LISTA DE PRECIOS', command=mostarTabla)
btn.place(x=700,y=170)

# Boton modificar
btnModificar=Button(ventana, font="Arial", fg="black",border= 3, background="light yellow" ,text='MODIFICAR PRODUCTO', command=modificarProducto)
mostrarAcciones(False)


btn=Button(ventana, font="Arial", fg="black",border= 3, background="light green" ,text='ALTA PRODUCTO', command=insertarProducto)
btn.place(x=585,y=210)

btn=Button(ventana, font="Arial", fg="black",border= 3, background="red"  ,text='BAJA PRODUCTO', command=borrarProducto)
btn.place(x=200,y=210)
btn=Button(ventana, font="Arial", fg="black",border= 3,  text='LIMPIAR ENTRADA', command=limpiarEntry)
btn.place(x=850,y=210)

###TREE VIEW- TABLA#############################################################
tablavagones=ttk.Treeview(height=20,columns=('#0', '#1','#2','#3','#4'))
tablavagones.place(x=10,y=250,width=1010,height=400)
tablavagones.column('#0', width=125,anchor='e')
tablavagones.heading('#0',text="CODIGO",anchor='w')
tablavagones.column('#1', width=125)
tablavagones.heading('#1',text="CATEGORIA",anchor="center")
tablavagones.column('#2', width=400)
tablavagones.heading('#2',text="DESCRIPCION",anchor="center")
tablavagones.column('#3', width=100,anchor='e')
tablavagones.heading('#3',text="CANTIDAD",anchor="center")
tablavagones.column('#4', width=100,anchor='e')
tablavagones.heading('#4',text="PRECIO",anchor="center")
tablavagones.column('#5', width=100,anchor='e')
tablavagones.heading('#5',text="PVP",anchor='center')
tablavagones.bind("<ButtonRelease-1>", imprimirSeleccion)
imprimirSeleccion(tk.Event)
#mostarTabla()

ventana.mainloop()