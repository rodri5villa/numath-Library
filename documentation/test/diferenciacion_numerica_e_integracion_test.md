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
