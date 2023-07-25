import sqlite3 
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from tkinter.font import Font
from tkinter.simpledialog import askstring
import customtkinter as ctk


##CORRECCION DE RUTA DE ARCHIVOS#########################################
##########################################################################
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
###########################################################################

#CONFIGURACION INICIAL VENTANARemito PRINCIPAL
ventanaRemito=tk.Tk()
ventanaRemito.geometry("730x700+10+10")#TAMAÑO Y UBICACION CON RESPECTO A LA PANTALLA                                                    
ventanaRemito.title("GENERACION DE REMITOS")#TITULO
ventanaRemito.resizable(width=False,height=False)#BLOQUEO DE REDIMENSION
ventanaRemito.configure(background="lightblue")#COLOR DE FONDO DE VENTANARemito
ventanaRemito.bind('<F1>', lambda event: activarValorizar())
ventanaRemito.bind('<F2>', lambda event: activarCargaLPrecios())
fuenteNegrita = Font(weight="bold")
spinbox = ttk.Spinbox()
#CREACION DE UN MARCO#########################################
cuadro1=tk.Frame(ventanaRemito,width=400,height=150,borderwidth=1,
        highlightthickness=1,
        highlightbackground="lightblue",
        bg='lightblue',padx=1,pady=1)
##Crear una fuente con negrita#################################
fuenteNegrita = Font(weight="bold")

cuadro1=Frame(ventanaRemito,width=500,height=480)

############################################################################################
##FUNCION DE FORMATO DECIMAL Y SEPARADOR DE MILES
def formatoDecimal(value): 
    return "{:,.2f}".format(value)  # Formato con 2 decimales y separadores de miles
##FUNCION DE LISTADO DE PRODUCTOS###########################################################
def mostarTabla():
    tablaFerreteria.delete(*tablaFerreteria.get_children())#borra el contenido de la tabla
    mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
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
    mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria WHERE codigo like '{codigoBusq}'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablaFerreteria.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],formatoDecimal(columna[4]),formatoDecimal(columna[5])))
        print(datos)
    entradaCategoria.delete(0, tk.END)  # Limpiar el contenido previo
    entradaCategoria.insert(0,columna[1])
    entradaDescripcion.delete(0, tk.END)  # Limpiar el contenido previo
    entradaDescripcion.insert(0,columna[2])
    entradaCantidad.delete(0, tk.END)  # Limpiar el contenido previo
    entradaCantidad.insert(0,columna[3])
    entradaPrecio.delete(0, tk.END)  # Limpiar el contenido previo
    entradaPrecio.insert(0,columna[4])
    entradaPrecioVP.delete(0, tk.END)  # Limpiar el contenido previo
    entradaPrecioVP.insert(0,columna[5])

def busquedaDescripcion():#POR DESCRIPCION
    tablaFerreteria.delete(*tablaFerreteria.get_children())#borra el contenido de la tabla treeview
    codigoBusq=entradaDescripcion.get()
    mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"SELECT * FROM stockFerreteria WHERE descripcion like '%{codigoBusq}%'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    for columna in datos:
        tablaFerreteria.insert("",0,text=columna[0], values=(columna[1],columna[2],columna[3],formatoDecimal(columna[4]),formatoDecimal(columna[5])))
    entradaCategoria.delete(0, tk.END)  # Limpiar el contenido previo
    entradaCategoria.insert(0,columna[1])
    entradaDescripcion.delete(0, tk.END)  # Limpiar el contenido previo
    entradaDescripcion.insert(0,columna[2])
    entradaCantidad.delete(0, tk.END)  # Limpiar el contenido previo
    entradaCantidad.insert(0,columna[3])
    entradaPrecio.delete(0, tk.END)  # Limpiar el contenido previo
    entradaPrecio.insert(0,columna[4])
    entradaPrecioVP.delete(0, tk.END)  # Limpiar el contenido previo
    entradaPrecioVP.insert(0,columna[5])
###FUNCION DE BORRADO DE PRODUCTO D REMITO###########################################################################
def borrarProductoRemito():
    varCodigo=int(entradaCodigo.get())
    mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
    cursor=mi_conexion.cursor() 
    instruccion= f"DELETE FROM  stockFerreteria WHERE codigo='{varCodigo}'"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    mi_conexion.commit()
    mi_conexion.close()
    limpiarEntry()
    
