import pytest
import math
from numath.ecuaciones_una_variable import bisection, fixed_point_iteration, newton_method, secant_method, false_position, steffensen_method, horner_method, muller_method

### BISECTION ###

def test_bisection_correct():
    
    funcion = "x^2- 4"
    a = "0"
    b = "3"
    TOL = "1e-5"
    N0 = "100"
    root, iterations = bisection(funcion, a, b, TOL, N0)
    assert root == pytest.approx(2, rel=1e-5), f"Se obtuvo {root}, en {iterations} iteraciones"

def test_bisection_error():
    
    funcion = "x^2- 4"
    a = "2"
    b = "3"
    TOL = "1e-5"
    N0 = "100"
    with pytest.raises(ValueError):
        bisection(funcion, a, b, TOL, N0)

### FIXED POINT ITERACTION ###

def test_fixed_point_correct():
   
    funcion = "cos(x)"
    p0 = "1.0" 
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = fixed_point_iteration(funcion, p0, TOL, N0)
    assert solution == pytest.approx(0.739085, rel=1e-5), f"Se esperaba ~0.739085 pero se obtuvo {solution} en {iterations} iteraciones"

def test_fixed_point_identity():
    
    funcion = "x"
    p0 = "42"  
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = fixed_point_iteration(funcion, p0, TOL, N0)
    assert solution == 42, f"Se esperaba 42 pero se obtuvo {solution}"
    assert iterations == 1, f"Se esperaba 1 iteración pero se realizaron {iterations}"

def test_fixed_point_error():
    
    funcion = "3x + 2"
    p0 = "0.0" 
    TOL = "1e-5"
    N0 = "100"
    with pytest.raises(ValueError):
        fixed_point_iteration(funcion, p0, TOL, N0)

### NEWTON METHOD ###

def test_newton_sqrt():

    funcion = "x^2 - 2"
    p0 = "1.0"  
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = newton_method(funcion, p0, TOL, N0)
    expected = math.sqrt(2)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_newton_cubic():
    
    funcion = "x^3 - 2"
    p0 = "1.5"
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = newton_method(funcion, p0, TOL, N0)
    expected = 2 ** (1/3)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_newton_deriv_zero():

    funcion = "x^3"
    p0 = "0.0"  
    TOL = "1e-5"
    N0 = "100"
    factor = "1e-8"
    with pytest.raises(ValueError):
        newton_method(funcion, p0, TOL, N0, factor)

### SECANT METHOD ###

def test_secant_sqrt():
    
    funcion = "x^2 - 4"
    p0 = "1.0"
    p1 = "2.0"
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = secant_method(funcion, p0, p1, TOL, N0)
    expected = math.sqrt(4)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_secant_linear():

    funcion = "5x + 3"
    p0 = "0.0"
    p1 = "1.0"
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = secant_method(funcion, p0, p1, TOL, N0)
    expected = -3/5
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_secant_division_zero():
    
    funcion = "5"
    p0 = "1.0"
    p1 = "2.0"
    TOL = "1e-5"
    N0 = "100"
    with pytest.raises(ValueError):
        secant_method(funcion, p0, p1, TOL, N0)

### FALSE POSITION ###

def test_false_position_sqrt():
    
    funcion = "x^2 - 7"
    p0 = "2.0"
    p1 = "4.0"
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = false_position(funcion, p0, p1, TOL, N0)
    expected = math.sqrt(7)
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_false_position_linear():
    
    funcion = "11x + 4"
    p0 = "-1.0"
    p1 = "0.0"
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = false_position(funcion, p0, p1, TOL, N0)
    expected = -4/11
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_false_position_invalid_interval():

    funcion = "2x + x^3 - 2"
    p0 = "2.0"
    p1 = "3.0"
    TOL = "1e-5"
    N0 = "100"
    with pytest.raises(ValueError):
        false_position(funcion, p0, p1, TOL, N0)

### STEFFENSEN METHOD ###

def test_steffensen_correct():
    
    funcion = "cos(x)"
    p0 = "7.0"
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = steffensen_method(funcion, p0, TOL, N0)
    expected = 0.739085
    assert solution == pytest.approx(expected, rel=1e-5), \
           f"Se esperaba {expected} pero se obtuvo {solution} en {iterations} iteraciones."

def test_steffensen_identity():
    
    funcion = "x"
    p0 = "5.0"
    TOL = "1e-5"
    N0 = "100"
    solution, iterations = steffensen_method(funcion, p0, TOL, N0)
    assert solution == pytest.approx(5.0, rel=1e-5), \
           f"Se esperaba 5.0, pero se obtuvo {solution} en {iterations} iteraciones."
    assert iterations == 1, f"Se esperaba convergencia en 1 iteración, pero se realizaron {iterations} iteraciones."

def test_steffensen_division_by_zero():
    
    funcion = "x + 1"
    p0 = "0.0"
    TOL = "1e-5"
    N0 = "100"
    with pytest.raises(ValueError):
        steffensen_method(funcion, p0, TOL, N0)

### HORNER METHOD ###

def test_horner_cubic():
    # P(x) = 2x^3 - 6x + 4.

    a = ["2", "0", "-6", "4"]
    x0 = "2"
    y, z = horner_method(a, x0)
    assert y == pytest.approx(8, rel=1e-5), f"Expected P(2)=8, got {y}"
    assert z == pytest.approx(18, rel=1e-5), f"Expected P'(2)=18, got {z}"

def test_horner_quadratic():
    # P(x) = x^2 + x + 5.
    
    a = ["1", "1", "5"]
    x0 = "3"
    y, z = horner_method(a, x0)
    assert y == pytest.approx(17, rel=1e-5), f"Expected P(3)=17, got {y}"
    assert z == pytest.approx(7, rel=1e-5), f"Expected P'(3)=7, got {z}"

def test_horner_linear():
    # P(x) = 3x - 2.
    
    a = ["3", "-2"]
    x0 = "4"
    y, z = horner_method(a, x0)
    assert y == pytest.approx(10, rel=1e-5), f"Expected P(4)=10, got {y}"
    assert z == pytest.approx(3, rel=1e-5), f"Expected P'(4)=3, got {z}"

### MULLER METHOD ###

def test_muller_root_convergence():
    
    funcion = "x^2 - 4"
    TOL = "1e-5"
    N0 = "100" 
    root = muller_method(funcion, 1, 3, 4, TOL, N0)
    assert pytest.approx(root, abs=1e-5) == 2

def test_muller_negative_discriminant():
    
    funcion = "x^2 + 1"
    TOL = "1e-5"
    N0 = "100"
    result = muller_method(funcion, -1, 0, 1, TOL, N0)
    assert result == "undefined"
