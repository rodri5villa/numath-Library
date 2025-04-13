import math
import pytest
from numath.diferenciacion_numerica_e_integracion import derivative_three_points_central, derivative_three_points_border, derivative_five_points_central, derivative_five_points_border, derivative_unified, second_derivative_central, second_derivative_central_data, trapezoidal_rule, simpson_rule, simpson_38_rule, n4_close_rule, midpoint_rule, n1_open_rule, n2_open_rule, n3_open_rule

### Punto medio de tres puntos ###

def test_derivative_three_points_central_sin():
   
    funcion = "sin(x)"
    x0 = math.pi / 4
    h = 1e-5
    deriv = derivative_three_points_central(funcion, x0, h)
    expected = math.cos(x0)
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_three_points_central_polynomial():
    
    funcion = "x^2"
    x0 = 2.0
    h = 1e-5
    deriv = derivative_three_points_central(funcion, x0, h)
    expected = 2 * x0 
    assert deriv == pytest.approx(expected, rel=1e-5)

### Extremo de tres puntos ###

def test_derivative_three_points_border_exponential():
    
    funcion = "exp(x)"
    x0 = 0.0
    h = 1e-5
    deriv = derivative_three_points_border(funcion, x0, h)
    expected = math.exp(x0) 
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_three_points_border_logarithm():
    
    funcion = "ln(1+x)"
    x0 = 0.0
    h = 1e-5
    deriv = derivative_three_points_border(funcion, x0, h)
    expected = 1 / (1 + x0)  
    assert deriv == pytest.approx(expected, rel=1e-5)

### Punto medio de cinco puntos ###

def test_derivative_five_points_central_cosine():
    
    funcion = "cos(x)"
    x0 = math.pi / 3  
    h = 1e-5
    deriv = derivative_five_points_central(funcion, x0, h)
    expected = -math.sin(x0)
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_five_points_central_cubic():
    
    funcion = "x^3"
    x0 = 2.0
    h = 1e-5
    deriv = derivative_five_points_central(funcion, x0, h)
    expected = 3 * x0**2 
    assert deriv == pytest.approx(expected, rel=1e-5)

### Extremo de cinco puntos ###

def test_derivative_five_points_border_exponential():
    
    funcion = "exp(x)"
    x0 = 0.0
    h = 1e-5
    deriv = derivative_five_points_border(funcion, x0, h)
    expected = math.exp(x0)  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_five_points_border_sqrt():
   
    funcion = "sqrt(1+x)"
    x0 = 0.0
    h = 1e-5
    deriv = derivative_five_points_border(funcion, x0, h)
    expected = 1 / (2 * math.sqrt(1 + x0))  
    assert deriv == pytest.approx(expected, rel=1e-5)

### Derivadas unificadas con respecto a los puntos dados ###

def test_derivative_unified_central5():

    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0,
        5.0: 25.0
    }
    x0 = 3.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_forward3():

    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0
    }
    x0 = 1.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_forward5():
    
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0,
        5.0: 25.0
    }
    x0 = 1.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_backward3():
    
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0
    }
    x0 = 3.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0 
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_backward5():
    
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0,
        5.0: 25.0
    }
    x0 = 5.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_unified_central3():
   
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0
    }
    x0 = 2.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  
    assert deriv == pytest.approx(expected, rel=1e-5)

### Punto medio de la segunda derivada ###

def test_second_derivative_central_polynomial():
   
    funcion = "x^2"
    x = 2.0
    h = 1e-5
    deriv2 = second_derivative_central(funcion, x, h)
    expected = 2.0
    assert deriv2 == pytest.approx(expected, rel=1e-5)

def test_second_derivative_central_sin():
    
    funcion = "sin(x)"
    x = math.pi / 4
    h = 1e-5
    deriv2 = second_derivative_central(funcion, x, h)
    expected = -math.sin(x)
    assert deriv2 == pytest.approx(expected, rel=1e-5)

### Punto medio de la segunda derivada respecto a los puntos dados ###

