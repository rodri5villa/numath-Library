from numath.transformacion import crear_funcion

### Punto medio de tres puntos ###

def derivative_three_points_central(funcion, x0, h):
   
    f = crear_funcion(funcion)
    return (f(x0 + h) - f(x0 - h)) / (2 * h)

### Extremo de tres puntos ###

def derivative_three_points_border(funcion, x0, h):
    
    f = crear_funcion(funcion)
    return (-3 * f(x0) + 4 * f(x0 + h) - f(x0 + 2 * h)) / (2 * h)

### Punto medio de cinco puntos ###

def derivative_five_points_central(funcion, x0, h):
    
    f = crear_funcion(funcion)
    return (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12 * h)

### Extremo de cinco puntos ###

def derivative_five_points_border(funcion, x0, h):
   
    f = crear_funcion(funcion)
    return (-25 * f(x0) + 48 * f(x0 + h) - 36 * f(x0 + 2 * h) + 16 * f(x0 + 3 * h) - 3 * f(x0 + 4 * h)) / (12 * h)

### Derivadas unificadas respecto a los puntos dados ###

def derivative_unified(datos, x0):
    
    claves = sorted(datos.keys())
    n = len(claves)
    
    if n < 3:
        raise ValueError("Se requieren al menos 3 puntos para calcular la derivada.")
    
    h = claves[1] - claves[0]
    
    if x0 not in claves:
        raise ValueError("El valor x0 no se encuentra en los datos proporcionados.")
    
    i = claves.index(x0)
    
    if n >= 5 and i >= 2 and i <= n - 3:
        return (datos[claves[i-2]] - 8 * datos[claves[i-1]] + 8 * datos[claves[i+1]] - datos[claves[i+2]]) / (12 * h)
    
    if i == 0:
        if n < 5:
            return (-3 * datos[claves[0]] + 4 * datos[claves[1]] - datos[claves[2]]) / (2 * h)
        else:
            return (-25 * datos[claves[0]] + 48 * datos[claves[1]] - 36 * datos[claves[2]] + 16 * datos[claves[3]] - 3 * datos[claves[4]]) / (12 * h)
    
    if i == n - 1:
        if n < 5:
            return (3 * datos[claves[n-1]] - 4 * datos[claves[n-2]] + datos[claves[n-3]]) / (2 * h)
        else:
            return (25 * datos[claves[n-1]] - 48 * datos[claves[n-2]] + 36 * datos[claves[n-3]] - 16 * datos[claves[n-4]] + 3 * datos[claves[n-5]]) / (12 * h)
    
    if i > 0 and i < n - 1:
        return (datos[claves[i+1]] - datos[claves[i-1]]) / (2 * h)
    
    raise ValueError("No se pudo calcular la derivada para x0 con los datos proporcionados.")

### Punto medio de la segunda derivada ###

def second_derivative_central(funcion, x0, h):
    
    f = crear_funcion(funcion)
    return (f(x0 - h) - 2 * f(x0) + f(x0 + h)) / (h**2)

### Punto medio de la segunda derivada respecto a los puntos dados ###

def second_derivative_central_data(datos, x0):

    claves = sorted(datos.keys())
    n = len(claves)
    
    if n < 3:
        raise ValueError("Se requieren al menos 3 puntos para calcular la segunda derivada.")
    
    h = claves[1] - claves[0]
    
    if x0 not in claves:
        raise ValueError("El valor x0 no se encuentra en los datos proporcionados.")
        
    i = claves.index(x0)
    
    if i == 0 or i == n - 1:
        raise ValueError("Para la fórmula central se requiere que x0 no esté en un extremo.")
    
    return (datos[claves[i-1]] - 2 * datos[x0] + datos[claves[i+1]]) / (h**2)
