# Documentación de los Tests del Módulo de Diferenciación Numérica e Integración

## 1- Punto medio de tres puntos

### 1. Test de Funcionalidad (`test_derivative_three_points_central_sin`) 

  - Se evalúa en `x = pi/4`  
  - La derivada exacta de `sin(x)` es `cos(x)`, y en `pi/4` se espera aproximadamente `sqrt(2)/2`

### 2. Test de Funcionalidad (`test_derivative_three_points_central_polynomial`)  
  
  - Se evalúa en `x = 2`  
  - La derivada exacta de `x^2` es `2x`, se espera `4` en `x=2`

## 2- Extremo de tres puntos

### 1. Test de Funcionalidad (`test_derivative_three_points_border_exponential`)
   
  - Se evalúa en `x = 0`  
  - La derivada exacta de `exp(x)` es `exp(x)` en `x = 0` se espera `1`.

### 2. Test de Funcionalidad (`test_derivative_three_points_border_logarithm`) 
  
  - Se evalúa en `x = 0` 
  - La derivada exacta de `ln(1+x)` es `1/(1+x)` en `x = 0` se espera `1`

## 3- Punto medio de cinco puntos

### 1. Test de Funcionalidad (`test_derivative_five_points_central_cosine`)  
  
  - Se evalúa en `x = pi/3`
  - La derivada exacta de `cos(x)` es `-sin(x)`; en `pi/3` se espera aproximadamente `-sin(pi/3)`

### 2. Test de Funcionalidad (`test_derivative_five_points_central_cubic`)  
  
  - Se evalúa en `x = 2`
  - La derivada exacta de `x^3` es `3x^2`; en `x = 2` se espera `12`

## 4- Extremo de cinco puntos

### 1. Test de Funcionalidad (`test_derivative_five_points_border_exponential`)  
  
  - Se evalúa en `x = 0`
  - La derivada exacta de `exp(x)` es `exp(x)`, en `x = 0` se espera `1`

### 2. Test de Funcionalidad (`test_derivative_five_points_border_sqrt`)  
  
  - Se evalúa en `x = 0`
  - La derivada exacta de `sqrt(1+x)` es `1/(2*sqrt(1+x))`, en `x = 0` se espera `0.5`

## 5- Derivadas unificadas con respecto a los puntos dados

### 1. Test de Funcionalidad (`test_derivative_unified_central5`)
 
  - Se utiliza el diccionario:
    ```python
    {1.0: 1.0, 2.0: 4.0, 3.0: 9.0, 4.0: 16.0, 5.0: 25.0}
    ```
  - Se evalúa en `x0 = 3.0` y el resultado esperado es `6`
  - Se utiliza la **fórmula del punto medio de cinco puntos:**

        f'(x0) = (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12 * h)

### 2. Test de Funcionalidad (`test_derivative_unified_forward3`)
  
  - Se utiliza el diccionario:
    ```python
    {1.0: 1.0, 2.0: 4.0, 3.0: 9.0}
    ```
  - Se evalúa en `x0 = 1.0` y el resultado esperado es `2`
  - Se utiliza la **fórmula forward de 3 puntos:**

        f'(x0) = (-3 * f(x0) + 4 * f(x0 + h) - f(x0 + 2 * h)) / (2 * h)

### 3. Test de Funcionalidad (`test_derivative_unified_forward5`) 
  
  - Se utiliza el diccionario:
    ```python
    {1.0: 1.0, 2.0: 4.0, 3.0: 9.0, 4.0: 16.0, 5.0: 25.0}
    ```
  - Se evalúa en `x0 = 1.0` y el resultado esperado es `2`
  - Se utiliza la **fórmula forward de 5 puntos:**

        f'(x0) = (-25 * f(x0) + 48 * f(x0 + h) - 36 * f(x0 + 2 * h) + 16 * f(x0 + 3 * h) - 3 * f(x0 + 4 * h)) / (12 * h) 

