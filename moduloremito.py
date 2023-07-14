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
ventana=tk.Tk()
ventana.geometry("720x700+10+10")#TAMAÑO Y UBICACION CON RESPECTO A LA PANTALLA                                                    
ventana.title("GENERACION DE REMITOS")#TITULO
ventana.resizable(width=False,height=False)#BLOQUEO DE REDIMENSION
ventana.configure(background="lightblue")#COLOR DE FONDO DE VENTANA
ventana.bind('<F1>', lambda event: activarValorizar())
ventana.bind('<F2>', lambda event: activarCargaLPrecios())
fuenteNegrita = Font(weight="bold")
spinbox = ttk.Spinbox()
#CREACION DE UN MARCO#########################################
cuadro1=tk.Frame(ventana,width=400,height=150,borderwidth=1,
        highlightthickness=1,
        highlightbackground="lightblue",
        bg='lightblue',padx=1,pady=1)
##Crear una fuente con negrita#################################
fuenteNegrita = Font(weight="bold")

cuadro1=Frame(ventana,width=500,height=480)

############################################################################################
##FUNCION DE FORMATO DECIMAL Y SEPARADOR DE MILES
def formatoDecimal(value): 
    return "{:,.2f}".format(value)  # Formato con 2 decimales y separadores de miles
##FUNCION DE LISTADO DE PRODUCTOS###########################################################
def mostarTabla():
    tablaFerreteria.delete(*tablaFerreteria.get_children())#borra el contenido de la tabla
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

###FUNCION DE BORRADO DE PRODUCTO D REMITO###########################################################################
def borrarProductoRemito():
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
        nuevoRango=valor[2]
        #print(valor[2])
        #print valor
        spinbox.configure(to=nuevoRango)
        spinbox.place(x=420,y=108) 
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
####################################################################################################################
varTotal=0
###FUNCION PARA INSERTAR EN TABLA REMITO############################################################################
def insertarTablaRemito():
    #####ASIGNACION DE VALORES A LAS VARIABLES
    global varTotal
    varCodigo=int(entradaCodigo.get())
    varCategoria=entradaCategoria.get()
    varDescripcion=entradaDescripcion.get()
    varCantidad=(spinbox.get())
    varPrecioUnit=float(entradaPrecio.get())
    varPrecioVPublico=float(entradaPrecioVP.get())
    #print (f"el varlor es:{varCantidad}")
    varSubtotal=(float(varCantidad)*varPrecioVPublico)
    tablaRemito.insert("",0,text=varCodigo, values=(varCategoria,varDescripcion,varCantidad,formatoDecimal(varPrecioUnit),formatoDecimal(varPrecioVPublico),formatoDecimal(varSubtotal)))
    varTotal=varSubtotal+varTotal
    print(varTotal)
    lblValorTotal.config(text=(f"TOTAL STOCK CARGADO: ${varTotal:,.2f}-"),font=fuenteNegrita)   
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
        nuevoRango=valoresSelec[2]
        #print(valoresSelec[2])
        #print (f"el valor para spinbox es: {nuevoRango}") #impresion de ayuda
        spinbox.configure(to=nuevoRango)
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
    
##FUNCION DE IMPRESION DE CONTENIDO DE TABLA#####################################################
def contenidoTablaRemito():
    valorTotal=0
    for item_id in tablaRemito.get_children():
    # Obtener los valores del elemento
        valores = tablaRemito.item(item_id)["values"]
        codigos=  tablaRemito.item(item_id)["text"]
        valores.insert(0,codigos)
        valorSubtotal=valores[6].replace(',','')
        valorTotal= (float(valorSubtotal))+(float(valorTotal))
        print(valores)#impresion con el codigo en el indice 0
    print (valorTotal)
    
    
    
##################################################################################################   
#INICIALIZACION DE VARIABLES######################################################################
codigoBusq=int()
descripcionBusq=()
itemTabla=()
sumaStock=()
spinCant= 0
##SPINBOX##########################################################################################
spinbox = ttk.Spinbox(ventana, from_=0, to=spinCant, increment=1, width=5)
spinbox.place(x=420,y=108)    

#ENTRY#############################################################################################
varUbicacion=ventana
entradaCodigo=ttk.Entry(varUbicacion,font=("Arial",10),width=7 ,justify="right",textvariable=codigoBusq)
entradaCodigo.place(x=65,y=48)
entradaCategoria=ttk.Entry(varUbicacion,font=("Arial",10),width=12, textvariable=itemTabla)
entradaCategoria.place(x=200,y=48)
entradaDescripcion=ttk.Entry(varUbicacion,font=("Arial",10),width=50, textvariable=itemTabla)
entradaDescripcion.place(x=100,y=78)
entradaCantidad=ttk.Entry(varUbicacion,font=("Arial",10),width=5,justify="right",textvariable=itemTabla)
entradaCantidad.place(x=420,y=48)
entradaPrecio=ttk.Entry(varUbicacion,font=("Arial",10),width=10,justify="right", textvariable=itemTabla)
entradaPrecio.place(x=110,y=108)
entradaPrecioVP=ttk.Entry(varUbicacion,font=("Arial",10),width=10,justify="right",textvariable=itemTabla)
entradaPrecioVP.place(x=290,y=108)
#ETIQUETAS#####################################################################################
lbl1=ttk.Label(ventana, text='VALOR DE STOCK CARGADO EN REMITO:',background='lightblue')
lbl1.place(x=10,y=10)
lbl10=ttk.Label(ventana, text='____________',background='lightblue')
lbl10.place(x=240,y=8)
########################################################
lblCodigo=ttk.Label(ventana, text='CODIGO:',background='lightblue')
lblCodigo.place(x=10,y=50)
lblCategoria=ttk.Label(ventana, text='CATEGORIA:',background='lightblue')
lblCategoria.place(x=125,y=50)
lblDescripcion=ttk.Label(ventana, text='DESCRIPCION:',background='lightblue')
lblDescripcion.place(x=10,y=80)
lblCantidad=ttk.Label(ventana, text='STOCK DSIPONIBLE:',background='lightblue')
lblCantidad.place(x=300,y=50)
lblPrecio=ttk.Label(ventana, text='PRECIO COSTO:',background='lightblue')
lblPrecio.place(x=10,y=110)
lblPrecioVP=ttk.Label(ventana, text='PRECIO VP:',background='lightblue')
lblPrecioVP.place(x=220,y=110)
lblValorTotal=ttk.Label(ventana, text=(f"TOTAL STOCK CARGADO: ${varTotal}-"),font=fuenteNegrita,background='lightblue')
lblValorTotal.place(x=400,y=670)
#FUNCION PARA ASIGNAR TECLA F A UN BOTON
def activarValorizar():
    btn1.invoke()