#FUNCION DE SELECCION DE MOUSE EN TABLA DE STOCK FERRETERIA#################################################################################
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
#FUNCION DE SELECCION DE MOUSE EN TABLA DE STOCK FERRETERIA#################################################################################
def seleccionMouseTablaRemito(event):
    seleccion=tablaRemito.selection()
    #print(seleccion)
    for item in seleccion:
        valor=tablaRemito.item(item)["values"]
        print("CODIGO:", tablaRemito.item(item)["text"])   #IMPRESION DE AYUDA
        print(valor)                                        #IMPRESION DE AYUDA
        print (valor[2])
        #########################################
        
####################################################################################################################
###FUNCION PARA INSERTAR EN TABLA REMITO############################################################################
def insertarTablaRemito():
    #####ASIGNACION DE VALORES A LAS VARIABLES
    varExisteProducto=False
    varCodigo=int(entradaCodigo.get())
    valoresRemito=tablaRemito.get_children()#lee todos los valores del treeview tablaRemito
    print(f'el valore del treeview al comienzo de la funciona: {valoresRemito}')
    if valoresRemito==():
        print("el treeview esta vacio")
        varCodigo=int(entradaCodigo.get())
        varCategoria=entradaCategoria.get()
        varDescripcion=entradaDescripcion.get()
        varCantidad=(spinbox.get())
        varPrecioUnit=float(entradaPrecio.get())
        varPrecioVPublico=float(entradaPrecioVP.get())
        varStock=int(entradaCantidad.get())
        #print (f"el varlor es:{varCantidad}")
        varSubtotal=(float(varCantidad)*varPrecioVPublico)
        tablaRemito.insert("",0,text=varCodigo, values=(varCategoria,varDescripcion,varCantidad,formatoDecimal(varPrecioUnit),formatoDecimal(varPrecioVPublico),formatoDecimal(varSubtotal)))
        #######resta de cantidad de productos###############################################
        stockDisminuido=varStock-(int(varCantidad))
        entradaCantidad.delete(0, tk.END)  # Limpiar el contenido previo
        entradaCantidad.insert(0,stockDisminuido)#actualiza el stock en la entrada
        ######DISMINUCION DE LA TABLA FERRETERIA############################################
        mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
        cursor=mi_conexion.cursor() 
        instruccion= f"UPDATE stockFerreteria SET  'cantidad'='{stockDisminuido}' WHERE codigo='{varCodigo}'"
        cursor.execute(instruccion)
        mi_conexion.commit()
        mi_conexion.close()
        ###########SELECCION DEL TREEVIEW FERRETERIA
        seleccion=tablaFerreteria.selection()
        if seleccion:
            valores=tablaFerreteria.item(seleccion)['values']
            indice=tablaFerreteria.item(seleccion)['text']
            nuevosValores=list(valores)
            #print(f'index para tablaferreteria{indice}')
            #print(f'nuevos valores para tablaferreteria{nuevosValores}')
            nuevosValores[2] = stockDisminuido
            tablaFerreteria.item(seleccion, values=nuevosValores)
        ####################################################################################
        #print(f"el estok restante es de: {stockDisminuido}")
        #print(varTotal)
        sumaSubTotales()

    else:
        print("el treeview tiene datos")
        varCantidad=(spinbox.get())
        #print('la cantidad es '+varCantidad)
        varCodigo=int(entradaCodigo.get())
        varPrecioVPublico=float(entradaPrecioVP.get())
        varStock=int(entradaCantidad.get())
        #valoresRemito=tablaRemito.get_children()#lee todos los valores del treeview tablaRemito
        for valorRemito in tablaRemito.get_children():#recorre los elementos text de la tablaRemito
            valorCodigoenRemito=tablaRemito.item(valorRemito,'text')
            valoresEnRemito=tablaRemito.item(valorRemito,'values')
            print(f'el dodigo a comparar es: {valorCodigoenRemito}\n')
            print(f'la cantidad en remito es: {valoresEnRemito[2]}\n')
            print(valorRemito)
            if valorCodigoenRemito==varCodigo:
                varExisteProducto=True
                print('hacemos una suma')
                break
        if varExisteProducto:
            cantIncremantada= (int(varCantidad))+(int(valoresEnRemito[2]))
            subTotalIncrementado=cantIncremantada*varPrecioVPublico
            print(cantIncremantada)
            nuevosValoresRemito=list(valoresEnRemito)
            print(nuevosValoresRemito)
            nuevosValoresRemito[2]=str(cantIncremantada)
            nuevosValoresRemito[5]=(formatoDecimal(subTotalIncrementado))
            print(nuevosValoresRemito)
            tablaRemito.item(valorRemito,values=nuevosValoresRemito)
            #######RESTA CANTIDAD DE PRODUCTOS DE LA ENTRADA###############################################
            stockDisminuido=varStock-(int(varCantidad))
            entradaCantidad.delete(0, tk.END)  # Limpiar el contenido previo
            entradaCantidad.insert(0,stockDisminuido)#actualiza el stock en la entrada
            ######DISMINUCION DE LA TABLA FERRETERIA############################################
            mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
            cursor=mi_conexion.cursor() 
            instruccion= f"UPDATE stockFerreteria SET  'cantidad'='{stockDisminuido}' WHERE codigo='{varCodigo}'"
            cursor.execute(instruccion)
            mi_conexion.commit()
            mi_conexion.close()
            ###########SELECCION DEL TREEVIEW FERRETERIA
            seleccion=tablaFerreteria.selection()
            if seleccion:
                valores=tablaFerreteria.item(seleccion)['values']
                indice=tablaFerreteria.item(seleccion)['text']
                nuevosValores=list(valores)
                #print(f'index para tablaferreteria{indice}')
                #print(f'nuevos valores para tablaferreteria{nuevosValores}')
                nuevosValores[2] = stockDisminuido
                tablaFerreteria.item(seleccion, values=nuevosValores)
                sumaSubTotales()
        else:
            print('insertamos un nuevo valor')
            varCodigo=int(entradaCodigo.get())
            varCategoria=entradaCategoria.get()
            varDescripcion=entradaDescripcion.get()
            varCantidad=(spinbox.get())
            varPrecioUnit=float(entradaPrecio.get())
            varPrecioVPublico=float(entradaPrecioVP.get())
            varStock=int(entradaCantidad.get())
            #print (f"el varlor es:{varCantidad}")
            varSubtotal=(float(varCantidad)*varPrecioVPublico)
            tablaRemito.insert("",0,text=varCodigo, values=(varCategoria,varDescripcion,varCantidad,formatoDecimal(varPrecioUnit),formatoDecimal(varPrecioVPublico),formatoDecimal(varSubtotal)))
            #######resta de cantidad de productos###############################################
            stockDisminuido=varStock-(int(varCantidad))
            entradaCantidad.delete(0, tk.END)  # Limpiar el contenido previo
            entradaCantidad.insert(0,stockDisminuido)#actualiza el stock en la entrada
            ######DISMINUCION DE LA TABLA FERRETERIA############################################
            mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
            cursor=mi_conexion.cursor() 
            instruccion= f"UPDATE stockFerreteria SET  'cantidad'='{stockDisminuido}' WHERE codigo='{varCodigo}'"
            cursor.execute(instruccion)
            mi_conexion.commit()
            mi_conexion.close()
            ###########SELECCION DEL TREEVIEW FERRETERIA
            seleccion=tablaFerreteria.selection()
            if seleccion:
                valores=tablaFerreteria.item(seleccion)['values']
                indice=tablaFerreteria.item(seleccion)['text']
                nuevosValores=list(valores)
                #print(f'index para tablaferreteria{indice}')
                #print(f'nuevos valores para tablaferreteria{nuevosValores}')
                nuevosValores[2] = stockDisminuido
                tablaFerreteria.item(seleccion, values=nuevosValores)
            ####################################################################################
            #print(f"el estok restante es de: {stockDisminuido}")
            #print(varTotal)
            sumaSubTotales()
            
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
def modiCantTablaRemito():
    seleccionDato= tablaRemito.focus()
    if seleccionDato:# Verifica que se haya seleccionado un elemento
        valores = (tablaRemito.item(seleccionDato)["values"])
        valorCodigo = (tablaRemito.item(seleccionDato)["text"])
        print (f'los valores para la seleccion a modificar son: {valores}')
        print (valorCodigo)
        selecElementoTablaFerreteria(valorCodigo)
        #tablaFerreteria.see(valorCodigo)
        # Solicitar al usuario ingresar el nuevo valor
        nuevoValorStock= askstring("Modificar valor", "Ingrese el nuevo valor", initialvalue=valores[2])
        if nuevoValorStock:
            # Actualizar el elemento en el Treeview con el nuevo valor
            tablaRemito.set(seleccionDato, column='#3', value=nuevoValorStock)
            valorEnTreeView=int(valores[2])
            nuevoValorStock=int(nuevoValorStock)
            print(f'valor del treeview {valorEnTreeView}')
            print(f'el nuevo valor en remito es {nuevoValorStock}')
            if nuevoValorStock>valorEnTreeView:
                valorDecremento=nuevoValorStock-valorEnTreeView
                print("REALIZAR UNA RESTA A LA TABLAFERRETERIA Y AL TREEVIEW FERRETERIA")
                valorActTabla=leerItemTabla(valorCodigo)-valorDecremento
                print (valorActTabla)
                actualizaTabla(valorActTabla,valorCodigo)#actualiza la tabla con el nuevo valor del treeview remito
                entradaCantidad.delete(0, tk.END)#borra el valor de la entrada stock
                entradaCantidad.insert(0,valorActTabla)#actualiza el valor de la entrada stock con el nuevo valor de la tabla
                ########selecElementoTablaFerreteria(valorCodigo)
                seleccionDatoFerreteria=tablaFerreteria.focus()
                tablaFerreteria.set(seleccionDatoFerreteria,column='#3' ,value=valorActTabla)
            elif nuevoValorStock<valorEnTreeView:
                print ("REALIZAR UNA SUMA EN LA TABLA FERRETERIA Y EN EL TREEVIEW FERRETERIA")
            elif nuevoValorStock==valorEnTreeView:
                print("no hacer nada")
                
                
