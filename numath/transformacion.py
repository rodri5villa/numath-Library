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
    funcion_entrada = re.sub(r'(?<=[xy])(?=[xy])', '*', funcion_entrada)

    return funcion_entrada

def crear_funcion(funcion_entrada):
    
    expr = reemplazar_funciones(funcion_entrada)
    # Detectar variables usadas
    vars_detectadas = []
    if re.search(r'\bx\b', expr):
        vars_detectadas.append('x')
    if re.search(r'\by\b', expr):
        vars_detectadas.append('y')
    if not vars_detectadas:
        # Por defecto asumimos variable x
        vars_detectadas.append('x')
    # Construir lambda con argumentos detectados
    args = ','.join(vars_detectadas)
    code = f"lambda {args}: {expr}"
    try:
        func = eval(code, {'math': math})
    except Exception as e:
        raise ValueError(f"Error al transformar la función '{funcion_entrada}': {e}")
    return func
