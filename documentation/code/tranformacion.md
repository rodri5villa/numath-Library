# Documentación de la clase Transformación

Esta clase convierte cadenas de texto que representan funciones matemáticas en _callables_ de Python (funciones lambda), permitiendo escribir expresiones como `x^2-3x`, `y**2` o `x*y+1` sin sintaxis estricta. El módulo se encarga de transformar esas cadenas en funciones evaluables.

> **IMPORTANTE:**
> - Ahora **se soportan variables** `x`, `y`, o ambas simultáneamente. La firma de la lambda resultante se adapta al conjunto de variables detectadas en la expresión.
> - Si no se detectan ni `x` ni `y`, se asume por defecto la variable `x`.
> - Para usar más variables o librerías (p.ej. `numpy`), hay que añadirlas al entorno de `eval` y ajustar el reemplazo.

## Funciones del módulo

### `reemplazar_funciones(funcion_entrada)`

Transforma la cadena de entrada:
- **Reemplazos básicos:**
  - `sin(` → `math.sin(`, `cos(` → `math.cos(`, `^` → `**`, `pi` → `math.pi`, etc.
- **Multiplicación implícita:**
  Inserta `*` en `3x` → `3*x`, `2sin(x)` → `2*math.sin(x)` o `xy` → `x*y`.

```python
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
        'sqrt(': 'math.sqrt(',
        '^': '**',
        'pow(': 'math.pow(',
        'pi': 'math.pi'
    }

funcion_python = reemplazar_funciones("3x^2 + sin(x)")  # "3*x**2 + math.sin(x)"
```

### `crear_funcion(funcion_entrada)`

Construye una función lambda de Python con firma adecuada según las variables en la expresión.

1. **Transformación:** Convierte la notación amigable a Python válido mediante `reemplazar_funciones()`.
2. **Detección de variables:** Busca `x` o `y` en la expresión transformada. Si aparecen ambas, crea `lambda x, y: …`; si solo una, `lambda x: …` o `lambda y: …`.
3. **Evaluación segura:** Usa `eval` con entorno limitado a `{ 'math': math }`.

```python
f1 = crear_funcion('sin(x)')        # lambda x: math.sin(x)
f2 = crear_funcion('y^2')         # lambda y: y**2
f3 = crear_funcion('xy + 2')      # lambda x,y: x*y + 2
```

> **Nota:** Si necesitas más variables (p.ej. `z`) o librerías (p.ej. `np`), adapta la detección y pasa el entorno a `eval`:
 ```python
  def crear_funcion(..., entorno={'math': math, 'np': np}):
    ...
    func = eval(code, entorno)
 ```

## Seguridad y extensibilidad

- El entorno de `eval` se restringe a evitar ejecución de código arbitrario.
- Para añadir nuevas funciones o constantes, amplía `partes_a_reemplazar`.
- La detección de variables se basa en expresiones regulares sencillas; para casos complejos revisa la cadena previa.

---

## Ejemplo completo de uso

```python
from mi_libreria.utils import crear_funcion

# Función de una variable
f = crear_funcion('x^3 - 3x + 1')
print(f(2))  # 2**3 - 3*2 + 1 = 3

# Función de y
g = crear_funcion('y/2 + 1')
print(g(4))  # 4/2 + 1 = 3

# Función de dos variables
h = crear_funcion('x*y + sin(x)')
print(h(2, math.pi))  # 2*math.pi + math.sin(2) ≈ 7.1924827339
```