### 4. Test de Funcionalidad (`test_derivative_unified_backward3`) 
  
  - Se utiliza el diccionario:
    ```python
    {1.0: 1.0, 2.0: 4.0, 3.0: 9.0}
    ```
  - Se evalúa en `x0 = 3.0` y el resultado esperado es `6`
  - Se utiliza la **fórmula backward de 3 puntos:**

        f'(x0) = (3 * f(x0) - 4 * f(x0 + h) + f(x0 + 2 * h)) / (2 * h) 

### 5. Test de Funcionalidad (`test_derivative_unified_backward5`) 
  
  - Se utiliza el diccionario:
    ```python
    {1.0: 1.0, 2.0: 4.0, 3.0: 9.0, 4.0: 16.0, 5.0: 25.0}
    ```
  - Se evalúa en `x0 = 5.0` y el resultado esperado es `10`
  - Se utiliza la **fórmula backward de 5 puntos:**

        f'(x0) = (25 * f(x0) - 48 * f(x0 + h) + 36 * f(x0 + 2 * h) - 16 * f(x0 + 3 * h) + 3 * f(x0 + 4 * h)) / (12 * h)
  
### 6. Test de Funcionalidad (`def test_derivative_unified_central3`) 
  
  - Se utiliza un diccionario con 4 puntos:
    ```python
    {1.0: 1.0, 2.0: 4.0, 3.0: 9.0, 4.0: 16.0}
    ```
  - Se evalúa en `x0 = 2.0` y el resultado esperado es `4`
  - Se utiliza la **fórmula del punto medio de tres puntos:**

        f'(x0) = (f(x0 + h) - f(x0 - h)) / (2 * h)

## 6- Punto medio de la segunda derivada

### 1. Test de Funcionalidad (`test_second_derivative_central_polynomial`)  
  
  - Se evalúa en `x = 2`
  - Para `f(x) = x^2`, la segunda derivada es `2`

### 2. Test de Funcionalidad (`test_second_derivative_central_sin`) 
  
  - Se evalúa en `x = pi/4`.  
  - Para `f(x) = sin(x)`, la segunda derivada es `-sin(x)`.

## 7- Punto medio de la segunda derivada respecto a los puntos dados

### 1. Test de Funcionalidad (`test_second_derivative_central_data_polynomial`)  
  
  - Se usan 3 puntos para `f(x) = x^2`:  

    ```python
    {1.9: 3.61, 2.0: 4.00, 2.1: 4.41}
    ``` 
  - Se evalúa en `x0 = 2` y se espera `2`

### 2. Test de Funcionalidad (`test_second_derivative_central_data_quadratic`)  
  
  - Se utilizan 5 puntos para la función `f(x) = 3x^2+2x+1`:

    ```python
    {0.0: 1.0, 0.5: 2.75, 1.0: 6.0, 1.5: 10.75, 2.0: 17.0}
    ```  
  - Se evalúa en `x0 = 0.5` y se espera `6`

## 8- Fórmulas de Newton-Cotes Cerradas

## 8.1- n=1: Regla Trapezoidal

### 1. Test de Funcionalidad (`test_n1c_linear`)

  - Se prueba el método usando una función lineal, para la cual la Regla del Trapecio es exacta.
  - Se evalúa la función `f(x) = 2x + 1` en `[0, 2]` y el resultado esperado es `6`
  
### 2. Test de Funcionalidad (`test_n1c_constant`)

  - Se prueba el método usando una función constante, cuyo resultado es exacto.
  - Se evalúa la función `f(x) = 4` en `[1, 3]` y el resultado esperado es `8`
  
## 8.2- n=2: Regla de Simpson

### 1. Test de Funcionalidad (`test_n2c_quadratic`)

  - Se prueba el método usando una función cuadrática, para la cual la Regla de Simpson es exacta.
  - Se evalúa la función `f(x) = x^2` en `[0, 1]` y el resultado esperado es `1/3 ≈ 0.33333`

