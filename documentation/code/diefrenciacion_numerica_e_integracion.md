# Documentación Módulo Diferenciación Númerica e Integración

## 1. Punto medio de tres puntos (`derivative_three_points_central(funcion, x0, h)`)

Calcula la derivada de una función en el punto `x0` utilizando la **fórmula del punto medio de tres puntos**. 

### Fórmula

`f'(x0) = (f(x0 + h) - f(x0 - h)) / (2 * h)`

### Parámetros de Entrada y Salida

```python
def derivative_three_points_central(funcion, x0, h):
"""    
    Parámetros:
        funcion: función a derivar
        x0: punto en el que se calcula la derivada
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
"""
```

### Ejemplo de uso

```python
funcion = "x^2" 
x0 = 2.0
h = 0.001
derivada = derivative_three_points_central(funcion, x0, h)
print("La derivada aproximada de x^2 en x=2 es:", derivada)
```

## 2. Extremo de tres puntos (`derivative_three_points_border(funcion, x0, h)`)

Calcula la derivada de una función en un punto extremo, utilizando la **fórmula del extremo de tres puntos**. Este método se emplea cuando el punto a evaluar está en el borde del intervalo.

### Fórmula

`f'(x0) = (-3 * f(x0) + 4 * f(x0 + h) - f(x0 + 2 * h)) / (2 * h)`

### Parámetros de Entrada y Salida

```python
def derivative_three_points_border(funcion, x0, h):
    """   
    Parámetros:
        funcion: función a derivar
        x0: punto en el extremo 
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
    """
```

### Ejemplo de uso

```python
funcion = "sin(x)"  
x0 = 0.0
h = 1e-5
derivada = derivative_three_points_border(funcion, x0, h)
print("La derivada aproximada de sin(x) en x=0 es:", derivada)
```

## 3. Punto medio de cinco puntos (`derivative_five_points_central(funcion, x0, h)`)

Calcula la derivada de una función en el punto `x0` utilizando la **fórmula del punto medio de cinco puntos**.

### Fórmula

`f'(x0) = (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12 * h)`

### Parámetros de Entrada y Salida

```python
def derivative_five_points_central(funcion, x0, h):
    """        
    Parámetros:
        funcion: función a derivar
        x0: punto en el que se calcula la derivada
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
    """
```

### Ejemplo de uso

```python
funcion = "cos(x)"  
x0 = math.pi / 3
h = 1e-5
derivada = derivative_five_points_central(funcion, x0, h)
print("La derivada aproximada de cos(x) en x=pi/3 es:", derivada)
```

## 4. Extremo de cinco puntos (`derivative_five_points_border(funcion, x0, h)`)

Calcula la derivada de una función en un punto extremo utilizando la **fórmula del extremo de cinco puntos** . Este método se emplea cuando el punto a evaluar está en el borde del intervalo.

### Fórmula

`f'(x0) = (-25 * f(x0) + 48 * f(x0 + h) - 36 * f(x0 + 2 * h) + 16 * f(x0 + 3 * h) - 3 * f(x0 + 4 * h)) / (12 * h)`

### Parámetros de Entrada y Salida

```python
def derivative_five_points_border(funcion, x0, h):
    """        
    Parámetros:
        funcion: función a derivar
        x0: punto en el extremo
        h: tamaño del paso
        
    Retorna:
        Aproximación de f'(x)
    """
```

### Ejemplo de uso

```python
funcion = "exp(x)"  
x0 = 0.0
h = 1e-5
derivada = derivative_five_points_border(funcion, x0, h)
print("La derivada aproximada de exp(x) en x=0 es:", derivada)
```

## 5. Derivadas unificadas respecto a los puntos dados (`derivative_unified(datos, x0)`)

### Proceso

Calcula la derivada numérica en el punto `x0` a partir de un conjunto de puntos dados en un diccionario `{x: f(x)}`. Este método selecciona automáticamente la fórmula adecuada según:
- Si hay al menos 5 puntos y `x0` tiene dos vecinos a cada lado, se utiliza la **fórmula del punto medio de cinco puntos**.
- Si `x0` es el primer elemento:
  - Usa la **fórmula forward de tres puntos** si hay menos de 5 puntos.
  - Si hay al menos 5 puntos, utiliza la **fórmula forward de cinco puntos**.
