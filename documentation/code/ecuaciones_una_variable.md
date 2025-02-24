# Documentación Módulo Ecuaciones de una Variable

## 1- Método de Bisección (`bisection(f, a, b, TOL, N0)`)

El **método de bisección** es un método numérico para encontrar la raíz de una función continua. Se basa en el **teorema del valor intermedio**, el cual establece que si una función `f(x)` es continua en un intervalo `[a, b]` y `f(a)` y `f(b)` tienen signos opuestos, entonces existe al menos un punto c en `[a, b]` tal que `f(c) = 0`.

### Proceso del Método

1. **Verificación de la condición inicial:**  
   Se comprueba que `f(a)` y `f(b)` tengan signos opuestos, es decir, que `f(a) * f(b) < 0`.

2. **Inicialización:**  
   Se inicializa el contador en 1 y se evalúa `FA = f(a)`.

3. **Iteración:**  
   En cada iteración se calcula el punto medio y se evalúa `FP = f(p)`.  
   Si `FP` es 0 o si la mitad del ancho del intervalo (b-a)/2 es menor que la tolerancia, se retorna `p` junto con el número de iteraciones.

4. **Actualización del Intervalo:**  
   Se incrementa i y se decide:
   - Si `FA` y `FP` tienen signos opuestos, la raíz se encuentra en `[𝑎,p]` por lo que se actualiza `b = p`.
   - De lo contrario, la raíz se encuentra en `[p,𝑏]` por lo que se actualiza `a = p` y `FA = FP`.

5. **Fallo:**  
   Si se alcanzan `N0` iteraciones sin convergencia, se lanza un error.

### Parametros de Entrada y Salida
```python
def bisection(f, a, b, TOL=1e-5, N0=100):
    """
    Entradas:
      f        : función (callable)
      a, b     : Puntos finales del intervalo en el que se busca la raíz.
      TOL      : Tolerancia para la aproximación de la raíz.
      N0       : Número máximo de iteraciones permitidas.

    Salida:
      Retorna una tupla (p, i) donde:
         - p es la aproximación a la raíz.
         - i es el número de iteraciones realizadas.
    """
```
### Ejemplo de Uso
Supongamos que queremos encontrar la raíz de la función `𝑓(𝑥)=𝑥**2−4` en el intervalo `[0,3]`. Para ello, definimos la función y llamamos a bisection_method:

```python
# Definición de la función a analizar
def f(x):
    return x**2 - 4

# Llamada al método de bisección en el intervalo [0, 3]
raiz, iteraciones = bisection_method(f, 0, 3)

print(f"La raíz aproximada es {raiz} encontrada en {iteraciones} iteraciones.")
```

## 2- Método de Iteración de Punto Fijo (`fixed_point_iteration(g, p0, TOL, N0)`)

El **método de iteración de punto fijo** es un método numérico para encontrar una solución a la ecuación `p = g(p)`. La idea es partir de una aproximación inicial y generar una sucesión definida por `p{i+1} = g(pi)`.

Si la función `g(p)` es contractiva en la región cercana al punto fijo, la sucesión converge a un valor `p` tal que `p = g(p)`.

### Proceso del Método

**Inicialización:**   
  Se inicializa el contador de iteraciones y se inicia un bucle que se ejecuta mientras el número de iteraciones no supere `N0`.

- **Proceso:**  
  Se calcula el siguiente valor `p` aplicando la función `g` a la aproximación actual `p0`.  
  Se verifica si la diferencia entre la nueva aproximación y la anterior es menor que la tolerancia. Si es así, se retorna `p` y el número de iteraciones y se termina la ejecución.

- **Iteración:**   
  Se incrementa el contador de iteraciones.
  Se actualiza `p0` con el valor de `p` para la siguiente iteración.

- **Fallo:**  
  Si se sale del bucle sin convergencia, se lanza un `ValueError` indicando que el método falló tras `N0` iteraciones.

### Parametros de Entrada y Salida

```python
def fixed_point_iteration(g, p0, TOL=1e-5, N0=100):
    """
    Entradas:
      g   : función (callable) que define el método de punto fijo, es decir, g(p).
      p0  : aproximación inicial.
      TOL : tolerancia para la convergencia.
      N0  : número máximo de iteraciones permitidas.
    
    Salida:
      Retorna una tupla (p, i) donde:
         - p es la aproximación a la solución.
         - i es el número de iteraciones realizadas.
    """
   ```

### Ejemplo de Uso
Definimos la función `g(p)` para el problema: `p = cos(p)`

   ```python
   def g(p):
        return math.cos(p)

    # Aproximación inicial
    p0 = 1.0

    try:
        solution, iterations = fixed_point_iteration(g, p0, TOL=1e-5, N0=100)
        print(f"La solución encontrada es {solution} en {iterations} iteraciones.")
    except ValueError as e:
        print(e)
   ```
## 3- Método de Newton (`newton_method(f, p0, TOL=1e-5, N0=100, factor=1e-8)`)

