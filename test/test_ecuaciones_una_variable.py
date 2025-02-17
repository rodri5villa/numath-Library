import pytest
from numath.ecuaciones_una_variable import bisection

def test_bisection_correct():
    # Función a analizar: f(x) = x^2 - 4
    def f(x):
        return x**2 - 4

    # Se espera que la raíz en el intervalo [0, 3] sea 2, ya que:
    # f(0) = -4 y f(3) = 5, cumpliendo la condición de cambio de signo.
    root, iterations = bisection(f, 0, 3, tol=1e-5, max_iter=100)
    assert root == pytest.approx(2, rel=1e-5), f"Se obtuvo {root}, en {iterations} iteraciones"

def test_bisection_error():
    # Función a analizar: f(x) = x^2 - 4
    def f(x):
        return x**2 - 4

    # Se prueba que se levante un ValueError si los extremos no tienen signos opuestos.
    # Por ejemplo, en el intervalo [2, 3] se tiene:
    # f(2) = 0 y f(3) = 5, por lo que f(2) * f(3) = 0 (no es menor que 0).
    with pytest.raises(ValueError):
        bisection(f, 2, 3, tol=1e-5, max_iter=100)