- Si `x0` es el último elemento:
  - Usa la **fórmula backward de tres puntos** si hay menos de 5 puntos.
  - Si hay al menos 5 puntos, utiliza la **fórmula backward de cinco puntos**.
- En otro caso, se usa la **fórmula del punto medio de tres puntos**.

Este método asume que los datos están equidistantes.

### Parámetros de Entrada y Salida

```python
def derivative_unified(datos, x0):
    """ 
    Parámetros:
        datos: Diccionario con los pares {x: f(x)}.
        x0: El valor de x en el que se quiere estimar la derivada.
    
    Retorna:
        Aproximación de la derivada f'(x0).
    """
```

### Ejemplo de uso

```python
datos = {
    1.0: 1.0,   
    2.0: 4.0,   
    3.0: 9.0,   
    4.0: 16.0,  
    5.0: 25.0   
}
x0 = 3.0
derivada = derivative_unified(datos, x0)
print("La derivada unificada en x=3.0 es:", derivada)
```

## 6. Punto medio de la segunda derivada (`second_derivative_central(funcion, x0, h)`)

Calcula una aproximación de la segunda derivada de una función en el punto `x0` utilizando la **fórmula del punto medio de la segunda derivada**. 

### Fórmula

`f''(x0) = (f(x0 - h) - 2 * f(x0) + f(x0 + h)) / (h**2)`

### Parámetros de Entrada y Salida

```python
def second_derivative_central(funcion, x0, h):
    """   
    Parámetros:
        funcion: función a derivar
        x0: punto en el que se calcula la segunda derivada
        h: tamaño del paso
            
    Retorna:
        Aproximación de la segunda derivada f''(x).
    """
```

### Ejemplo de uso

```python
funcion = "x^2"  
x0 = 2.0
h = 0.001
seg_deriv = second_derivative_central(funcion, x0, h)
print("La segunda derivada de x^2 en x=2.0 es:", seg_deriv)
```

---

## 7. Punto medio de la segunda derivada respecto a los puntos dados (`second_derivative_central_data(datos, x0)`)

Calcula la aproximación de la segunda derivada en un punto `x0` a partir de un conjunto de puntos dados en un diccionario `{x: f(x)}`. Se utiliza la **fórmula del punto medio de la segunda derivada**, asumiendo que los datos están equidistantes y que `x0` cuenta con un vecino a ambos lados.

### Parámetros de Entrada y Salida

```python
def second_derivative_central_data(datos, x0):
    """   
    Parámetros:
        datos: Diccionario con los pares {x: f(x)}.
        x0: El valor de x en el que se quiere estimar la derivada.
            
    Retorna:
        Aproximación de la segunda derivada f''(x0).
    """
```

### Ejemplo de uso

```python
datos = {
    1.9: 3.61,
    2.0: 4.00,
    2.1: 4.41
}
x0 = 2.0
seg_deriv_data = second_derivative_central_data(datos, x0)
print("La segunda derivada a partir de datos en x=2.0 es:", seg_deriv_data)
```

## 8. Fórmulas de Newton-Cotes Cerradas

## 8.1. n=1: Regla Trapezoidal (`newton_cotes_n1_close(funcion, a, b)`)

La **Regla del Trapecio** aproxima la integral de una función en el intervalo `[a, b]` interpolando la función por una línea recta que conecta los extremos.

### Fórmula

`I = (h / 2) * (f(a) + f(b))`

donde 

`h = b - a`

### Parámetros de Entrada y Salida

```python
def trapezoidal_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "2x+1"
a = 0
b = 2

resultado = trapezoidal_rule(funcion, a, b)
print("Resultado Regla Trapezoidal:", resultado)
```

## 8.2. n=2: Regla de Simpson (`newton_cotes_n2_close(funcion, a, b)`)

La **Regla de Simpson** aproxima la integral mediante la interpolación de la función con un polinomio de segundo grado (una parábola) utilizando tres puntos equidistantes: `x0 = a`, `x1 = a+h` y `x2 = b`.

