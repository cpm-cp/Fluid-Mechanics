# Este programa calcula el diamtetro real y elige el material de la tubería y el diametro nominal
# para una sustancia en específico (Ácido fosfórico)
 
from math import pi
from scipy.optimize import fsolve
from pipe_choice import choice_type_pipe

## Las sustancias con posibilidad de transportar son:
## Insert List ###
## Pero para efectos prácticos sólo está codificado para el H3PO4 []
## Se puede escalar


def calcular_diametro(substance_to_transport: str):
    # Llama a la función para realizar la selección con una sustancia de la lista substances_type
    choice_type_pipe(substance_to_transport)

    # Calcular el diámetro de la tubería de polipropileno y la velocidad del fluido 

# Definir la función que representa el sistema de ecuaciones
def sistema_ecuaciones(x):
    D, V = x
    ecuacion_cuadratica = (pi / 4) * D**2 * V - 2.12*10**-4
    ecuacion_lineal = ((V * D ) / (1.67712*10**-7)) - 8000
    return [ecuacion_cuadratica, ecuacion_lineal]


# Lamar la función calcular diámetro
ácido = calcular_diametro("ácido")
print(ácido)

# Adivinanza inicial para D y V
x0 = [0.5, 0.0001]  # Cambiar los valores iniciales para estar más cerca de la solución

# Resolver el sistema de ecuaciones utilizando fsolve con un máximo de 500,000 evaluaciones
solucion = fsolve(sistema_ecuaciones, x0, maxfev=5000)

# Extraer D y V de la solución
D, V = solucion

# Verificar que D no sea mayor que 0.140
if D > 0.140:
    D = 0.140

# Mostrar la solución
print(f"La solución del sistema es: D = {D}, V = {V}")