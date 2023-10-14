import math
import numpy as np
from pydantic import BaseModel

substances_type = ["ácido", "hydroxide", "ammine", "carboxyl", "alcohol"]
capitalized_substances_type = [s.capitalize() for s in substances_type]

def substance_type(type: str) -> str:
    try:
        if type.capitalize() in capitalized_substances_type:
            return type
        else:
            None
    except ValueError:
        print("Tipo de sustancia no contenida")

class PipeTypeItem(BaseModel):
    tipo: str
    descripcion: str
    resumen: str
    precio: float

class PipeType(BaseModel):
    tipos: list[PipeTypeItem]

# Lista de tipos de tuberías completada
tipos_de_tuberias = [
    {
        "tipo": "Tuberías de acero al carbono",
        "descripcion": "Las tuberías de acero al carbono son duraderas y resistentes a la corrosión, lo que las hace ideales para transportar agua, gas natural, aceite crudo y una variedad de productos químicos.",
        "resumen": "Resistente a la corrosión, adecuado para varios fluidos.",
        "precio": 20.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de PVC (Policloruro de vinilo)",
        "descripcion": "Las tuberías de PVC son ligeras, económicas y resistentes a la corrosión. Se utilizan principalmente para el transporte de agua potable, aguas residuales, productos químicos no corrosivos y sistemas de irrigación.",
        "resumen": "Económico y resistente a la corrosión, utilizado en agua y sistemas de riego.",
        "precio": 10.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de cobre",
        "descripcion": "Las tuberías de cobre son conocidas por su excelente conductividad térmica y resistencia a la corrosión. Se utilizan para transportar agua potable, gases medicinales y sistemas de calefacción y refrigeración.",
        "resumen": "Conductividad térmica excepcional, resistente a la corrosión.",
        "precio": 30.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de plástico PE (Polietileno)",
        "descripcion": "El polietileno es resistente a la corrosión y se utiliza en tuberías para el transporte de agua potable, gas natural, productos químicos no corrosivos y sistemas de riego.",
        "resumen": "Resistente a la corrosión, utilizado en agua y sistemas de riego.",
        "precio": 15.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de hierro fundido dúctil",
        "descripcion": "Estas tuberías son resistentes y duraderas, adecuadas para el transporte de agua potable, aguas residuales, lodos y otros fluidos con sólidos en suspensión.",
        "resumen": "Resistente y duradero, utilizado en agua y fluidos con sólidos en suspensión.",
        "precio": 25.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de acero inoxidable",
        "descripcion": "El acero inoxidable es altamente resistente a la corrosión y se utiliza para transportar una amplia variedad de ácidos corrosivos en aplicaciones industriales.",
        "resumen": "Altamente resistente a la corrosión, utilizado en aplicaciones industriales.",
        "precio": 40.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de titanio",
        "descripcion": "El titanio es extremadamente resistente a la corrosión y se utiliza en aplicaciones donde se requiere una resistencia excepcional a ácidos altamente corrosivos.",
        "resumen": "Extremadamente resistente a la corrosión, utilizado en ácidos altamente corrosivos.",
        "precio": 60.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de plástico reforzado con fibra de vidrio (FRP)",
        "descripcion": "Las tuberías de FRP son resistentes a la mayoría de los ácidos y productos químicos corrosivos, siendo ideales para aplicaciones en la industria química y plantas de tratamiento de aguas residuales.",
        "resumen": "Resistente a ácidos y productos químicos corrosivos, utilizado en la industria química y plantas de tratamiento de aguas residuales.",
        "precio": 35.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de polipropileno (PP) y polietileno de alta densidad (PEAD)",
        "descripcion": "El PP y el PEAD son plásticos resistentes a una amplia gama de ácidos y productos químicos corrosivos y se utilizan en aplicaciones donde no se requiere resistencia extrema a la corrosión.",
        "resumen": "Resistente a ácidos y productos químicos corrosivos, utilizado en aplicaciones diversas.",
        "precio": 18.0  # Precio promedio en dólares por un tramo de tubería
    },
    {
        "tipo": "Tuberías de polietileno clorado (CPVC)",
        "descripcion": "El CPVC es un material termoplástico resistente a la corrosión y se utiliza para transportar ácidos y productos químicos en aplicaciones de procesamiento químico e industrial.",
        "resumen": "Resistente a ácidos y productos químicos, utilizado en procesamiento químico e industrial.",
        "precio": 22.0  # Precio promedio en dólares por un tramo de tubería
    },
]

# Crear instancias de PipeTypeItem a partir de la lista de tipos_de_tuberias
pipe_type_items = [PipeTypeItem(**item) for item in tipos_de_tuberias]

# Crear una instancia de PipeType con la lista de PipeTypeItem
pipe_type = PipeType(tipos=pipe_type_items)

def choice_type_pipe(substance=substances_type) -> str:
    '''
    Esta función elige el tipo de tubería necesaria para transportar un fluido en concreto
    (Ácido fosfórico), esto en función del precio y las características que esta brinde para
    el fluido.

    Recibe el tipo de sustancia como parámetro.
    substance: str
    '''

    # Verifica si la sustancia está en la lista substances_type
    if substance in substances_type:
        # Llama a la función substance_type() con el tipo de sustancia como argumento
        selected_substance = substance_type(substance)
        
        # Verifica si substance_type() ha devuelto una sustancia válida
        if selected_substance:
            # Inicializa una lista para almacenar las tuberías que cumplen con la condición
            tuberias_cumplen_condicion = []
            
            # Itera a través de las tuberías para encontrar las que contienen "ácido" y "corrosivo" en descripción y resumen
            for item in pipe_type.tipos:
                if "corrosivo" in item.resumen and "ácido" in item.resumen:
                    tuberias_cumplen_condicion.append(item)
            
            # Comprueba si se encontraron tuberías que cumplan la condición
            if tuberias_cumplen_condicion:
                # Encuentra la tubería con el precio más bajo
                tuberia_menor_precio = min(tuberias_cumplen_condicion, key=lambda x: x.precio)
                
                # Imprime la tubería con el precio más bajo
                print(f"Tubería con menor precio entre las que cumplen la condición para el tipo de sustancia '{selected_substance}':")
                print(f"Tipo: {tuberia_menor_precio.tipo}, Precio: {tuberia_menor_precio.precio} USD\n")
            else:
                print(f"No se encontraron tuberías que cumplan la condición para la sustancia '{selected_substance}'.")
        else:
            print(f"El tipo de sustancia '{substance}' no es válido.")
    else:
        print(f"El tipo de sustancia '{substance}' no está en la lista de sustancias válidas.")