El Método de Newton es un procedimiento iterativo para encontrar soluciones aproximadas de la ecuación `f(x)=0`. Se parte de una aproximación inicial y se va mejorando dicha aproximación usando la fórmula `p = p0 - f(p0)/f′(p0)`

### Proceso del Método

1. **Inicialización:**  
   Se elige una aproximación inicial para la raíz de la función `f(x)=0`, se establece el contador de iteraciones en 1 y llamamos al metodo privado `_derivative` para calcular la derivada de la función.

2. **Iteración:**  
   En cada iteración se realiza lo siguiente:
   - **Cálculo de la nueva aproximación:**  
     Se calcula:
     `p= p0 − f(p0)/f′(p0)`, en nuestro caso `p = p0 - f_val / df_val`

     `df_val` se obtiene numéricamente mediante el método de diferencia centrada.
   - **Evaluación del cambio:**  
     Se calcula la diferencia para evaluar el progreso de la iteración.

   **`threshold`**:   El umbral se define como `factor * (1 + |p0|)`. Esto permite ajustar el umbral en función de la escala de la aproximación inicial. Si la magnitud de la derivada en `p0` es menor que este umbral, se considera que la derivada es demasiado pequeña, y por tanto no es seguro aplicar el método de Newton.
3. **Criterio de Convergencia:**  
   Si la diferencia es menor que la tolerancia predefinida, se considera que la iteración ha convergido y se retorna la solución aproximada junto con el número de iteraciones.

4. **Actualización:**  
   Si la condición de convergencia no se cumple, se incrementa el contador en 1 y se actualiza `p0` con el valor de `p` para la siguiente iteración.

5. **Fallo:**  
   Si la derivada es demasiado pequeña en `p0` (es decir, menor que el umbral relativo calculado) o si se alcanza el número máximo de iteraciones sin convergencia, se lanza un ValueError indicando que el método de Newton no se puede aplicar o que ha fallado.

### Parametros de Entrada y Salida

```python
def newton_method(f, p0, TOL=1e-5, N0=100, factor=1e-8):
   """
      Entradas:
         f        : función (callable) para la cual se busca la raíz, f(x)=0.
         p0       : aproximación inicial.
         TOL      : tolerancia para la convergencia.
         N0       : número máximo de iteraciones permitidas.
         factor   : factor para calcular el umbral relativo utilizado en la verificación de la derivada.
            
      Salida:
         Retorna una tupla (p, i) donde:
            - p es la aproximación a la raíz.
            - i es el número de iteraciones realizadas.
      """
```

### Ejemplo de Uso
Utilizamos el método de Newton, usando derivación numérica, y elegimos una aproximación inicial razonable.

   ```python

   def f(x):
      return x**3 - 2

   p0 = 1.5  
   solution, iterations = newton_method(f, p0, TOL=1e-5, N0=100, factor=1e-8)
   print(f"La solución encontrada es {solution} en {iterations} iteraciones.")
   ```
## 4- Método de la secante (`secant_method(f, p0, p1, TOL=1e-5, N0=100)`)

El **Método de la Secante** es un método numérico para encontrar una solución aproximada a la ecuación `f(x)=0` sin requerir el cálculo explícito de la derivada. En lugar de usar la derivada, utiliza dos aproximaciones iniciales y calcula la siguiente aproximación mediante la recta secante que une los puntos `(p0, f(p0))` y `(p1, f(p1))`.

### Proceso del Método

1. **Inicialización:**  
   Se disponen dos aproximaciones iniciales `p0` y `p1` y se calcula:
   - `q0 = f(p0)`
   - `q1 = f(p1)`
   Se establece el contador de iteraciones en `i = 2`, ya que ya se conocen dos puntos.

2. **Iteración:**  
   Mientras que la iteración es menor o igual al número máximo de iteraciones, se hacen los siguientes pasos:
   - **Cálculo de la nueva aproximación:**  
     Se calcula: `p = p1 - q1 * (p1 - p0) / (q1 - q0)`
   - **Criterio de Convergencia:**  
     Si `|p - p_1| < TOL`, se retorna `p` junto con el número de iteraciones.
   - **Actualización:**  
     Se actualizan las variables para la siguiente iteración:
     - `p0 <- p1` y `q0 <- q1`
     - `p1 <- p` y `q1 <- f(p)` Se incrementa `i`.

3. **Fallo:**  
   Si se alcanzan `N0` iteraciones sin satisfacer el criterio de convergencia, se lanza un error indicando que el método no fue exitoso.

### Parametros de Entrada y Salida

```python
def secant_method(f, p0, p1, TOL=1e-5, N0=100):
    """
    Entradas:
      f    : función (callable) para la cual se busca la raíz, f(x)=0.
      p0   : primera aproximación inicial.
      p1   : segunda aproximación inicial.
      TOL  : tolerancia para la convergencia.
      N0   : número máximo de iteraciones permitidas.
    
    Salida:
      Retorna una tupla (p, i) donde:
         - p es la aproximación a la raíz.
         - i es el número de iteraciones realizadas.
```

