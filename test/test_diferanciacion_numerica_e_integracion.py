import math
import pytest
from numath.diferenciacion_numerica_e_integracion import derivative_three_points_central, derivative_three_points_border, derivative_five_points_central, derivative_five_points_border, derivative_unified, second_derivative_central, second_derivative_central_data, newton_cotes_n1_close, newton_cotes_n2_close, newton_cotes_n3_close, newton_cotes_n4_close, newton_cotes_n0_open, newton_cotes_n1_open, newton_cotes_n2_open, newton_cotes_n3_open, composite_simpson_rule, composite_trapezoidal_rule, composite_midpoint_rule, romberg_integration, composite_double_simpson, double_gaussian_integration, triple_gaussian_integration

### Punto medio de tres puntos ###

def test_derivative_three_points_central_sin():
   
    funcion = "sin(x)"
    x0 = "pi / 4"
    h = "1e-5"
    deriv = derivative_three_points_central(funcion, x0, h)
    expected = math.cos(math.pi/4)
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_three_points_central_polynomial():
    
    funcion = "x^2"
    x0 = "2.0"
    h = "1e-5"
    deriv = derivative_three_points_central(funcion, x0, h)
    expected = 2 * 2
    assert deriv == pytest.approx(expected, rel=1e-5)

### Extremo de tres puntos ###

def test_derivative_three_points_border_exponential():
    
    funcion = "exp(x)"
    x0 = "0.0"
    h = "1e-5"
    deriv = derivative_three_points_border(funcion, x0, h)
    expected = math.exp(0) 
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_three_points_border_logarithm():
    
    funcion = "ln(1+x)"
    x0 = "0.0"
    h = "1e-5"
    deriv = derivative_three_points_border(funcion, x0, h)
    expected = 1 / (1 + 0)  
    assert deriv == pytest.approx(expected, rel=1e-5)

### Punto medio de cinco puntos ###

def test_derivative_five_points_central_cosine():
    
    funcion = "cos(x)"
    x0 = "pi / 3" 
    h = "1e-5"
    deriv = derivative_five_points_central(funcion, x0, h)
    expected = -math.sin(math.pi/3)
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_five_points_central_cubic():
    
    funcion = "x^3"
    x0 = "2.0"
    h = "1e-5"
    deriv = derivative_five_points_central(funcion, x0, h)
    expected = 3 * 2**2 
    assert deriv == pytest.approx(expected, rel=1e-5)

### Extremo de cinco puntos ###

def test_derivative_five_points_border_exponential():
    
    funcion = "exp(x)"
    x0 = "0.0"
    h = "1e-5"
    deriv = derivative_five_points_border(funcion, x0, h)
    expected = math.exp(0)  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_five_points_border_sqrt():
   
    funcion = "sqrt(1+x)"
    x0 = "0.0"
    h = "1e-5"
    deriv = derivative_five_points_border(funcion, x0, h)
    expected = 1 / (2 * math.sqrt(1 + 0))  
    assert deriv == pytest.approx(expected, rel=1e-5)

### Derivadas unificadas con respecto a los puntos dados ###

def test_derivative_unified_central5():

    datos = {
        "1.0": "1.0",
        "2.0": "4.0",
        "3.0": "9.0",
        "4.0": "16.0",
        "5.0": "25.0"
    }
    x0 = "3.0"
    deriv = derivative_unified(datos, x0)
    expected = 2 * 3  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_forward3():

    datos = {
        "1.0": "1.0",
        "2.0": "4.0",
        "3.0": "9.0"
    }
    x0 = "1.0"
    deriv = derivative_unified(datos, x0)
    expected = 2 * 1  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_forward5():
    
    datos = {
        "1.0": "1.0",
        "2.0": "4.0",
        "3.0": "9.0",
        "4.0": "16.0",
        "5.0": "25.0"
    }
    x0 = "1.0"
    deriv = derivative_unified(datos, x0)
    expected = 2 * 1  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_backward3():
    
    datos = {
        "1.0": "1.0",
        "2.0": "4.0",
        "3.0": "9.0"
    }
    x0 = "3.0"
    deriv = derivative_unified(datos, x0)
    expected = 2 * 3 
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_backward5():
    
    datos = {
        "1.0": "1.0",
        "2.0": "4.0",
        "3.0": "9.0",
        "4.0": "16.0",
        "5.0": "25.0"
    }
    x0 = "5.0"
    deriv = derivative_unified(datos, x0)
    expected = 2 * 5  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_central3():
   
    datos = {
        "1.0": "1.0",
        "2.0": "4.0",
        "3.0": "9.0",
        "4.0": "16.0"
    }
    x0 = "2.0"
    deriv = derivative_unified(datos, x0)
    expected = 2 * 2 
    assert deriv == pytest.approx(expected, rel=1e-5)

### Punto medio de la segunda derivada ###