### 2. Test de Funcionalidad (`test_n2c_cubic`)

  - Se prueba el método con una función cúbica, para la cual la Regla de Simpson también da el valor exacto.
  - Se evalúa la función `f(x) = x^3` en `[0, 1]` y el resultado esperado es `1/4 = 0.25`

## 8.3- n=3: Regla de Simpson 3/8

### 1. Test de Funcionalidad (`test_n3c_cubic`)

  - Se prueba la regla utilizando la función cúbica.
  - Se evalúa la función `f(x) = x^3` en `[0, 1]` y el resultado esperado es `1/4 = 0.25`

### 2. Test de Funcionalidad (`test_n3c_doble_cubic`)

  - Se prueba la regla utilizando una función cúbica escalada.
  - Se evalúa la función `f(x) = 2x^3` en `[0, 1]` y el resultado esperado es `2 * (1/4) = 0.5`

## 8.4- n=4

### 1. Test de Funcionalidad (`test_n4c_polynomial_degree4`)

  - Se prueba la regla n=4 con un polinomio de grado 4.
  - Se evalúa la función `f(x) = x^4` en `[0, 2]` y el resultado esperado es `32/5 = 6.4`

### 2. Test de Funcionalidad (`test_n4c_polynomial_degree5`)

  - Se prueba la regla n=4 con un polinomio de grado 5.
  - Se evalúa la función `f(x) = 3x^5` en `[0, 1]` y el resultado esperado es `3/6 = 0.5`

## 9- Fórmulas de Newton-Cotes Abiertas

## 9.1- n=0: Regla del Punto Medio

### 1. Test de Funcionalidad (`test_n0a_constant`)

  - Se prueba la regla del punto medio utilizando una función constante.
  - Se evalúa la función `f(x) = 4` en `[2, 6]` y el resultado esperado es `16`

### 2. Test de Funcionalidad (`test_n0a_lineal`)

  - Se prueba la regla del punto medio con una función lineal.
  - Se evalúa la función `f(x) = 2x` en `[0, 4]` y el resultado esperado es `16`

## 9.2- n=1

### 1. Test de Funcionalidad (`test_n1a_lineal`)

  - Se prueba la regla de `n=1` usando una función lineal.
  - Se evalúa la función `f(x) = x + 1` en `[1, 4]` y el resultado esperado es `10.5`

### 2. Test de Funcionalidad (`test_n1a_afine`)

  - Se prueba la regla de `n=1` con una función afín.
  - Se evalúa la función `f(x) = 3x + 2` en `[0, 3]` y el resultado esperado es `19.5`

## 9.3- n=2

### 1. Test de Funcionalidad (`test_n2a_quadratic`)

  - Se prueba la regla de `n=2` utilizando una función cuadrática.  
  - Se evalúa la función `f(x) = x^2` en `[0, 4]` y el resultado esperado es `64/3`

### 2. Test de Funcionalidad (`test_n2a_no_lineal`)

  - Se prueba la regla de `n=2` con una función polinómica de segundo grado sumada a un término lineal.
  - Se evalúa la función `f(x) = x^2 + x` en `[1, 5]` y el resultado esperado es `160/3`

## 9.4- n=3 

### 1. Test de Funcionalidad (`test_n3a_cubic`)

  - Se prueba la regla de `n=3` usando una función cúbica.
  - Se evalúa la función `f(x) = x^3` en `[0, 5]` y el resultado esperado es `625/4 = 156.25`

### 2. Test de Funcionalidad (`test_n3a_cubic_escalada`)

  - Se prueba la regla de `n=3` con una función cúbica escalada.
  - Se evalúa la función `f(x) = 2x^3` en `[1, 6]` y el resultado esperado es `647.5`

## 10- Regla de Simpson Compuesta

