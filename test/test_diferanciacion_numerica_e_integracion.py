import math
import pytest
from numath.diferenciacion_numerica_e_integracion import derivative_three_points_central, derivative_three_points_border, derivative_five_points_central, derivative_five_points_border, derivative_unified

### Punto medio de tres puntos ###

def test_derivative_three_points_central_sin():
    """
    Test para la función sin(x).
    La derivada exacta de sin(x) es cos(x).
    Se evalúa en x = pi/4, donde cos(pi/4) = sqrt(2)/2.
    """
    funcion = "sin(x)"
    x = math.pi / 4
    h = 1e-5
    deriv = derivative_three_points_central(funcion, x, h)
    expected = math.cos(x)
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_three_points_central_polynomial():
    """
    Test para la función x^2.
    La derivada exacta de x^2 es 2*x.
    Se evalúa en x = 2, donde la derivada es 4.
    """
    funcion = "x^2"
    x = 2.0
    h = 1e-5
    deriv = derivative_three_points_central(funcion, x, h)
    expected = 2 * x  # Derivada de x^2
    assert deriv == pytest.approx(expected, rel=1e-5)

### Extremo de tres puntos ###

def test_derivative_three_points_border_exponential():
    """
    Test para la función exp(x) utilizando el método forward de tres puntos.
    Se evalúa en x = 0, donde la derivada exacta es exp(0) = 1.
    """
    funcion = "exp(x)"
    x = 0.0
    h = 1e-5
    deriv = derivative_three_points_border(funcion, x, h)
    expected = math.exp(x)  # Debe ser 1 en x=0
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_three_points_border_logarithm():
    """
    Test para la función ln(1+x) utilizando el método forward de tres puntos.
    Se evalúa en x = 0, donde la derivada exacta es 1/(1+0) = 1.
    """
    funcion = "ln(1+x)"
    x = 0.0
    h = 1e-5
    deriv = derivative_three_points_border(funcion, x, h)
    expected = 1 / (1 + x)  # En x = 0, es 1.
    assert deriv == pytest.approx(expected, rel=1e-5)


### Punto medio de cinco puntos ###

def test_derivative_five_points_central_cosine():
    """
    Test para la función cos(x) usando la fórmula central de cinco puntos.
    La derivada exacta de cos(x) es -sin(x).
    Se evalúa en x = pi/3, donde -sin(pi/3) ≈ -0.8660254.
    """
    funcion = "cos(x)"
    x = math.pi / 3  # Aproximadamente 1.0471975512
    h = 1e-5
    deriv = derivative_five_points_central(funcion, x, h)
    expected = -math.sin(x)
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_five_points_central_cubic():
    """
    Test para la función x^3 usando la fórmula central de cinco puntos.
    La derivada exacta de x^3 es 3*x^2.
    Se evalúa en x = 2, donde 3*(2**2) = 12.
    """
    funcion = "x^3"
    x = 2.0
    h = 1e-5
    deriv = derivative_five_points_central(funcion, x, h)
    expected = 3 * x**2  # 12 para x = 2
    assert deriv == pytest.approx(expected, rel=1e-5)

### Extremo de cinco puntos ###

def test_derivative_five_points_border_exponential():
    """
    Test para f(x) = exp(x) usando la fórmula forward de cinco puntos.
    Se evalúa en x = 0, donde la derivada exacta es exp(0) = 1.
    """
    funcion = "exp(x)"
    x = 0.0
    h = 1e-5
    deriv = derivative_five_points_border(funcion, x, h)
    expected = math.exp(x)  # exp(0) = 1
    assert deriv == pytest.approx(expected, rel=1e-5)

def test_derivative_five_points_border_sqrt():
    """
    Test para f(x) = sqrt(1+x) usando la fórmula forward de cinco puntos.
    Se evalúa en x = 0, donde la derivada exacta es 1/(2*sqrt(1+0)) = 0.5.
    """
    funcion = "sqrt(1+x)"
    x = 0.0
    h = 1e-5
    deriv = derivative_five_points_border(funcion, x, h)
    expected = 1 / (2 * math.sqrt(1 + x))  # 1/(2*1)=0.5
    assert deriv == pytest.approx(expected, rel=1e-5)



### Derivadas unificadas con respecto a los puntos dados ###

# Caso 1: Punto interior con al menos 5 datos, se usa la fórmula central de 5 puntos.
def test_derivative_unified_central5():
    # Diccionario con 5 puntos: {1:1, 2:4, 3:9, 4:16, 5:25}.
    # Se evalúa en x0=3 (índice 2, tiene dos vecinos a cada lado).
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0,
        5.0: 25.0
    }
    x0 = 3.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  # 6.0
    assert deriv == pytest.approx(expected, rel=1e-5)

# Caso 2.1: x0 es el primer elemento y hay menos de 5 puntos,
# se usa la fórmula forward de 3 puntos.
def test_derivative_unified_forward3():
    # Diccionario con 3 puntos: {1:1, 2:4, 3:9}.
    # x0 es el primer elemento, x0=1.
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0
    }
    x0 = 1.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  # 2.0
    assert deriv == pytest.approx(expected, rel=1e-5)

# Caso 2.2: x0 es el primer elemento y hay al menos 5 puntos,
# se usa la fórmula forward de 5 puntos.
def test_derivative_unified_forward5():
    # Diccionario con 5 puntos: {1:1,2:4,3:9,4:16,5:25}.
    # x0 es el primer elemento, x0=1.
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0,
        5.0: 25.0
    }
    x0 = 1.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  # 2.0
    assert deriv == pytest.approx(expected, rel=1e-5)

# Caso 3.1: x0 es el último elemento y hay menos de 5 puntos,
# se usa la fórmula backward de 3 puntos.
def test_derivative_unified_backward3():
    # Diccionario con 3 puntos: {1:1, 2:4, 3:9}.
    # x0 es el último elemento, x0=3.
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0
    }
    x0 = 3.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  # 6.0
    assert deriv == pytest.approx(expected, rel=1e-5)

# Caso 3.2: x0 es el último elemento y hay al menos 5 puntos,
# se usa la fórmula backward de 5 puntos.
def test_derivative_unified_backward5():
    # Diccionario con 5 puntos: {1:1,2:4,3:9,4:16,5:25}.
    # x0 es el último elemento, x0=5.
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0,
        5.0: 25.0
    }
    x0 = 5.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  # 10.0
    assert deriv == pytest.approx(expected, rel=1e-5)

# Caso 4: x0 es un punto interior pero no se cumple la condición para la fórmula de 5 puntos.
# Aquí usaremos un diccionario con 4 puntos; en ese caso, x0 no tiene dos vecinos a cada lado para usar la fórmula de 5 puntos,
# y se usa la fórmula central de 3 puntos.
def test_derivative_unified_central3():
    # Diccionario con 4 puntos: {1:1, 2:4, 3:9, 4:16}.
    # x0 es un punto interior, elegimos x0=2 (índice 1) o x0=3 (índice 2).
    # Usamos x0=2; la derivada exacta es 2*2 = 4.
    datos = {
        1.0: 1.0,
        2.0: 4.0,
        3.0: 9.0,
        4.0: 16.0
    }
    x0 = 2.0
    deriv = derivative_unified(datos, x0)
    expected = 2 * x0  # 4.0
    assert deriv == pytest.approx(expected, rel=1e-5)
