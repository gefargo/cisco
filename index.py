#importacion de toda la libreria de tkinter
from tkinter import *
root = Tk()


display = Entry(root)
display.grid(row = 0, column=0, columnspan=4, padx = 5, pady = 5 )
#objetos 
bonton1 = Button(root, text="1", width=5, height=2)
bonton2 = Button(root, text="2", width=5, height=2)
bonton3 = Button(root, text="3", width=5, height=2)
bonton4 = Button(root, text="4", width=5, height=2)
bonton5 = Button(root, text="5", width=5, height=2)
bonton6 = Button(root, text="6", width=5, height=2)
bonton7 = Button(root, text="7", width=5, height=2)
bonton8 = Button(root, text="8", width=5, height=2)
bonton9 = Button(root, text="9", width=5, height=2)
bonton0 = Button(root, text="0", width=5, height=2)

boton_borrar = Button(root, text= "AC", width=5, height= 2)
boton_parentesis1 = Button(root, text= "(", width=5, height= 2)
boton_parentesis2 = Button(root, text= ")", width=5, height= 2)

boton_punto = Button(root, text= ".", width=5, height= 2)
boton_div = Button(root, text= "/", width=5, height= 2)
boton_mult = Button(root, text= "x", width=5, height= 2)
boton_sum = Button(root, text= "+", width=5, height= 2)
boton_rest= Button(root, text= "-", width=5, height= 2)
boton_igual = Button(root, text= "AC", width=5, height= 2)

#pocisiones de los botones 

bonton1.grid(row= 1, column= 1, padx= 5) 
bonton2.grid(row= 1, column= 2, padx= 5)
bonton3.grid(row= 1, column= 3, padx= 5)
bonton4.grid(row= 2, column= 1, padx= 5)
bonton5.grid(row= 2, column= 2, padx= 5)
bonton6.grid(row= 2, column= 3, padx= 5)
bonton7.grid(row= 3, column= 1, padx= 5)
bonton8.grid(row= 3, column= 2, padx= 5)
bonton9.grid(row= 3, column= 3, padx= 5)
bonton0.grid(row= 4, column= 1, padx= 5)

root.mainloop()