### 1. Test de Funcionalidad (`test_composite_simpson_mixed_polynomial`)
  
  - Se evalúa la función `f(x) = 3x^3 - x^2 + 5x - 2` en el intervalo `[-1, 2]` usando `n = 4` 
  - El resultado esperado es `39/4`  

### 2. Test de Funcionalidad (`test_composite_simpson_quadratic_shifted`)

  - Se evalúa la función `f(x) = x^2 + 2x + 1` en `[1, 4]` con `n = 6`
  - El resultado esperado es `39.0`  

## 11- Regla Trapezoidal Compuesta

### 1. Test de Funcionalidad (`test_composite_trapezoidal_exponential`)

  - Se evalúa la función `f(x) = exp(x)` en `[0, 1]` con `n = 50`
  - El resultado esperado es `e - 1`

### 2. Test de Funcionalidad (`test_composite_trapezoidal_reciprocal_square`)

  - Se evalúa la función `f(x) = 1/(1+x^2)` en `[-1, 1]` con `n = 100`
  - El resultado esperado es `π/2`

## 12- Regla del Punto Medio Compuesta

### 1. Test de Funcionalidad (`test_composite_midpoint_logarithm`)

  - Se evalúa la función `f(x) = ln(1+x)` en `[0, 1]` con `n = 10`
  - El resultado esperado es `2ln2 - 1`

### 2. Test de Funcionalidad (`test_composite_midpoint_gaussian`)

  - Se evalúa la función `f(x) = exp(-x^2)` en `[0, 1]` con `n = 20`
  - El resultado esperado es `0.7468241328124271`

## 13- Integración de Romberg

### 1. Test de Funcionalidad (`test_romberg_sin`)

- Se aproxima la función `sin(x)` en `[0, pi]` con `n = 5`  
- El resultado esperado es `2.0`

### 2. Test de Funcionalidad (`test_romberg_polynomial_cubic`)

- Se aproxima la función `x^3` en `[0, 1]` con `n = 4`  
- El resultado esperado es `0.25`

## 14- Integral Doble de Simpson

### 1. Test de Funcionalidad (`test_composite_double_simpson_logarithm`)

- Se aproxima la función `ln(x+2y)` en `[1.4, 2]` con `[c_func, d_func] = [1, 1.5]` con `n = m = 10`  
- El resultado esperado es `0.4295545265`

### 2. Test de Funcionalidad (`test_composite_double_simpson_variable_limits`)

- Se aproxima la función `xy` en `[0, 2]` con `[c_func, d_func] = [0, x]` con `n = m = 4`  
- El resultado esperado es `2.0`

## 15- Integral Doble Gaussiana

### 1. Test de Funcionalidad (`test_double_gaussian_x_times_y_squared`)

- Se aproxima la función `x*y^2` en el dominio `[0, 3]`, `[0, 1]` usando cuadratura de Gauss–Legendre con `m = n = 4`.
- El resultado esperado es `1.5`

### 2. Test de Funcionalidad (`test_double_gaussian_sin_x_cos_y`)

- Se aproxima la función `sin(x)*cos(y)` en el dominio `[0, π]`, `[0, π/2]` usando cuadratura de Gauss–Legendre con `m = n = 5`.
- El resultado esperado es `1.5`

## 16- Integral Triple Gaussiana

### 1. Test de Funcionalidad (`test_triple_gaussian_sum_of_vars`)

- Se aproxima la función `x+y+z` en el dominio `[0, 1]`, `[0, 1]`, `[0, 1]` usando cuadratura de Gauss–Legendre con `m = n = p = 4`.
- El resultado esperado es `1.5`

### 2. Test de Funcionalidad (`test_triple_gaussian_product_xyz_region`)

- Se aproxima la función `x*y*z` en el dominio `[1, 2]`, `[0, 1]`, `[0, 1]` usando cuadratura de Gauss–Legendre con `m = n = p = 3`.
- El resultado esperado es `0.375`