def leerItemTabla(codigo):
            mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
            cursor=mi_conexion.cursor() 
            instruccion= f"SELECT * FROM stockFerreteria WHERE codigo='{codigo}'"##columna like '%variable%' busca un item en la columna que contenga el parametro de busqueda
            cursor.execute(instruccion)
            datos=cursor.fetchall()
            mi_conexion.commit()
            mi_conexion.close()
            #print (datos)
            for valorDato in datos:
                #print (valorDato[3])
                valor=valorDato[3]
                return valor
def actualizaTabla(stock,codigo):
            mi_conexion= sqlite3.connect("basededatosDesarrollo.db")  
            cursor=mi_conexion.cursor() 
            instruccion= f"UPDATE stockFerreteria SET  'cantidad'='{stock}' WHERE codigo='{codigo}'"
            cursor.execute(instruccion)
            mi_conexion.commit()
            mi_conexion.close()
            
def busqElementoTablaFerreteria(codigoBuscado):
    for producto in tablaFerreteria.get_children():
        print(producto)
        if codigoBuscado==tablaFerreteria.item(producto,'text'):
            print(f'el resultado de la funcion busqElelemtoTablaFerreteria es: {producto}')
            return producto

def selecElementoTablaFerreteria(codigoBuscado):
    if codigoBuscado=="":
        return
    codigoEncontrado=busqElementoTablaFerreteria(codigoBuscado)
    print (f'el codigo encontrado es: {codigoEncontrado}')
    if codigoEncontrado:
        tablaFerreteria.selection_set(codigoEncontrado)
        tablaFerreteria.focus(codigoEncontrado)


                

    
