import tkinter as tk
from tkinter import *

def limpiarcampos():
    numA.set(0)
    numB.set(0)

def sumar():
    numeroA=numA.get()
    numeroB=numB.get()
    resultado= numeroA+numeroB
    Res.set(resultado)
    limpiarcampos()
def restar():
    numeroA = numA.get()
    numeroB = numB.get()
    resultado = numeroA - numeroB
    Res.set(resultado)
    limpiarcampos()
def multiplicar():
    numeroA = numA.get()
    numeroB = numB.get()
    resultado = numeroA * numeroB
    Res.set(resultado)
    limpiarcampos()
def dividir():
    numeroA = numA.get()
    numeroB = numB.get()
    resultado = numeroA / numeroB
    Res.set(resultado)
    limpiarcampos()
#Creacion de ventana
#Utilizamos el "tk" porque en la parte superior de la iumportacion de la libreria indicamos que
#en vez de ultilizar la palabra "tkinter" utilizaremos "tk" por eso es el uso del as.
ventana= tk.Tk()
#Configurar el tamaño de la ventana
ventana.config(width=300, height=200)
etiquetaNA=Label(ventana,text="Número A: ")
etiquetaNA.place(x=0,y=0)
numA=IntVar()
#Creacion de una entrada "caja de texto" con la palabra "ttk" que proviene de la libreria tkinter
#Le indicamos tambien que esta entrada estara entro de nuestra ventana
entradaNA=Entry(ventana, textvariable=numA)
#Posteriormente le damos una posicion a esta entrada o caja de texto
entradaNA.place(x=70,y=0)

etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)
numB=IntVar()
entradaNB=Entry(ventana, textvariable=numB)
entradaNB.place(x=70,y=30)

etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)
Res=IntVar()
salidaRES=Entry(ventana, textvariable=Res)
salidaRES.place(x=70,y=60)

botontransportar=Button(ventana, text="Sumar", command=sumar)
botontransportar.place(x=0,y=90)
botontransportar=Button(ventana, text="Restar", command=restar)
botontransportar.place(x=0,y=120)
botontransportar=Button(ventana, text="Multiplicar", command=multiplicar)
botontransportar.place(x=0,y=150)
botontransportar=Button(ventana, text="Dividir", command=dividir)
botontransportar.place(x=0,y=180)


ventana.mainloop()
