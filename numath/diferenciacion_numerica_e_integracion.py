from numath.transformacion import crear_funcion

### Punto medio de tres puntos ###

def derivative_three_points_central(funcion, x, h):
    """
    Calcula la derivada de una función en x usando la fórmula central de tres puntos.
    
    Fórmula:
        f'(x) ≈ (f(x + h) - f(x - h)) / (2*h)
    
    Parámetros:
        f: función a derivar
        x: punto en el que se calcula la derivada
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
    """
    f = crear_funcion(funcion)
    return (f(x + h) - f(x - h)) / (2 * h)

### Extremo de tres puntos ###

def derivative_three_points_forward(funcion, x, h):
    """
    Calcula la derivada de una función en x (extremo) usando la fórmula hacia adelante de tres puntos.
    
    Fórmula:
        f'(x) ≈ (-3f(x) + 4f(x + h) - f(x + 2*h)) / (2*h)
        
    Parámetros:
        f: función a derivar
        x: punto en el extremo (normalmente el inicio del intervalo)
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
    """
    f = crear_funcion(funcion)
    return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)

### Punto medio de cinco puntos ###

def derivative_five_points_central(funcion, x, h):
    """
    Calcula la derivada de una función en x usando la fórmula central de cinco puntos.
    
    Fórmula:
        f'(x) ≈ (f(x - 2*h) - 8f(x - h) + 8f(x + h) - f(x + 2*h)) / (12*h)
        
    Parámetros:
        f: función a derivar
        x: punto en el que se calcula la derivada
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
    """
    f = crear_funcion(funcion)
    return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)

### Extremo de cinco puntos ###

def derivative_five_points_forward(funcion, x, h):
    """
    Calcula la derivada de una función en x (extremo) usando la fórmula hacia adelante de cinco puntos.
    
    Fórmula:
        f'(x) ≈ (-25f(x) + 48f(x + h) - 36f(x + 2*h) + 16f(x + 3*h) - 3f(x + 4*h)) / (12*h)
        
    Parámetros:
        f: función a derivar
        x: punto en el extremo (normalmente el inicio del intervalo)
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
    """
    f = crear_funcion(funcion)
    return (-25 * f(x) + 48 * f(x + h) - 36 * f(x + 2 * h) + 16 * f(x + 3 * h) - 3 * f(x + 4 * h)) / (12 * h)

### Derivadas unificadas con respecto a los puntos dados ###

def derivative_unified(datos, x0):
    """
    Calcula la derivada numérica en x0 a partir de datos discretos (en un diccionario {x: f(x)})
    utilizando la siguiente lógica:
    
    - Si hay al menos 5 puntos y x0 tiene dos vecinos a cada lado, se usa la fórmula central de cinco puntos.
    - Si x0 es el primer elemento:
         - Si hay menos de 5 puntos se usa la fórmula forward de tres puntos.
         - Sino se utiliza la fórmula forward de cinco puntos.
    - Si x0 es el último elemento:
         - Si hay menos de 5 puntos se usa la fórmula backward de tres puntos.
         - Sino se utiliza la fórmula backward de cinco puntos.
    - En otro caso, se usa la fórmula central de tres puntos.
    
    Se asume que los datos están equidistantes.
    
    Parámetros:
        datos: Diccionario con los pares {x: f(x)}.
        x0: El valor de x en el que se quiere estimar la derivada.
    
    Retorna:
        Aproximación de la derivada f'(x0).
    """
    # Ordenar las claves (valores de x) de manera creciente.
    claves = sorted(datos.keys())
    n = len(claves)
    
    if n < 3:
        raise ValueError("Se requieren al menos 3 puntos para calcular la derivada.")
    
    # Suponemos que los datos son equidistantes; se calcula h tomando el primer par.
    h = claves[1] - claves[0]
    
    if x0 not in claves:
        raise ValueError("El valor x0 no se encuentra en los datos proporcionados.")
    i = claves.index(x0)
    
    # Caso 1: Fórmula central de 5 puntos para mayor precisión (para puntos interiores)
    if n >= 5 and i >= 2 and i <= n - 3:
        return (datos[claves[i-2]] - 8 * datos[claves[i-1]] + 8 * datos[claves[i+1]] - datos[claves[i+2]]) / (12 * h)
    
    # Caso 2: x0 es el primer elemento (extremo izquierdo)
    if i == 0:
        # Si hay menos de 5 puntos, usar forward de 3 puntos
        if n < 5:
            return (-3 * datos[claves[0]] + 4 * datos[claves[1]] - datos[claves[2]]) / (2 * h)
        else:
            # Hay al menos 5 puntos, usar forward de 5 puntos
            return (-25 * datos[claves[0]] + 48 * datos[claves[1]] - 36 * datos[claves[2]] + 16 * datos[claves[3]] - 3 * datos[claves[4]]) / (12 * h)
    
    # Caso 3: x0 es el último elemento (extremo derecho)
    if i == n - 1:
        # Si hay menos de 5 puntos, usar backward de 3 puntos
        if n < 5:
            return (3 * datos[claves[n-1]] - 4 * datos[claves[n-2]] + datos[claves[n-3]]) / (2 * h)
        else:
            # Hay al menos 5 puntos, usar backward de 5 puntos
            return (25 * datos[claves[n-1]] - 48 * datos[claves[n-2]] + 36 * datos[claves[n-3]] - 16 * datos[claves[n-4]] + 3 * datos[claves[n-5]]) / (12 * h)
    
    # Caso 4: x0 es un punto interior pero no se cumple la condición para la fórmula central de 5 puntos,
    # en este caso se utiliza la fórmula central de 3 puntos.
    if i > 0 and i < n - 1:
        return (datos[claves[i+1]] - datos[claves[i-1]]) / (2 * h)
    
    raise ValueError("No se pudo calcular la derivada para x0 con los datos proporcionados.")

# Ejemplo de uso:
datos = {
    1.8: 10.889365,  
    1.9: 12.703199,
    2.0: 14.778112,
    2.1: 17.148957,
    2.2: 19.855030
}
x0 = 2.0
derivada = derivative_unified(datos, x0)
print("Derivada unificada en", x0, "=", derivada)




# # Ejemplo de uso con la función sin(x)
# if __name__ == "__main__":
#     funcion = "ln(x) * sin(x)"
#     x = 3  
#     h = 0.1

#     # Calcular derivadas usando diferentes fórmulas
#     deriv_central_3 = derivative_three_points_central(funcion, x, h)
#     print("Derivada (central, 3 puntos):", deriv_central_3)
    
  

 
