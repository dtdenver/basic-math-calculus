from sympy import symbols
from basic_math_calculus.calculus import derivative

def test_derivative():
    x = symbols("x")
    assert derivative(x**2 + 1, x) == 2 * x