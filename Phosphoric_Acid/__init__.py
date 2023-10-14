import tkinter as tk
import math
from scipy.optimize import fsolve
from tools.Pipe.pipe_choice import choice_type_pipe

# Definir la función para calcular el diámetro de la tubería y mostrar el resultado de choice_type_pipe
def calcular_diametro():
    sustancia_a_transportar = sustancia_var.get()
    
    # Llamar a choice_type_pipe solo si la sustancia seleccionada es "Ácido Fosfórico"
    if sustancia_a_transportar == "ácido":
        resultado_choice = choice_type_pipe(sustancia_a_transportar)
        resultado_choice_label.config(text=resultado_choice)
    else:
        resultado_choice_label.config(text="")

    # Definir la función que representa el sistema de ecuaciones
    def sistema_ecuaciones(x):
        D, V = x
        ecuacion_cuadratica = (math.pi / 4) * D**2 * V - 2.12*10**-4
        ecuacion_lineal = ((V * D ) / (1.67712*10**-7)) - 8000
        return [ecuacion_cuadratica, ecuacion_lineal]

    # Adivinanza inicial para D y V
    x0 = [0.5, 0.0001]  # Cambiar los valores iniciales para estar más cerca de la solución

    # Resolver el sistema de ecuaciones utilizando fsolve con un máximo de 500,000 evaluaciones
    solucion = fsolve(sistema_ecuaciones, x0, maxfev=500)

    # Extraer D y V de la solución
    D, V = solucion

    # Verificar que D no sea mayor que 0.140
    if D > 0.140:
        D = 0.140

    # Mostrar la solución en la etiqueta de resultado
    resultado_label.config(text=f"La solución del sistema es: D = {D}, V = {V}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Diámetro y Velocidad de Tubería")

# Etiqueta para seleccionar la sustancia
sustancia_label = tk.Label(ventana, text="Seleccione la sustancia a transportar:")
sustancia_label.pack()

# Variable de control para la selección de la sustancia
sustancia_var = tk.StringVar(ventana)
sustancia_var.set("Ácido Fosfórico")  # Valor por defecto

# Menú desplegable para seleccionar la sustancia
sustancia_menu = tk.OptionMenu(ventana, sustancia_var, "Ácido Fosfórico", "Otra Sustancia")
sustancia_menu.pack()

# Botón para calcular el diámetro
calcular_button = tk.Button(ventana, text="Calcular Diámetro", command=calcular_diametro)
calcular_button.pack()

# Etiqueta para mostrar el resultado de choice_type_pipe
resultado_choice_label = tk.Label(ventana, text="")
resultado_choice_label.pack()

# Etiqueta para mostrar el resultado de los cálculos
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Iniciar la aplicación
ventana.mainloop()
