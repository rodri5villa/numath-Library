import math
import pytest
from numath.diferenciacion_numerica_e_integracion import derivative_three_points_central, derivative_three_points_border, derivative_five_points_central, derivative_five_points_border, derivative_unified, second_derivative_central, second_derivative_central_data

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