def activarCargaLPrecios():
    btn4.invoke()
#BOTONES#########################################################################################
style= ttk.Style()
style.configure("EstiloBotonRemito1.TButton", background="red", foreground="black", font=("Arial", 10, "bold"))
style.configure("EstiloBotonRemito2.TButton", background="blue", foreground="black", font=("Arial", 10, "bold"))

btn1=ttk.Button(ventana,text='INSERTAR',command=insertarTablaRemito,style='EstiloBotonRemito1.TButton',width=25)
btn1.place(x=540,y=145)
#######################################
btn2=ttk.Button(ventana,  text='BUSCAR CODIGO', command=busquedaCodigo,style='EstiloBotonRemito2.TButton',width=25)
btn2.place(x=540,y=90)
#######################################
btn3=ttk.Button(ventana, text='BUSCAR DESCRIPCION', command=busquedaDescripcion,style='EstiloBotonRemito2.TButton',width=25)
btn3.place(x=540,y=50)
#######################################
btn4=ttk.Button(ventana,  text='F2-CARGAR LISTA DE PRECIOS', command=mostarTabla,style='EstiloBotonRemito2.TButton')
btn4.place(x=300,y=145)
# #mostrarModificar(False)
#######################################
btn7=ttk.Button(ventana ,text='BAJA PRODUCTO', command=borrarProductoRemito,style='EstiloBotonRemito2.TButton')
btn7.place(x=10,y=145)
#######################################
btn8=ttk.Button(ventana,  text='LIMPIAR ENTRADA', command=limpiarEntry,style='EstiloBotonRemito2.TButton')
btn8.place(x=150,y=145)
#######################################
btn10=ttk.Button(ventana, text='TEST', command=contenidoTablaRemito,style='EstiloBotonRemito2.TButton',width=25)
btn10.place(x=540,y=10)
################################################################################

################################################################################
###TREE VIEW- TABLA#############################################################
style.theme_use('clam')#ASIGANCION DE THEMAS- CLAM, DEFAULT, ALT, AQUA, STEP, CLASSIC
tablaFerreteria=ttk.Treeview(height=20,
                             show='tree headings',
                             columns=('#0', '#1','#2','#3','#4'))
style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white"
                )
tablaFerreteria=ttk.Treeview(height=20,show='tree headings',columns=('#0', '#1','#2','#3','#4'))
tablaFerreteria.place(x=10,y=190,width=700,height=150)
tablaFerreteria.column('#0', width=20,anchor='e')
tablaFerreteria.heading('#0',text="CODIGO",anchor='center',)
tablaFerreteria.column('#1', width=40)
tablaFerreteria.heading('#1',text="CATEGORIA",anchor="center")
tablaFerreteria.column('#2', width=250)
tablaFerreteria.heading('#2',text="DESCRIPCION",anchor="center")
tablaFerreteria.column('#3', width=20,anchor='e')
tablaFerreteria.heading('#3',text="STOCK",anchor="center")
tablaFerreteria.column('#4', width=20,anchor='e')
tablaFerreteria.heading('#4',text="PRECIO",anchor="center")
tablaFerreteria.column('#5', width=20,anchor='e')
tablaFerreteria.heading('#5',text="PVP",anchor='center')
tablaFerreteria.bind("<ButtonRelease-1>", imprimirSeleccion)
tablaFerreteria.bind("<<TreeviewSelect>>", capturaSeleccion)

################################################################################
###TREE VIEW- TABLA#############################################################
tablaRemito=ttk.Treeview(height=20,show='tree headings',columns=('#0', '#1','#2','#3','#4','#5'))
tablaRemito.place(x=10,y=360,width=700,height=300)
tablaRemito.column('#0', width=10,anchor='e')
tablaRemito.heading('#0',text="CODIGO",anchor='center',)
tablaRemito.column('#1', width=40)
tablaRemito.heading('#1',text="CATEGORIA",anchor="center")
tablaRemito.column('#2', width=230)
tablaRemito.heading('#2',text="DESCRIPCION",anchor="center")
tablaRemito.column('#3', width=8,anchor='e')
tablaRemito.heading('#3',text="CANT.",anchor="center")
tablaRemito.column('#4', width=10,anchor='e')
tablaRemito.heading('#4',text="PRECIO",anchor="center")
tablaRemito.column('#5', width=10,anchor='e')
tablaRemito.heading('#5',text="PVP",anchor='center')
tablaRemito.column('#6', width=10,anchor='e')
tablaRemito.heading('#6',text="SUBTOTAL",anchor='center')
tablaRemito.bind("<ButtonRelease-1>", imprimirSeleccion)
tablaRemito.bind("<<TreeviewSelect>>", capturaSeleccion)

mostarTabla()
ventana.mainloop()