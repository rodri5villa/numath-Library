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

### FÓRMULAS NEWTON-COTES CERRADAS ###

### n=1: Regla Trapezoidal ###

def newton_cotes_n1_close(funcion, a, b):
   
    f = crear_funcion(funcion)
    h = b - a
    I = (h / 2) * (f(a) + f(b)) 
    return I

### n=2: Regla de Simpson ###

def newton_cotes_n2_close(funcion, a, b):
    
    f = crear_funcion(funcion)
    h = (b - a) / 2
    I = (h / 3) * (f(a) + 4 * f(a + h) + f(b))
    return I

### n=3: Regla de Simpson 3/8 ###

def newton_cotes_n3_close(funcion, a, b):
    
    f = crear_funcion(funcion)
    h = (b - a) / 3
    I = (3 * h / 8) * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))
    return I

### n=4

def newton_cotes_n4_close(funcion, a, b):
    
    f = crear_funcion(funcion)
    h = (b - a) / 4
    I = (2 * h / 45) * (7 * f(a) + 32 * f(a + h) + 12 * f(a + 2 * h) + 32 * f(a + 3 * h) + 7 * f(b))
    return I

### FÓRMULAS NEWTON-COTES ABIERTAS ###

### n=0: Regla del Punto Medio ###
def newton_cotes_n0_open(funcion, a, b):
    
    f = crear_funcion(funcion)
    h = (b - a) / 2.0
    x0 = a + h
    I = 2 * h * f(x0)
    return I

### n=1 ###

def newton_cotes_n1_open(funcion, a, b):
    
    f = crear_funcion(funcion)
    h = (b - a) / 3.0
    x0 = a + h
    x1 = x0 + h  
    I = (3.0 * h / 2.0) * (f(x0) + f(x1))
    return I

### n=2 ###

def newton_cotes_n2_open(funcion, a, b):
    
    f = crear_funcion(funcion)
    h = (b - a) / 4.0
    x0 = a + h
    x1 = x0 + h   
    x2 = x1 + h   
    I = (4.0 * h / 3.0) * (2.0 * f(x0) - f(x1) + 2.0 * f(x2))
    return I

### n=3 ###

def newton_cotes_n3_open(funcion, a, b):
    
    f = crear_funcion(funcion)
    h = (b - a) / 5.0
    x0 = a + h
    x1 = x0 + h   
    x2 = x1 + h   
    x3 = x2 + h   
    I = (5.0 * h / 24.0) * (11.0 * f(x0) + f(x1) + f(x2) + 11.0 * f(x3))
    return I

### Regla de Simpson Compuesta ###

def composite_simpson_rule(funcion, a, b, n):
    
    f = crear_funcion(funcion)
    
    if n <= 0 or n % 2 != 0:
        raise ValueError("El número de subintervalos n debe ser un entero par positivo.")
    
    h = (b - a) / n
    
    sum_odd = 0.0   
    sum_even = 0.0  
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum_even += f(x)
        else:
            sum_odd += f(x)
    
    I = (h / 3.0) * (f(a) + 2.0 * sum_even + 4.0 * sum_odd + f(b))
    return I

### Regla Trapezoidal Compuesta ###

def composite_trapezoidal_rule(funcion, a, b, n):
    
    f = crear_funcion(funcion)

    if n <= 0:
        raise ValueError("El número de subintervalos n debe ser un entero positivo.")

    h = (b - a) / n

    suma_interiores = 0.0
    for j in range(1, n):
        xj = a + j * h
        suma_interiores += f(xj)

    I = (h / 2.0) * (f(a) + 2.0 * suma_interiores + f(b))
    return I

### Regla del Punto Medio Compuesta ###

def composite_midpoint_rule(funcion, a, b, n):
    
    f = crear_funcion(funcion)

    if n <= 0 or n % 2 != 0:
        raise ValueError("El número de subintervalos n debe ser un entero positivo y par.")

    h = (b - a) / n
    suma_mid = 0.0

    for j in range(1, n, 2):
        xj = a + j * h
        suma_mid += f(xj)

    I = 2.0 * h * suma_mid
    return I
