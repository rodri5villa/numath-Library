# Documentación Módulo Ecuaciones de una Variable

## 1- Método de Bisección (`bisection(f, a, b, tol, max_iter)`)

El **método de bisección** es un método numérico para encontrar la raíz de una función continua. Se basa en el **teorema del valor intermedio**, el cual establece que si una función f(x) es continua en un intervalo [a, b] y f(a) y f(b) tienen signos opuestos, entonces existe al menos un punto c en [a, b] tal que f(c) = 0 .

### Proceso del Método

1. **Verificación de la condición inicial:**  
   Se comprueba que f(a) y f(b) tengan signos opuestos, es decir, que f(a) X f(b) < 0.

2. **Cálculo del punto medio:**  
   Se calcula el punto medio c = {a + b} / {2} y se evalúa f(c).

3. **Criterio de parada:**  
   Si |f(c)| es menor que una tolerancia predefinida (o si el ancho del intervalo es muy pequeño), se acepta c como una aproximación de la raíz.

4. **Selección del subintervalo:**  
   Dependiendo del signo de f(c), se selecciona el subintervalo [a, c] o [c, b] para continuar la búsqueda.

    - Si 𝑓(𝑎) y 𝑓(𝑐) tienen signos opuestos, la raíz se encuentra en [𝑎,𝑐] de lo contrario, está en [𝑐,𝑏].

5. **Iteración:**  
   Se repite el proceso hasta alcanzar la tolerancia o un número máximo de iteraciones.

### Explicación del Código de la Función

```python
    """
    Aplica el método de bisección para encontrar una raíz de la función f en el intervalo [a, b].

    Parámetros:
      f        : función continua (callable) para la cual se busca la raíz.
      a, b     : extremos del intervalo inicial en el que f(a) y f(b) deben tener signos opuestos.
      tol      : tolerancia para la aproximación de la raíz (error aceptable).
      max_iter : número máximo de iteraciones permitidas.

    Retorna:
      Una tupla (c, i) donde:
         - c es la aproximación de la raíz.
         - i es el número de iteraciones realizadas.

    Lanza:
      ValueError si f(a) y f(b) no tienen signos opuestos.
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