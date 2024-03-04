import tkinter as tk
import math

def calcular_area_circulo():
    try:
        radio = float(entry_radio.get())
        area = math.pi * radio**2
        label_resultado.config(text=f"Área: {area}")
    except ValueError:
        label_resultado.config(text="Ingresa un valor válido para el radio")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Área de Círculo")

# Crear widgets
label_instrucciones = tk.Label(ventana, text="Ingresa el radio del círculo:")
entry_radio = tk.Entry(ventana)
boton_calcular = tk.Button(ventana, text="Calcular Área", command=calcular_area_circulo)
label_resultado = tk.Label(ventana, text="PIZA")

# Posicionar widgets
label_instrucciones.pack()
entry_radio.pack()
boton_calcular.pack()
label_resultado.pack()

# Iniciar bucle de la aplicación
ventana.mainloop()