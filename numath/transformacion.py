import math
import re

def reemplazar_funciones(funcion_entrada):

    partes_a_reemplazar = {
        'asin(': 'math.asin(',
        'acos(': 'math.acos(',
        'atan(': 'math.atan(',
        'sin(': 'math.sin(',
        'cos(': 'math.cos(',
        'tan(': 'math.tan(',
        'exp()': 'math.e',
        'exp(': 'math.exp(',
        'ln(': 'math.log(',
        # 'log(': 'math.log(',
        'sqrt(': 'math.sqrt(',
        '^': '**',
        'pow(': 'math.pow(',
        'pi': 'math.pi'
    }

    # Realizar los reemplazos definidos en el diccionario
    for parte, reemplazo in partes_a_reemplazar.items():
        funcion_entrada = funcion_entrada.replace(parte, reemplazo)
    
    # Usar expresiones regulares para insertar el operador de multiplicación
    # Dígito seguido de letra/función
    funcion_entrada = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', funcion_entrada)
    # Variable x o y seguida de otra x o y
    funcion_entrada = re.sub(r'(?<=[xyz])(?=[xyz])', '*', funcion_entrada)

    return funcion_entrada

def crear_funcion(funcion_entrada: str):
    """
    Crea una lambda con firma (x=0, y=0, z=0), sin aceptar otros kwargs.
    - Si usas sólo x, llama f(x=valor) o f(valor).
    - Si usas sólo y, llama f(y=valor).
    - Si usas sólo z, llama f(z=valor).
    - Cualquier otro keyword, e.g. w=..., lanzará TypeError.
    """
    expr = reemplazar_funciones(funcion_entrada)
    code = f"lambda x=0, y=0, z=0: {expr}"
    try:
        func = eval(code, {'math': math})
    except Exception as e:
        raise ValueError(f"Error al transformar '{funcion_entrada}': {e}")
    return func