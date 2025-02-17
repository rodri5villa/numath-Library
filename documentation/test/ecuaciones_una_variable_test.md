# Documentación General de Tests del Módulo Ecuaciones de una Variable

## 1- Método de Bisección

Se han diseñado pruebas para garantizar tanto la correcta ejecución de la función en condiciones válidas como para confirmar que se gestionan adecuadamente los casos en los que la entrada no es válida.

### 1. Test de Funcionalidad (`test_bisection_correct`)

  - Se define una función matemática para la cual se conoce la raíz en un determinado intervalo.
  - Se invoca el método de bisección con parámetros como el intervalo, una tolerancia y un máximo de iteraciones.
  - Se utiliza `pytest.approx` para comparar la raíz calculada con el valor esperado, permitiendo un margen de error relativo.
  - El mensaje del assert proporciona información adicional en caso de fallo, mostrando la raíz obtenida y las iteraciones realizadas.

### 2. Test de Excepción (`test_bisection_error`)
 
  - Se define cualquier función de la cual se sabe que, para el intervalo dado, los extremos no tienen signos opuestos.
  - Se utiliza el contexto `pytest.raises(ValueError)` para indicar que, al invocar el método con un intervalo no válido, se espera que se produzca un error.
  - Este test garantiza que el método no continúa su ejecución en condiciones erróneas.
