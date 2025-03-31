# Documentación de la clase Transformación

Esta clase permite transformar cadenas de texto que representan funciones matemáticas en una función _callable_ de Python (una función lambda). La idea es que el usuario pueda escribir expresiones como por ejemplo, `x^2-3x`, sin necesidad de usar la sintaxis estricta de Python, y que el módulo se encargue de convertirlas en una función que se pueda evaluar numéricamente.

 **IMPORTANTE:**  
 - Actualmente, solo se permite utilizar la variable `x` para definir la función. Esto se debe a que la conversión y los reemplazos definidos en `eval` están orientados exclusivamente a la variable `x`. 

- Si se desean utilizar otras librerías o funciones adicionales, será necesario añadirlas explícitamente en el entorno seguro (scope) definido en `eval`.

## Funciones del Módulo

### `reemplazar_funciones(funcion_entrada)`

Esta función transforma la cadena de entrada reemplazando funciones y operadores por sus equivalentes en Python, y corrigiendo la omisión del operador de multiplicación.

- **Reemplazos básicos:**  
  Se sustituyen funciones y constantes escritas en notación "amigable" por sus equivalentes en Python. Por ejemplo:
  - `sen(` se reemplaza por `math.sin(`  
  - `acos(` se reemplaza por `math.acos(`  
  - `^` se reemplaza por `**`  
  - `pi` se reemplaza por `math.pi`

- **Inserción de Multiplicación Implícita:**  
  Utiliza expresiones regulares para insertar el operador de multiplicación `*` en casos donde se omite, como en `3x` (convertido a `3*x`) o `2sin(x)` (convertido a `2*math.sin(x)`).

### `crear_funcion(funcion_entrada)`

Esta función toma una cadena que representa una función en notación "amigable" y devuelve una función lambda de Python que se puede evaluar. Utiliza internamente `reemplazar_funciones` para convertir la cadena a una expresión válida.

- **Transformación:**  
  Convierte la notación amigable a una sintaxis compatible con Python.

- **Evaluación Segura:**  
  Se utiliza `eval` para construir la función lambda, restringiendo el entorno a solo tener acceso al módulo `math` y, por tanto, reduciendo el riesgo de ejecutar código malicioso.

- **Uso Exclusivo de la Variable `x`:**  
  La función lambda se crea asumiendo que la variable independiente es `x`. Esto significa que si se desea usar otra variable o incluir otras librerías, habrá que modificar la función y actualizar el entorno de `eval`.

## Consideraciones de Seguridad y Extensibilidad

- **Restricción del Entorno (`eval`):**  

  El entorno de `eval` se limita a `{ "math": math }` para garantizar que solo se tengan disponibles las funciones y constantes del módulo `math`.  
  **Si se desea utilizar otra librería** (por ejemplo, `numpy` o alguna función personalizada), es necesario añadirla explícitamente al diccionario.  
  ```python
  funcion = eval("lambda x: " + funcion_transformada, {"math": math, "np": np})
  ```

- **Uso Exclusivo de la Variable `x`:**  

  Actualmente, el transformador está diseñado para trabajar con la variable `x`. Si el usuario introduce otra variable (por ejemplo, `y`), la transformación no funcionará correctamente, ya que el diccionario y la construcción de la lambda asumen que la única variable es `x`. 
  **Si se quisiera añadir otra variable**, habría que modificar la construcción de la lambda:
    ```python
    funcion = eval("lambda x, y: " + funcion_transformada, {"math": math})
    ```

- **Extensión del Diccionario de Reemplazos:**  

  Para incluir más funciones o soportar notación de LaTeX, se pueden agregar nuevos elementos al diccionario `partes_a_reemplazar`. 
---

## Ejemplo de Uso

```python
if __name__ == "__main__":
    # El usuario ingresa la función en notación amigable
    funcion_usuario = "x^2-3x"
    
    # Crear la función lambda a partir de la cadena
    f = crear_funcion(funcion_usuario)
    
    # Probar la función para algunos valores
    for valor in [0, 1, 2]:
        print(f"f({valor}) = {f(valor)}")
    
    # Salida esperada:
    # f(0) = 0
    # f(1) = -2
    # f(2) = -2
```