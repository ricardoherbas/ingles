import tkinter as Tk
from tkinter import ttk
from tkinter import *
ventana= Tk()
ventana.title("TALLER MECANICO EL TUERCA")
ventana.config(bg="light blue")
#ventana.iconbitmap("tuerca.ico")
tabla=ttk.Treeview(ventana)

titulo=Label(ventana,text="EL TUERCA",font=("arial bold",30),bg="yellow",fg="black")
titulo.grid(row=0,column=0,columnspan=9,padx=20,pady=20)    

id1=Label(ventana,text="Id",font=("arial bold",15),bg="light blue")
cliente1=Label(ventana,text="Cliente",font=("arial bold",15),bg="light blue")
vehiculo1=Label(ventana,text="Vehiculo",font=("arial bold",15),bg="light blue")
detalle1=Label(ventana,text="Detalle",font=("arial bold",15),bg="light blue")
fecha1=Label(ventana,text="Fecha",font=("arial bold",15),bg="light blue")
id1.grid(row=1,column=0,padx=10,pady=10)
cliente1.grid(row=2,column=0,padx=10,pady=10)
vehiculo1.grid(row=3,column=0,padx=10,pady=10)
detalle1.grid(row=4,column=0,padx=10,pady=10)
fecha1.grid(row=5,column=0,padx=10,pady=10)

ingreso_id=Entry(ventana,width=30,bd=10)
ingreso_cliente=Entry(ventana,width=30,bd=10)
ingreso_vehiculo=Entry(ventana,width=30,bd=10)
ingreso_detalle=Entry(ventana,width=30,bd=10)
ingreso_fecha=Entry(ventana,width=30,bd=10)
ingreso_id.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
ingreso_cliente.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
ingreso_vehiculo.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
ingreso_detalle.grid(row=4,column=1,columnspan=3,padx=5,pady=5)
ingreso_fecha.grid(row=5,column=1,columnspan=3,padx=5,pady=5)

Id=str(ingreso_id.get())
Cliente=str(ingreso_cliente.get())
Vehiculo=str(ingreso_vehiculo.get())
Detalle=str(ingreso_detalle.get())
Fecha=str(ingreso_fecha.get())

ingresar1=Button(ventana,text="Ingresar",padx=5,pady=5,width=5,bd=5)
ingresar1.grid(row=6,column=1,columnspan=1)
borrar=Button(ventana,text="Borrar",padx=5,pady=5,width=5,bd=5)
borrar.grid(row=6,column=2,columnspan=1)
imprimir1=Button(ventana,text="Mostrar",padx=5,pady=5,width=5,bd=5)
imprimir1.grid(row=6,column=3,columnspan=1)

estilo=ttk.Style()
estilo.configure("Treeview.Heading",font=("arial bold",15))


tabla["columns"]=("Id","Cliente","Vehiculo","Detalle","Fecha")
tabla.column("#0",width=0,stretch=NO)
tabla.column("Id",anchor=W,width=100)
tabla.column("Cliente",anchor=W,width=100)
tabla.column("Vehiculo",anchor=W,width=100)
tabla.column("Detalle",anchor=W,width=100)
tabla.column("Fecha",anchor=W,width=100)
                                            
tabla.heading("#0")
tabla.heading("Id",text="Id")
tabla.heading("Cliente",text="Cliente")
tabla.heading("Vehiculo",text="Vehiculo")
tabla.heading("Detalle",text="Detalle")
tabla.heading("Fecha",text="Fecha")


tabla.grid(row=1,column=5,columnspan=5,rowspan=5)

ventana.mainloop()              
                    