### Ejemplo de Uso

Considera la ecuación `f(x)=x^2-2=0`. La raíz real es `sqrt{2}, approx 1.41421`. Utilizaremos dos aproximaciones iniciales, por ejemplo, `p0=1` y `p1=2`.

```python

def f(x):
    return x**2 - 2

p0 = 1.0
p1 = 2.0

solution, iterations = secant_method(f, p0, p1, TOL=1e-5, N0=100)
print(f"La solución encontrada es {solution} en {iterations} iteraciones.")
```
## 5- Método de Posición Falsa (`false_position(f, p0, p1, TOL=1e-5, N0=100)`)

El **método de la posición falsa** es un método numérico para encontrar una solución aproximada de la ecuación `f(x)=0` cuando la función `f` es continua en el intervalo `[p0, p1]` y `f(p0)` y `f(p1)` tienen signos opuestos. La idea es usar una recta secante (la línea que une los puntos `(p0, f(p0))` y `(p1, f(p1))`) para estimar la raíz.

### Proceso del Método

1. **Inicialización:**
   - Se establecen dos aproximaciones iniciales.
   - Se calculan `q0 = f(p0)` y `q1 = f(p1)`.
   - Se fija el contador `i=2`.

2. **Iteración:**
   - Se calcula una nueva aproximación usando la fórmula de la posición falsa: `p = p1 - q1 * (p1 - p0) / (q1 - q0)`
   - Si `|p - p_1| < TOL`, se considera que el proceso ha convergido y se retorna `p` junto con el número de iteraciones.
   - Se incrementa el contador en 1.
   - Se calcula `q = f(p)`. Luego, se verifica el signo de `q` respecto a `q1`:
     - Si `q * q1 < 0`, se actualiza `p0 = p1` y `q0 = q1`.
   - Se actualiza `p1 = p` y `q1 = q`.
   
3. **Fallo:**
   - Si se alcanza el número máximo de iteraciones `N0` sin convergencia, se lanza un error indicando que el método falló.

### Parametros de Entrada y Salida

```python
def false_position(f, p0, p1, TOL=1e-5, N0=100):
    """
    Entradas:
      f    : función (callable) para la cual se busca la raíz, f(x)=0.
      p0   : primera aproximación inicial.
      p1   : segunda aproximación inicial.
      TOL  : tolerancia para la convergencia.
      N0   : número máximo de iteraciones permitidas.
      
    Salida:
      Retorna una tupla (p, i) donde:
         - p es la aproximación a la raíz.
         - i es el número de iteraciones realizadas.
   """
```

### Diferencia con Metodo de la Secante

Ambos métodos utilizan la idea de aproximar la raíz mediante la intersección de la línea secante que une dos puntos en la gráfica de `f(x)`, pero difieren en cómo actualizan sus aproximaciones:

- **Método de la Secante**  
  - Utiliza los dos últimos puntos calculados (sin mantener necesariamente una condición de bracketing) para generar la nueva aproximación mediante: `p = p1 - q1 * (p1 - p0) / (q1 - q0)`.

  - No garantiza que las aproximaciones encuadren una raíz. Esto puede hacer que la convergencia sea rápida, pero en algunos casos puede perder la garantía de que la raíz se encuentra entre las aproximaciones.

- **Método de la Falsa Posición**  
  - También usa la misma fórmula: `p = p1 - q1 * (p1 - p0) / (q1 - q0)`.  
  - Sin embargo, **mantiene siempre un intervalo `[p0, p1]` donde `f(p0)` y `f(p1)` tienen signos opuestos**. Después de calcular `p`, se decide qué extremo actualizar según el signo de `f(p)`:
    - Si `f(p)` tiene el mismo signo que `f(p1)`, se actualiza `p0` (y se conserva el bracketing).
    - Si `f(p)` tiene el mismo signo que `f(p0)`, se actualiza `p1`.
  - De esta forma, se garantiza que en cada iteración el intervalo sigue conteniendo una raíz.

### Ejemplo de Uso

Consideremos la función `f(x)=x^2-3`, cuya raíz real es `sqrt{3} \approx 1.73205`. Utilizaremos las aproximaciones iniciales `p0=1.0` y `p1=2.0`.

```python

def f(x):
    return x**2 - 3

p0 = 1.0
p1 = 2.0

solution, iterations = false_position(f, p0, p1, TOL=1e-5, N0=100)
print(f"La solución encontrada es {solution} en {iterations} iteraciones.")
```





## Adicional

### Método privado para derivar `(_derivative(f, TOL=1e-5))`
Metodo privado que retorna una función que aproxima la derivada de `f` utilizando la fórmula de diferencia centrada.

**Parámetros**:
   - **f** : Función (callable) de la cual se quiere calcular la derivada.
   - **TOL** : Paso pequeño para la aproximación (por defecto 1e-5).