### Fórmula

`I = (h / 3) * (f(a) + 4 * f(a + h) + f(b))`

donde 

`h = (b - a) / 2`

### Parámetros de Entrada y Salida

```python
def simpson_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "x^2"
a = 0
b = 1

resultado = simpson_rule(funcion, a, b)
print("Resultado Regla de Simpson:", resultado)
```

## 8.3. n=3: Regla de Simpson 3/8 (`newton_cotes_n3_close(funcion, a, b)`)

La **Regla de Simpson 3/8** aproxima la integral de la función utilizando la interpolación con un polinomio de tercer grado sobre cuatro puntos igualmente espaciados: `x0 = a`, `x1 = a+h`, `x2 = a+2*h` y `x3 = b`.

### Fórmula

`I = (3 * h / 8) * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))`

donde 

`h = (b - a) / 3`

### Parámetros de Entrada y Salida

```python
def simpson_38_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "x^3"
a = 0
b = 1

resultado = simpson_38_rule(funcion, a, b)
print("Resultado Regla de Simpson 3/8:", resultado)
```

## 8.4. n=4 (`newton_cotes_n4_close(funcion, a, b)`)

La regla **n=4** es un método de Newton–Cotes que evalúa la función en cinco puntos igualmente espaciados: `x0 = a`, `x1 = a+h`, `x2 = a+2*h`, `x3 = a+3*h` y `x4 = b`.

### Fórmula

`I = (2 * h / 45) * (7 * f(a) + 32 * f(a + h) + 12 * f(a + 2 * h) + 32 * f(a + 3 * h) + 7 * f(b))`

donde 

`h = (b - a) / 4`

### Parámetros de Entrada y Salida

```python
def n4_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "x^4"
a = 0
b = 2

resultado = n4_rule(funcion, a, b)
print("Resultado Regla de Boole (n=4):", resultado)
```

## 9. Fórmulas de Newton-Cotes Abiertas

## 9.1. n=0: Regla del Punto Medio (`newton_cotes_n0_open(funcion, a, b)`)

Este método aproxima la integral de la función mediante la evaluación en el punto medio del intervalo, dado un intervalo `[a, b]` 

### Fórmula

`I = 2 * h * f(x0)`

donde 

`h = (b - a) / 2.0`

y los puntos son: 

    x0 = a + h

### Parámetros de Entrada y Salida

```python
def midpoint_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración ⇒ longitud total = 2h.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "sin(x)"
a = 2
b = 6

resultado = midpoint_rule(funcion, a, b)
print("Integral aproximada (n=0):", resultado)
```

## 9.2. n=1 (`newton_cotes_n1_open(funcion, a, b)`)

En esta regla se utiliza dos puntos interiores del intervalo `[a, b]` 

### Fórmula

`I = (3.0 * h / 2.0) * (f(x0) + f(x1))`

donde 

`h = (b - a) / 3.0`

y los puntos son: 

    x0 = a + h
    x1 = x0 + h

### Parámetros de Entrada y Salida

```python
def n1_open_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración ⇒ longitud total = 3h.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "x+1"
a = 1
b = 4

resultado = n1_open_rule(funcion, a, b)
print("Integral aproximada (n=1):", resultado)
```

## 9.3. n=2 (`newton_cotes_n2_open(funcion, a, b)`)

Esta regla utiliza tres puntos interiores del intervalo `[a, b]` 

### Fórmula

`I = (4.0 * h / 3.0) * (2.0 * f(x0) - f(x1) + 2.0 * f(x2))`

donde 

`h = (b - a) / 4.0`

y los puntos son: 

    x0 = a + h
    x1 = x0 + h
    x2 = x1 + h

### Parámetros de Entrada y Salida

```python
def n2_open_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración ⇒ longitud total = 4h.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "x^2"
a = 0
b = 4

resultado = n2_open_rule(funcion, a, b)
print("Integral aproximada (n=2):", resultado)
```

## 9.4. n=3 (`newton_cotes_n3_open(funcion, a, b)`)

