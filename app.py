from tkinter import *
from math import pi
ventana = Tk()


ventana.geometry("360x360")

radio = StringVar()
area = StringVar()
volumen = StringVar()
#region funciones
def calcular():
        pass
        r=float(radio.get())
        area.set((r**2)*pi*4)
        volumen.set((r**3)*pi*(4/3))
def borrar():
        pass
        radio.set("")
        area.set("")
        volumen.set("")


label1 = Label(ventana,text = "CALCULA EL AREA Y COLUMEN DE UN CIRCULO" ,font=("consolas",12,"bold")).place(x=53, y=40)
label2 = Label(ventana,text = "RADIO" ,font=("consolas",12,"bold")).place(x=50, y=90)
label3 = Label(ventana,text = "AREA" ,font=("consolas",12,"bold")).place(x=50, y=150)
label4 = Label(ventana,text = "VOLUMEN" ,font=("consolas",12,"bold")).place(x=50, y=210)
label5 = Label(ventana,text = "CALCULA EL AREA Y COLUMEN DE UN CIRCULO" ,font=("consolas",12,"bold")).place(x=53, y=40)

entry1 = Entry(textvariable=radio,font=("consolas", 15, "bold"), fg="black",bg="white").place(height=30,width=120,x=120,y=90)
entry2 = Entry(textvariable=area,font=("consolas", 15, "bold"), fg="black",bg="white").place(height=30,width=120,x=120,y=150)
entry3 = Entry(textvariable=volumen,font=("consolas", 15, "bold"), fg="black",bg="white").place(height=30,width=120,x=120,y=210)

button1 = Button(text="CALCULAR",font=("consolas",8,"bold"),command=lambda:calcular()).place(height=30,width=70,x=260,y=90)
button2 = Button(text="BORRAR",font=("consolas",8,"bold"),command=lambda:borrar()).place(height=30,width=70,x=260,y=150)

ventana.mainloop()