def test_second_derivative_central_polynomial():
   
    funcion = "x^2"
    x = "2.0"
    h = "1e-5"
    deriv2 = second_derivative_central(funcion, x, h)
    expected = 2.0
    assert deriv2 == pytest.approx(expected, rel=1e-5)

def test_second_derivative_central_sin():
    
    funcion = "sin(x)"
    x = "pi / 4"
    h = "1e-5"
    deriv2 = second_derivative_central(funcion, x, h)
    expected = -math.sin(math.pi/4)
    assert deriv2 == pytest.approx(expected, rel=1e-5)

### Punto medio de la segunda derivada respecto a los puntos dados ###

def test_second_derivative_central_data_polynomial():
    
    datos = {
        "1.9": "3.61",
        "2.0": "4.00",
        "2.1": "4.41"
    }
    x0 = "2.0"
    deriv2 = second_derivative_central_data(datos, x0)
    expected = 2.0
    assert deriv2 == pytest.approx(expected, rel=1e-5)

def test_second_derivative_central_data_quadratic():
    
    datos = {
        "0.0": "1.0",
        "0.5": "2.75",
        "1.0": "6.0",
        "1.5": "10.75",
        "2.0": "17.0"
    }
    x0 = "0.5"
    deriv2 = second_derivative_central_data(datos, x0)
    expected = 6.0
    assert deriv2 == pytest.approx(expected, rel=1e-5)

### Newton-Cotes Cerradas ###
### n=1: Regla Trapezoidal ###

def test_n1c_linear():
   
    funcion = "2x+1"
    a = "0"
    b = "2"
    resultado = newton_cotes_n1_close(funcion, a, b)
    expected = 6
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n1c_constant():
    
    funcion = "4"
    a = "1"
    b = "3"
    resultado = newton_cotes_n1_close(funcion, a, b)
    expected = 8
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=2: Regla de Simpson ###

def test_n2c_quadratic():
   
    funcion = "x^2"
    a = "0"
    b = "1"
    resultado = newton_cotes_n2_close(funcion, a, b)
    expected = 1/3
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n2c_cubic():
   
    funcion = "x^3"
    a = "0"
    b = "1"
    resultado = newton_cotes_n2_close(funcion, a, b)
    expected = 1/4
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=3: Regla de Simpson 3/8 ###

def test_n3c_cubic():
   
    funcion = "x^3"
    a = "0"
    b = "1"
    resultado = newton_cotes_n3_close(funcion, a, b)
    expected = 0.25
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n3c_doble_cubic():
   
    funcion = "2x^3"
    a = "0"
    b = "1"
    resultado = newton_cotes_n3_close(funcion, a, b)
    expected = 0.5
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=4 ###

def test_n4c_polynomial_degree4():
   
    funcion = "x^4"
    a = "0"
    b = "2"
    resultado = newton_cotes_n4_close(funcion, a, b)
    expected = 32/5
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n4c_polynomial_degree5():
  
    funcion = "3x^5"
    a = "0"
    b = "1"
    resultado = newton_cotes_n4_close(funcion, a, b)
    expected = 0.5
    assert resultado == pytest.approx(expected, rel=1e-5)

### Newton-Cotes Abiertas ###
### n=0 ###

def test_n0a_constant():
    
    funcion = "4"
    a = "2"
    b = "6"
    resultado = newton_cotes_n0_open(funcion, a, b)
    expected = 16
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n0a_lineal():
    
    funcion = "2x"
    a = "0"
    b = "4"
    resultado = newton_cotes_n0_open(funcion, a, b)
    expected = 16
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=1 ###

def test_n1a_lineal():
    
    funcion = "x+1"
    a = "1"
    b = "4"
    resultado = newton_cotes_n1_open(funcion, a, b)
    expected = 10.5
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n1a_afine():
    
    funcion = "3x+2"
    a = "0"
    b = "3"
    resultado = newton_cotes_n1_open(funcion, a, b)
    expected = 19.5
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=2 ###

def test_n2a_quadratic():
    
    funcion = "x^2"
    a = "0"
    b = "4"
    resultado = newton_cotes_n2_open(funcion, a, b)
    expected = 64/3
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n2a_no_lineal():
    
    funcion = "x^2+x"
    a = "1"
    b = "5"
    resultado = newton_cotes_n2_open(funcion, a, b)
    expected = 160/3
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=3 ###

def test_n3a_cubic():
    
    funcion = "x^3"
    a = "0"
    b = "5"
    resultado = newton_cotes_n3_open(funcion, a, b)
    expected = 625/4  
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n3a_cubic_escalada():
    
    funcion = "2x^3"
    a = "1"
    b = "6"
    resultado = newton_cotes_n3_open(funcion, a, b)
    expected = 647.5
    assert resultado == pytest.approx(expected, rel=1e-5)

### Regla de Simpson Compuesta ###

def test_composite_simpson_mixed_polynomial():
    
    funcion = "3x^3 - x^2 + 5x - 2"
    a = "-1"
    b = "2"
    n = "4"
    resultado = composite_simpson_rule(funcion, a, b, n)
    expected = 39/4
    assert resultado == pytest.approx(expected, rel=0, abs=1e-12)