########SUMA SUBTOTALES###########################################################################
def sumaSubTotales():
        valoresRemito=tablaRemito.get_children()#lee todos los valores del treeview tablaRemito
        sumaSubTotales=0
        for valores in valoresRemito:
            valorItem= tablaRemito.item(valores,'values')
            valorSubtotal=(valorItem[5]).replace(',','')
            sumaSubTotales=sumaSubTotales+(float(valorSubtotal))
        lblValorTotal.config(text=(f"TOTAL STOCK CARGADO: ${sumaSubTotales:,.2f}-"),font=fuenteNegrita) 

    
    
##################################################################################################   
#INICIALIZACION DE VARIABLES######################################################################
codigoBusq=int()
descripcionBusq=()
itemTabla=()
sumaStock=()
spinCant= 0
##SPINBOX##########################################################################################
spinbox = ttk.Spinbox(ventanaRemito, from_=0, to=spinCant, increment=1, width=5)
spinbox.place(x=420,y=108)    

#ENTRY#############################################################################################
varUbicacion=ventanaRemito
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
lbl1=ttk.Label(ventanaRemito, text='VALOR DE STOCK CARGADO EN REMITO:',background='lightblue')
lbl1.place(x=10,y=10)
lbl10=ttk.Label(ventanaRemito, text='____________',background='lightblue')
lbl10.place(x=240,y=8)
########################################################
lblCodigo=ttk.Label(ventanaRemito, text='CODIGO:',background='lightblue')
lblCodigo.place(x=10,y=50)
lblCategoria=ttk.Label(ventanaRemito, text='CATEGORIA:',background='lightblue')
lblCategoria.place(x=125,y=50)
lblDescripcion=ttk.Label(ventanaRemito, text='DESCRIPCION:',background='lightblue')
lblDescripcion.place(x=10,y=80)
lblCantidad=ttk.Label(ventanaRemito, text='STOCK DSIPONIBLE:',background='lightblue')
lblCantidad.place(x=300,y=50)
lblPrecio=ttk.Label(ventanaRemito, text='PRECIO COSTO:',background='lightblue')
lblPrecio.place(x=10,y=110)
lblPrecioVP=ttk.Label(ventanaRemito, text='PRECIO VP:',background='lightblue')
lblPrecioVP.place(x=220,y=110)
lblValorTotal=ttk.Label(ventanaRemito, text=(f"TOTAL STOCK CARGADO: $ 0.00-"),font=fuenteNegrita,background='lightblue')
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

