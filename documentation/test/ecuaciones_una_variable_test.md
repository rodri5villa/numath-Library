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

  - Se utiliza una función como g(x)=3x+2, cuyo único punto fijo es -1, pero si se elige un valor inicial distinto (por ejemplo, 0), la iteración diverge.
  - Se utiliza `pytest.raises(ValueError)` para verificar que, al exceder el número máximo de iteraciones, se lanza el error esperado.

## 3- Método de Newton 

### 1. Test de Funcionalidad (`test_newton_sqrt2`)
 
  - Resuelve la ecuación f(x)=x^2-2=0 usando el método de Newton.
  - Se espera que la solución sea aproximadamente sqrt(2) (~1.41421).
  - Se utiliza `pytest.approx` para comparar la solución obtenida dentro de una tolerancia definida.
  - Se valida también el número de iteraciones requeridas para la convergencia.

### 2. Test de Funcionalidad (`test_newton_cubic`)

  - Resuelve la ecuación f(x)=x^3-2=0 usando el método de Newton.
  - La única raíz real es x = cuberoot(2) (~1.25992). 
  - Se compara la solución obtenida usando `pytest.approx`.
  - Se verifica la convergencia dentro de la tolerancia especificada.

### 3. Test de Excepción para Derivada Cero (`test_newton_deriv_zero`)
  - Verifica que se lance un ValueError cuando la derivada es cero en el punto inicial.
  - Por ejemplo, para f(x)=x^3, f'(0)=0. Se espera que el método lance un error si p0=0.
  - Se utiliza `pytest.raises(ValueError)` para confirmar que se lanza la excepción cuando se inicia en \( p_0=0 \).





## Adicionales

### 1. Derivación Numérica

#### 1. Test de Funcionalidad con cos(x) (`test_derivative_cos`)
  - Verifica que la derivada numérica de cos(x) en un punto sea aproximadamente -sin(x).
  - Se utiliza `pytest.approx` para comparar el valor calculado.
  - Se permite un margen de error relativo que garantice la precisión de la aproximación.

#### 2. Test de Funcionalidad con f(x)=x^2 (`test_derivative_x2`)
  - Verifica que la derivada numérica de f(x)=x^2 en un punto sea aproximadamente 2*x.
  - Se compara el resultado de la derivada numérica con el valor exacto usando `pytest.approx`.