def test_composite_simpson_quadratic_shifted():
    
    funcion = "x^2 + 2x + 1"
    a = "1" 
    b = "4"
    n = "6"
    resultado = composite_simpson_rule(funcion, a, b, n)
    expected = 39.0
    assert resultado == pytest.approx(expected, rel=0, abs=1e-12)

### Regla Trapezoidal Compuesta ###

def test_composite_trapezoidal_exponential():
    
    funcion = "exp(x)"
    a = "0"
    b = "1"
    n = "50"
    resultado = composite_trapezoidal_rule(funcion, a, b, n)
    expected = math.e - 1
    assert resultado == pytest.approx(expected, rel=1e-4)

def test_composite_trapezoidal_reciprocal_square():
    
    funcion = "1/(1+x^2)"
    a = "-1"
    b = "1"
    n = "100"
    resultado = composite_trapezoidal_rule(funcion, a, b, n)
    expected = math.pi/2
    assert resultado == pytest.approx(expected, rel=1e-4)

### Regla del Punto Medio Compuesta ###

def test_composite_midpoint_logarithm():
    
    funcion = "ln(1+x)"
    a = "0"
    b = "1"
    n = "10"
    resultado = composite_midpoint_rule(funcion, a, b, n)
    expected = 2*math.log(2) - 1
    assert resultado == pytest.approx(expected, rel=1e-2)

def test_composite_midpoint_gaussian():
   
    funcion = "exp(-x^2)"
    a = "0"
    b = "1" 
    n = "20"
    resultado = composite_midpoint_rule(funcion, a, b, n)
    expected = 0.7468241328124271
    assert resultado == pytest.approx(expected, rel=1e-3)

### Integración de Romberg ###

def test_romberg_sin():
    
    funcion = "sin(x)"
    a = "0"
    b = "pi"
    n = "5"
    R = romberg_integration(funcion, a, b, n)
    resultado = R[5][5]
    expected = 2.0
    assert resultado == pytest.approx(expected, rel=1e-8)

def test_romberg_polynomial_cubic():
   
    funcion = "x^3"
    a = "0"
    b = "1"
    n = "4"
    R = romberg_integration(funcion, a, b, n)
    resultado = R[4][4]
    expected = 0.25
    assert resultado == pytest.approx(expected, abs=1e-12)

### Integral Doble de Simpson ###

def test_composite_double_simpson_logarithm():
        
    funcion = "ln(x+2y)"
    a = "1.4"
    b = "2"
    c_func = "1"
    d_func = "1.5"
    n = m = "10"
    resultado = composite_double_simpson(funcion, a, b, c_func, d_func, n, m)
    expected = 0.4295545265
    assert resultado == pytest.approx(expected, rel=1e-7)

def test_composite_double_simpson_variable_limits():
   
    funcion = "xy"
    a = "0"
    b = "2"
    c_func = "0"
    d_func = "x"
    n = m = "4"
    resultado = composite_double_simpson(funcion, a, b, c_func, d_func, n, m)
    expected = 2.0
    assert resultado == pytest.approx(expected, rel=1e-9)

### Integral Doble Gaussiana ###

def test_double_gaussian_x_times_y_squared():
    
    funcion = "x*y^2"
    a = "0"
    b = "3"
    c_func = "0"
    d_func = "1"
    m = n = "4"
    resultado = double_gaussian_integration(funcion, a, b, c_func, d_func, m, n)
    expected = 1.5
    assert resultado == pytest.approx(expected, rel=1e-9)

def test_double_gaussian_sin_x_cos_y():
    
    funcion = "sin(x)*cos(y)"
    a = "0"
    b = "pi"
    c_func = "0"
    d_func = "pi/2"
    m = n = "5"
    resultado = double_gaussian_integration(funcion, a, b, c_func, d_func, m, n)
    expected = 2.0
    assert resultado == pytest.approx(expected, rel=1e-7)

### Integral Triple Gaussiana ###

def test_triple_gaussian_sum_of_vars():
    
    funcion = "x+y+z"
    a = "0"
    b = "1"
    c_func = "0"
    d_func = "1"
    alpha_func = "0"
    beta_func = "1"
    m = n = p = "4"
    resultado = triple_gaussian_integration(funcion, a, b, c_func, d_func, alpha_func, beta_func, m, n, p)
    expected = 1.5
    assert resultado == pytest.approx(expected, rel=1e-9)

def test_triple_gaussian_product_xyz_region():
    
    funcion = "x*y*z"
    a = "1"
    b = "2"
    c_func = "0"
    d_func = "1"
    alpha_func = "0"
    beta_func = "1"
    m = n = p = "3"
    resultado = triple_gaussian_integration(funcion, a, b, c_func, d_func, alpha_func, beta_func, m, n, p)
    expected = 0.375
    assert resultado == pytest.approx(expected, rel=1e-9)
