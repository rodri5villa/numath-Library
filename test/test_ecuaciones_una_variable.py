import pytest
import math
from numath.ecuaciones_una_variable import bisection, fixed_point_iteration, newton_method, secant_method, false_position

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

def test_newton_sqrt():
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

### SECANT METHOD ###

def test_secant_sqrt():
    def f(x):
        return x**2 - 4

    p0 = 1.0
    p1 = 2.0
    solution, iterations = secant_method(f, p0, p1, TOL=1e-5, N0=100)
    expected = math.sqrt(4)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_secant_linear():
    def f(x):
        return 5 * x + 3

    p0 = 0.0
    p1 = 1.0
    solution, iterations = secant_method(f, p0, p1, TOL=1e-5, N0=100)
    expected = -3/5
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_secant_division_zero():
    def f(x):
        return 5

    p0 = 1.0
    p1 = 2.0
    with pytest.raises(ValueError):
        secant_method(f, p0, p1, TOL=1e-5, N0=100)

### FALSE POSITION ###

def test_false_position_sqrt():
    def f(x):
        return x**2 - 7

    p0 = 2.0
    p1 = 4.0
    solution, iterations = false_position(f, p0, p1, TOL=1e-5, N0=100)
    expected = math.sqrt(7)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_false_position_linear():
    def f(x):
        return 11 * x + 4

    p0 = -1.0
    p1 = 0.0
    solution, iterations = false_position(f, p0, p1, TOL=1e-5, N0=100)
    expected = -4/11
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_false_position_invalid_interval():
    def f(x):
        return 2 * x + x**3 - 2

    p0 = 2.0
    p1 = 3.0
    with pytest.raises(ValueError):
        false_position(f, p0, p1, TOL=1e-5, N0=100)