btn1=ctk.CTkButton(ventanaRemito,text='INSERTAR',command=insertarTablaRemito,fg_color="green", border_color='gray', hover_color='gray',text_color='black', border_width=1)
btn1.place(x=540,y=145)
#######################################
btn2=ctk.CTkButton(ventanaRemito,  text='BUSCAR CODIGO', command=busquedaCodigo,width=100, corner_radius=3)
btn2.place(x=540,y=90)
#######################################
btn3=ctk.CTkButton(ventanaRemito, text='BUSCAR DESCRIPCION', command=busquedaDescripcion,width=50)
btn3.place(x=540,y=50)
#######################################
btn4=ctk.CTkButton(ventanaRemito,  text='F2-CARGAR LISTA DE PRECIOS', command=mostarTabla,width=50)
btn4.place(x=300,y=145)
# #mostrarModificar(False)
#######################################
btn7=ctk.CTkButton(ventanaRemito ,text='BAJA PRODUCTO', command=borrarProductoRemito,width=50)
btn7.place(x=10,y=145)
#######################################
btn8=ctk.CTkButton(ventanaRemito,  text='LIMPIAR ENTRADA', command=limpiarEntry,width=50)
btn8.place(x=150,y=145)
#######################################
btn10=ctk.CTkButton(ventanaRemito, text='MODIFICAR', command=modiCantTablaRemito,width=50)
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
tablaFerreteria=ttk.Treeview(ventanaRemito,height=20,show='tree headings',columns=('#0', '#1','#2','#3','#4'))
tablaFerreteria.place(x=10,y=190,width=710,height=150)
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
tablaRemito=ttk.Treeview(ventanaRemito,height=20,show='tree headings',columns=('#0', '#1','#2','#3','#4','#5'))
tablaRemito.place(x=10,y=360,width=710,height=300)
tablaRemito.column('#0', width=18,anchor='e')
tablaRemito.heading('#0',text="CODIGO",anchor='center',)
tablaRemito.column('#1', width=40)
tablaRemito.heading('#1',text="CATEGORIA",anchor="center")
tablaRemito.column('#2', width=230)
tablaRemito.heading('#2',text="DESCRIPCION",anchor="center")
tablaRemito.column('#3', width=8,anchor='e')
tablaRemito.heading('#3',text="CANT.",anchor="center")
tablaRemito.column('#4', width=10,anchor='e')
tablaRemito.heading('#4',text="PRECIO",anchor="center")
tablaRemito.column('#5', width=15,anchor='e')
tablaRemito.heading('#5',text="PVP",anchor='center')
tablaRemito.column('#6', width=15,anchor='e')
tablaRemito.heading('#6',text="SUBTOTAL",anchor='center')
tablaRemito.bind("<ButtonRelease-1>", seleccionMouseTablaRemito)


mostarTabla()
ventanaRemito.mainloop()
