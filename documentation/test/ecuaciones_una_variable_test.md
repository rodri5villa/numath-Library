# Documentación General de Tests del Módulo Ecuaciones de una Variable

## 1- Método de Bisección

### 1. Test de Funcionalidad (`test_bisection_correct`)

  - Se define una función matemática para la cual se conoce la raíz en un determinado intervalo.
  - Se invoca el método de bisección con parámetros como el intervalo, una tolerancia y un máximo de iteraciones.
  - Se utiliza `pytest.approx` para comparar la raíz calculada con el valor esperado, permitiendo un margen de error relativo.
  - El mensaje del assert proporciona información adicional en caso de fallo, mostrando la raíz obtenida y las iteraciones realizadas.

### 2. Test de Excepción (`test_bisection_error`)
 
  - Se define cualquier función de la cual se sabe que, para el intervalo dado, los extremos no tienen signos opuestos.
  - Se utiliza el contexto `pytest.raises(ValueError)` para indicar que, al invocar el método con un intervalo no válido, se espera que se produzca un error.
  - Este test garantiza que el método no continúa su ejecución en condiciones erróneas.

## 2- Método de Iteración de Punto Fijo

### 1. Test de Funcionalidad (`test_fixed_point_correct`)

  - Se define una función matemática y se utiliza una aproximación inicial razonable.
  - La iteración se ejecuta con parámetros de tolerancia y número máximo de iteraciones.
  - Se utiliza `pytest.approx` para comparar la solución obtenida con el valor esperado, permitiendo un margen de error relativo.
  - En caso de error, el mensaje del assert informa del valor obtenido y el número de iteraciones realizadas.

### 2. Test Trivial de Identidad (`test_fixed_point_identity`)

  - En este caso, cualquier valor es un punto fijo; por lo tanto, la iteración debería converger inmediatamente.

### 3. Test de Excepción (`test_fixed_point_error`)

  - Se utiliza una función como `g(x)=3x+2`, cuyo único punto fijo es -1, pero si se elige un valor inicial distinto (por ejemplo, 0), la iteración diverge.
  - Se utiliza `pytest.raises(ValueError)` para verificar que, al exceder el número máximo de iteraciones, se lanza el error esperado.

## 3- Método de Newton 

### 1. Test de Funcionalidad (`test_newton_sqrt`)
 
  - Resuelve la ecuación `f(x)=x^2-2=0` usando el método de Newton.
  - Se espera que la solución sea aproximadamente `sqrt(2) (~1.41421)`.
  - Se utiliza `pytest.approx` para comparar la solución obtenida dentro de una tolerancia definida.
  - Se valida también el número de iteraciones requeridas para la convergencia.

### 2. Test de Funcionalidad (`test_newton_cubic`)

  - Resuelve la ecuación `f(x)=x^3-2=0` usando el método de Newton.
  - La única raíz real es `x = cuberoot(2) (~1.25992)`. 
  - Se compara la solución obtenida usando `pytest.approx`.
  - Se verifica la convergencia dentro de la tolerancia especificada.

### 3. Test de Excepción (`test_newton_deriv_zero`)
  - Verifica que se lance un ValueError cuando la derivada es cero en el punto inicial.
  - Por ejemplo, para `f(x)=x^3`, `f'(0)=0`. Se espera que el método lance un error si `p0=0`.
  - Se utiliza `pytest.raises(ValueError)` para confirmar que se lanza la excepción cuando se inicia en `p0=0`.

## 4- Método de la Secante

### 1. Test de Funcionalidad (`test_secant_sqrt`): 
   - Se definen dos aproximaciones iniciales.
   - Se espera que el método de la secante converja a la raíz real, que es `sqrt{4} (2)`.
   - Se utiliza `pytest.approx` para validar que la solución obtenida se encuentre dentro de la tolerancia definida.

### 2. Test de Funcionalidad (`test_secant_linear`):
   - Se define una función lineal, cuya raíz es `-3/5`.
   - Debido a la linealidad de la función, el método de la secante debe converger en una sola iteración.
   - Se verifica que la solución obtenida es igual a `-3/5`.

### 3. Test de Excepción (`test_secant_division_zero`):  
   - Se define una función constante, `f(x)=5`, para la cual el numerador de la fórmula de la secante es cero ya que `f(p0) = f(p1) = 5`.
   - Esta situación produce una división por cero en el cálculo de la nueva aproximación.
   - Se utiliza `pytest.raises(ValueError)` para confirmar que el método lanza la excepción adecuada.

## 5 - Método de Posición Falsa

### 1. Test de Funcionalidad (`test_false_position_sqrt`)
- Se define la función `f(x)=x^2-7`. Esta función tiene dos raíces reales: `sqrt{7}` y `-sqrt{7}`.  
  En este test, se utilizan las aproximaciones iniciales `p0=2.0` y `p1=4.0`, de modo que:
  - `f(2.0) = 4 - 7 = -3` (negativo)
  - `f(4.0) = 16 - 7 = 9` (positivo)  
  Esto garantiza que el intervalo `[2.0,4.0]` encierra la raíz positiva `sqrt{7}`.
- Se utiliza `pytest.approx` para comparar la solución obtenida con el valor esperado con una tolerancia relativa de 1e-5.  
  En caso de que la solución no se aproxime al valor esperado, se mostrará un mensaje con la solución y el número de iteraciones.

### 2. Test de Funcionalidad (`test_false_position_linear`)

- Se define la función lineal `f(x)=11x+4`, cuya única raíz es `x = -4/11 approx -0.363636`.  
- Se utiliza `pytest.approx` para comparar la solución obtenida con `-4/11` utilizando una tolerancia relativa de 1e-5.

### 3. Test de Excepción (`test_false_position_invalid_interval`)

- Se define la función `f(x)=2x+x^3-2`.  
- En este caso, se espera que ambos valores `f(2.0)` y `f(3.0)` tengan el mismo signo, lo que implica que el intervalo no encierra ninguna raíz (violando la condición necesaria).
- Se utiliza `pytest.raises(ValueError)` para comprobar que se lanza el error esperado en este escenario.
