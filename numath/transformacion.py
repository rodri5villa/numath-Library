import math
import re

def reemplazar_funciones(funcion_entrada):

    partes_a_reemplazar = {
        'asen(': 'math.asin(',
        'acos(': 'math.acos(',
        'atan(': 'math.atan(',
        'sen(': 'math.sin(',
        'cos(': 'math.cos(',
        'tan(': 'math.tan(',
        'exp()': 'math.e',
        'exp(': 'math.exp(',
        'ln(': 'math.log(',
        'log(': 'math.log(',
        'sqrt(': 'math.sqrt(',
        '^': '**',
        'pow(': 'math.pow(',
        'pi': 'math.pi'
    }

    # Realizar los reemplazos definidos en el diccionario
    for parte, reemplazo in partes_a_reemplazar.items():
        funcion_entrada = funcion_entrada.replace(parte, reemplazo)
    
    # Usar expresiones regulares para insertar el operador de multiplicación
    # Ejemplo: "3x" -> "3*x" o "2sin(x)" -> "2*math.sin(x)"
    funcion_entrada = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', funcion_entrada)

    return funcion_entrada

def crear_funcion(funcion_entrada):
    
    # Primero se realiza el reemplazo de la notación
    funcion_transformada = reemplazar_funciones(funcion_entrada)
    
    # Se construye la función lambda usando eval. Se limita el scope para que solo se pueda acceder a math (y al parámetro x).
    try:
        funcion = eval("lambda x: " + funcion_transformada, {"math": math})
    except Exception as e:
        raise ValueError("Error al transformar la función: " + str(e))
    
    return funcion
