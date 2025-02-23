# Documentación Módulo Ecuaciones de una Variable

## 1- Método de Bisección (`bisection(f, a, b, TOL, N0)`)

El **método de bisección** es un método numérico para encontrar la raíz de una función continua. Se basa en el **teorema del valor intermedio**, el cual establece que si una función f(x) es continua en un intervalo [a, b] y f(a) y f(b) tienen signos opuestos, entonces existe al menos un punto c en [a, b] tal que f(c) = 0 .

### Proceso del Método

1. **Verificación de la condición inicial:**  
   Se comprueba que f(a) y f(b) tengan signos opuestos, es decir, que f(a) X f(b) < 0.

2. **Inicialización:**  
   Se inicializa el contador en 1 y se evalúa FA = f(a).

3. **Iteración:**  
   En cada iteración se calcula el punto medio y se evalúa FP = f(p).  
   Si FP es 0 o si la mitad del ancho del intervalo (b-a)/2 es menor que la tolerancia, se retorna p junto con el número de iteraciones.

4. **Actualización del Intervalo:**  
   Se incrementa i y se decide:
   - Si FA y FP tienen signos opuestos, la raíz se encuentra en [𝑎,p] por lo que se actualiza b = p.
   - De lo contrario, la raíz se encuentra en [p,𝑏] por lo que se actualiza a = p y FA = FP.

5. **Fallo:**  
   Si se alcanzan N0 iteraciones sin convergencia, se lanza un error.

### Explicación del Código de la Función

```python
    """
    Realiza el método de bisección para encontrar una raíz de la función f en el intervalo [a, b].

    Entradas:
      a, b     : Puntos finales del intervalo en el que se busca la raíz.
      TOL      : Tolerancia para la aproximación de la raíz.
      N0       : Número máximo de iteraciones permitidas.

    Salida:
      Retorna una tupla (p, i) donde:
         - p es la aproximación a la raíz.
         - i es el número de iteraciones realizadas.

      Si f(a) y f(b) no tienen signos opuestos o si el método no converge en N0 iteraciones,
      se lanza un ValueError con un mensaje de error.
    """
```
### Ejemplo de Uso
Supongamos que queremos encontrar la raíz de la función 𝑓(𝑥)=𝑥**2−4 en el intervalo [0,3]. Para ello, definimos la función y llamamos a bisection_method:

```python
# Definición de la función a analizar
def f(x):
    return x**2 - 4

# Llamada al método de bisección en el intervalo [0, 3]
raiz, iteraciones = bisection_method(f, 0, 3)

print(f"La raíz aproximada es {raiz} encontrada en {iteraciones} iteraciones.")
```

## 2- Método de Iteración de Punto Fijo (`fixed_point_iteration(g, p0, TOL, N0)`)

El **método de iteración de punto fijo** es un método numérico para encontrar una solución a la ecuación p = g(p). La idea es partir de una aproximación inicial p_0 y generar una sucesión definida por `p_{i+1} = g(p_i)`.

Si la función g(p) es contractiva en la región cercana al punto fijo, la sucesión converge a un valor p tal que p = g(p).

### Proceso del Método

**Paso 1:**   
  Se inicializa el contador de iteraciones.

- **Paso 2:**  
  Se inicia un bucle que se ejecuta mientras el número de iteraciones no supere N0.

- **Paso 3:**  
  Se calcula el siguiente valor p aplicando la función g a la aproximación actual p0.

- **Paso 4:**   
  Se verifica si la diferencia entre la nueva aproximación y la anterior es menor que la tolerancia. Si es así, se retorna p y el número de iteraciones y se termina la ejecución.

- **Paso 5:**   
  Se incrementa el contador de iteraciones.

- **Paso 6:**  
  Se actualiza p0 con el valor de p para la siguiente iteración.

- **Paso 7:**  
  Si se sale del bucle sin convergencia, se lanza un `ValueError` indicando que el método falló tras N0 iteraciones.

### Explicación del Código de la Función

```python
    """
    Realiza el método de iteración de punto fijo para encontrar una solución de p = g(p).
    
    Entradas:
      g   : función (callable) que define el método de punto fijo, es decir, g(p).
      p0  : aproximación inicial.
      TOL : tolerancia para la convergencia.
      N0  : número máximo de iteraciones permitidas.
    
    Salida:
      Retorna una tupla (p, i) donde:
         - p es la aproximación a la solución.
         - i es el número de iteraciones realizadas.
         
      Si el método no converge en N0 iteraciones, se lanza un ValueError con un mensaje de falla.
    
    Pseudocódigo:
      Paso 1: Determine i = 1.
      Paso 2: Mientras i ≤ N0, haga los pasos 3–6.
      Paso 3: Determine p = g(p0). (Calcule p_i)
      Paso 4: Si |p - p0| < TOL entonces
                 SALIDA(p) y termine.
      Paso 5: Determine i = i + 1.
      Paso 6: Determine p0 = p. (Actualizar p0)
      Paso 7: SALIDA("El método falló después de N0 iteraciones")
    """
   ```

### Ejemplo de Uso
Definimos la función g(p) para el problema: p = cos(p)

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
El Método de Newton es un procedimiento iterativo para encontrar soluciones aproximadas de la ecuación f(x)=0. Se parte de una aproximación inicial p0 y se va mejorando dicha aproximación usando la fórmula `p = p0 - f′(p0)/f(p0)`

### Proceso del Método

1. **Inicialización:**  
   Se elige una aproximación inicial p_0 para la raíz de la función f(x)=0, se establece el contador de iteraciones en 1 y llamamos al metodo privado `_derivative` para calcular la derivada de la función.

2. **Iteración:**  
   En cada iteración se realiza lo siguiente:
   - **Cálculo de la nueva aproximación:**  
     Se calcula:
     `p= p0 − f′(p0)/f(p0)`, en nuestro caso `p = p0 - f_val / df_val`
     df_val se obtiene numéricamente mediante el método de diferencia centrada.
   - **Evaluación del cambio:**  
     Se calcula la diferencia para evaluar el progreso de la iteración.

3. **Criterio de Convergencia:**  
   Si la diferencia es menor que la tolerancia predefinida, se considera que la iteración ha convergido y se retorna la solución aproximada (p) junto con el número de iteraciones (i).

4. **Actualización:**  
   Si la condición de convergencia no se cumple, se incrementa el contador en 1 y se actualiza p_0 con el valor de p para la siguiente iteración.

5. **Fallo:**  
   Si se alcanza el número máximo de iteraciones sin convergencia, se lanza un error.


### Explicación del Código de la Función

   ```python
   """
      Aplica el Método de Newton para encontrar una solución aproximada de f(x)=0, 
      calculando numéricamente la derivada de f.

      Entradas:
         f   : función (callable) para la cual se busca la raíz, f(x)=0.
         p0  : aproximación inicial.
         TOL : tolerancia para la convergencia.
         N0  : número máximo de iteraciones permitidas.
         h   : paso utilizado para calcular la derivada numérica (por defecto 1e-5).

      Salida:
         Retorna una tupla (p, i) donde:
            - p es la aproximación a la raíz.
            - i es el número de iteraciones realizadas.

         Si el método no converge en N0 iteraciones, se lanza un ValueError.
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





## Adicional

### Método para derivar `(_derivative(f, TOL=1e-5))`
Metodo que retorna una función que aproxima la derivada de f utilizando la fórmula de diferencia centrada.

**Parámetros**:
   - **f** : Función (callable) de la cual se quiere calcular la derivada.
   - **TOL** : Paso pequeño para la aproximación (por defecto 1e-5).