def test_second_derivative_central_data_polynomial():
    
    datos = {
        1.9: 3.61,
        2.0: 4.00,
        2.1: 4.41
    }
    x0 = 2.0
    deriv2 = second_derivative_central_data(datos, x0)
    expected = 2.0
    assert deriv2 == pytest.approx(expected, rel=1e-5)

def test_second_derivative_central_data_quadratic():
    
    datos = {
         0.0: 1.0,
         0.5: 2.75,
         1.0: 6.0,
         1.5: 10.75,
         2.0: 17.0
    }
    x0 = 0.5
    deriv2 = second_derivative_central_data(datos, x0)
    expected = 6.0
    assert deriv2 == pytest.approx(expected, rel=1e-5)

### Newton-Cotes Cerradas ###
### n=1: Regla Trapezoidal ###

def test_trapezoidal_linear():
   
    funcion = "2x+1"
    a = 0
    b = 2
    resultado = trapezoidal_rule(funcion, a, b)
    expected = 6
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_trapezoidal_constant():
    
    funcion = "4"
    a = 1
    b = 3
    resultado = trapezoidal_rule(funcion, a, b)
    expected = 8
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=2: Regla de Simpson ###

def test_simpson_quadratic():
   
    funcion = "x^2"
    a = 0
    b = 1
    resultado = simpson_rule(funcion, a, b)
    expected = 1/3
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_simpson_cubic():
   
    funcion = "x^3"
    a = 0
    b = 1
    resultado = simpson_rule(funcion, a, b)
    expected = 1/4
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=3: Regla de Simpson 3/8 ###

def test_simpson38_cubic():
   
    funcion = "x^3"
    a = 0
    b = 1
    resultado = simpson_38_rule(funcion, a, b)
    expected = 0.25
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_simpson38_doble_cubic():
   
    funcion = "2x^3"
    a = 0
    b = 1
    resultado = simpson_38_rule(funcion, a, b)
    expected = 0.5
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=4 ###

def test_n4_polynomial_degree4():
   
    funcion = "x^4"
    a = 0
    b = 2
    resultado = n4_close_rule(funcion, a, b)
    expected = 32/5
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n4_polynomial_degree5():
  
    funcion = "3x^5"
    a = 0
    b = 1
    resultado = n4_close_rule(funcion, a, b)
    expected = 0.5
    assert resultado == pytest.approx(expected, rel=1e-5)

### Newton-Cotes Abiertas ###
### n=0 ###

def test_midpoint_rule_constant():
    
    funcion = "4"
    a = 2
    b = 6
    resultado = midpoint_rule(funcion, a, b)
    expected = 16
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_midpoint_rule_lineal():
    
    funcion = "2x"
    a = 0
    b = 4
    resultado = midpoint_rule(funcion, a, b)
    expected = 16
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=1 ###

def test_n1_open_rule_lineal():
    
    funcion = "x+1"
    a = 1
    b = 4
    resultado = n1_open_rule(funcion, a, b)
    expected = 10.5
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n1_open_rule_afine():
    
    funcion = "3x+2"
    a = 0
    b = 3
    resultado = n1_open_rule(funcion, a, b)
    expected = 19.5
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=2 ###

def test_n2_open_rule_quadratic():
    
    funcion = "x^2"
    a = 0
    b = 4
    resultado = n2_open_rule(funcion, a, b)
    expected = 64/3
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n2_open_rule_no_lineal():
    
    funcion = "x^2+x"
    a = 1
    b = 5
    resultado = n2_open_rule(funcion, a, b)
    expected = 160/3
    assert resultado == pytest.approx(expected, rel=1e-5)

### n=3 ###

def test_n3_open_rule_cubic():
    
    funcion = "x^3"
    a = 0
    b = 5
    resultado = n3_open_rule(funcion, a, b)
    expected = 625/4  # 156.25
    assert resultado == pytest.approx(expected, rel=1e-5)

def test_n3_open_rule_cubic_escalada():
    
    funcion = "2x^3"
    a = 1
    b = 6
    resultado = n3_open_rule(funcion, a, b)
    expected = 647.5
    assert resultado == pytest.approx(expected, rel=1e-5)