Esta regla utiliza cuatro puntos interiores del intervalo `[a, b]` 

### Fórmula

`I = (5.0 * h / 24.0) * (11.0 * f(x0) + f(x1) + f(x2) + 11.0 * f(x3))`

donde 

`h = (b - a) / 5.0`

y los puntos son: 

    x0 = a + h
    x1 = x0 + h
    x2 = x1 + h
    x3 = x2 + h

### Parámetros de Entrada y Salida

```python
def n3_open_rule(funcion, a, b):
    """
    Parámetros:
      funcion: función a integrar.
      a, b: extremos del intervalo de integración ⇒ longitud total = 5h.
    
    Devuelve:
      Aproximación de la integral.
    """
```

### Ejemplo de Uso

```python
funcion = "x^3"
a = 0
b = 5

resultado = n3_open_rule(funcion, a, b)
print("Integral aproximada (n=3):", resultado)
```

## 10. Regla de Simpson Compuesta (`composite_simpson_rule(funcion, a, b, n)`)

Aproxima la integral definida de una función `f(x)` en el intervalo `[a,b]` utilizando la **regla compuesta de Simpson**, que interpola la función mediante parábolas en pares de subintervalos para aumentar la precisión.

### Fórmula

`I = (h / 3.0) * (f(a)  + 2.0 * sum_even + 4.0 * sum_odd + f(b))`

donde 

`h = (b - a) / n`

y `n` es el número de subintervalos (debe ser par).

### Parámetros de Entrada y Salida

```python
def composite_simpson_rule(funcion, a, b, n):
    """
    Parámetros:
      funcion: Cadena que representa la función.
      a, b: Extremos del intervalo de integración.
      n: Número de subintervalos (entero positivo, debe ser par).

    Devuelve:
      Aproximación numérica de la integral de f(x) en [a,b].
    """
```

### Ejemplo de uso

```python
funcion = "sin(x)"
a = 0
b = math.pi
n = 100

resultado = composite_simpson_rule(funcion, a, b, n)
print(resultado)
```

## 11. Regla Trapezoidal Compuesta (`composite_trapezoidal_rule(funcion, a, b, n)`)

Aproxima la integral definida de una función `f(x)` en el intervalo `[a,b]` mediante la **regla trapezoidal compuesta**, que aproxima el área bajo la curva con trapezoides en cada subintervalo.

### Fórmula

`I = (h / 2.0) * (f(a) + 2.0 * suma_interiores + f(b))`

donde 

`h = (b - a) / n`

### Parámetros de Entrada y Salida

```python
def composite_trapezoidal_rule(funcion, a, b, n):
    """
    Parámetros:
      funcion : Cadena que representa la función a integrar,.
      a, b : Extremos del intervalo de integración.
      n : Número de subintervalos (entero positivo).

    Devuelve:
      Aproximación numérica de la integral de f(x) en [a, b].
    """
```

### Ejemplo de uso

```python
funcion = "sin(x)"
a = 0
b = math.pi
n = 100

resultado = composite_trapezoidal_rule(funcion, a, b, n)
print(resultado) 
```

## 12. Regla del Punto Medio Compuesta (`composite_midpoint_rule(funcion, a, b, n)`)

Aproxima la integral definida de una función `f(x)` en el intervalo `[a,b]` usando la **regla del punto medio compuesta**, que evalúa la función en los puntos medios de pares de subintervalos.

### Fórmula

`I = 2.0 * h * suma_mid`

donde 

`h = (b - a) / n`

y `n` es par.

### Parámetros de Entrada y Salida

```python
def composite_midpoint_rule(funcion, a, b, n):
    """
    Parámetros:
      funcion : Cadena que representa la función a integrar.
      a, b : Extremos del intervalo de integración.
      n : Número de subintervalos (entero positivo y par).

    Devuelve:
      Aproximación numérica de la integral de f(x) en [a, b].
    """
```

### Ejemplo de uso

```python
funcion = "sin(x)"
a = 0
b = math.pi
n = 10

resultado = composite_midpoint_rule(funcion, a, b, n)
print(resultado) 
```
