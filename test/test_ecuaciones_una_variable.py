import pytest
import math
from numath.ecuaciones_una_variable import bisection, fixed_point_iteration, newton_method, derivative

### BISECTION ###

def test_bisection_correct():
    def f(x):
        return x**2 - 4
    
    root, iterations = bisection(f, 0, 3, TOL=1e-5, N0=100)
    assert root == pytest.approx(2, rel=1e-5), f"Se obtuvo {root}, en {iterations} iteraciones"

def test_bisection_error():
    def f(x):
        return x**2 - 4

    with pytest.raises(ValueError):
        bisection(f, 2, 3, TOL=1e-5, N0=100)

### FIXED POINT ITERACTION ###

def test_fixed_point_correct():
   
    def g(x):
        return math.cos(x)
    
    p0 = 1.0  
    solution, iterations = fixed_point_iteration(g, p0, TOL=1e-5, N0=100)
    assert solution == pytest.approx(0.739085, rel=1e-5), f"Se esperaba ~0.739085 pero se obtuvo {solution} en {iterations} iteraciones"

def test_fixed_point_identity():
    def g(x):
        return x
    
    p0 = 42  
    solution, iterations = fixed_point_iteration(g, p0, TOL=1e-5, N0=100)
    assert solution == 42, f"Se esperaba 42 pero se obtuvo {solution}"
    assert iterations == 1, f"Se esperaba 1 iteración pero se realizaron {iterations}"

def test_fixed_point_error():
    def g(x):
        return 3 * x + 2
    
    p0 = 0.0  
    with pytest.raises(ValueError):
        fixed_point_iteration(g, p0, TOL=1e-5, N0=50)

### NEWTON METHOD ###

def test_newton_sqrt2():
    def f(x):
        return x**2 - 2

    p0 = 1.0  
    solution, iterations = newton_method(f, p0, TOL=1e-5, N0=100)
    expected = math.sqrt(2)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_newton_cubic():
    def f(x):
        return x**3 - 2
    
    p0 = 1.5
    solution, iterations = newton_method(f, p0, TOL=1e-5, N0=100)
    expected = 2 ** (1/3)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_newton_deriv_zero():
    def f(x):
        return x**3

    p0 = 0.0  
    with pytest.raises(ValueError):
        newton_method(f, p0, TOL=1e-5, N0=50, factor=1e-8)





### ADICIONALES ###

## _DERIVATIVE ##

def test_derivative_cos():
    def f(x):
        return math.cos(x)
    
    df_approx = derivative(f, TOL=1e-5)
    x_val = math.pi / 4
    expected = -math.sin(x_val) 
    assert df_approx(x_val) == pytest.approx(expected, rel=1e-5), \
        f"Derivada de cos(x) en {x_val} debería ser ~{expected}, pero se obtuvo {df_approx(x_val)}"

def test_derivative_x2():
    def f(x):
        return x**2
    
    df_approx = derivative(f, TOL=1e-5)
    x_val = 3.0
    expected = 6.0  
    assert df_approx(x_val) == pytest.approx(expected, rel=1e-5), \
        f"Derivada de x^2 en {x_val} debería ser {expected}, pero se obtuvo {df_approx(x_val)}"