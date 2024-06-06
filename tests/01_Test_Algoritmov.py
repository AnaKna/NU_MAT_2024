import unittest
from sympy import Symbol, sympify, sin  # Assuming you use SymPy for symbolic expressions
import sys
import math

sys.path.append('.')
from src.Gauss_Legendre import Gauss_Legendre
from src.Gauss_Legendre_Composition import GL_composite_int
from src.Trapez_integration import trapez_int, trapez_int_sin

# The function to be integrated: x**4 + 3
def f_x4_3(x):
    return x**4 + 3


def f_x3_15(x):
    return x**3 + 15


# Definicija funkcije: sin(x)/x
def sin_div_x(x):
  if(x == 0):     # sin(0)/0 je nedefinirano -> limita je 1
    if math.isnan(sin(x) / x):
        return 1.0
  else:
    return sin(x) / x

#--------------------------------TEST GAUSS-LEGENDREOVEGA ALGORITMA----------------------------------------------------------

# Če je stopnja polinoma <= 2*N-1 je aproksimacija integrala točka in je Error = 0
# 2*N-1 = 2*2 - 1 = 3 , kar za funkcijo x^4+3 ne velja
class TestGaussLegendre_1(unittest.TestCase):

    def test_polynomial_function_1(self):
        """Tests Gauss-Legendre with a polynomial function."""
        x = Symbol('x')
        f = sympify("x**4+3")
        stopnja = 4
        a = 1
        b = 4
        expected_integral = 213.6  # Solution for the definite integral
        integral, error = Gauss_Legendre(f, stopnja, x, a, b)
        self.assertAlmostEqual(integral + error , expected_integral, places=5)


# Če je stopnja polinoma <= 2*N-1 je aproksimacija integrala točka in je Error = 0
# 2*N-1 = 2*2 - 1 = 3, kar za funkcijo x**3 + 15 velja
class TestGaussLegendre_2(unittest.TestCase):

    def test_polynomial_function_2(self):
        """Tests Gauss-Legendre with a polynomial function."""
        x = Symbol('x')
        f = sympify("x**3 + 15")
        stopnja = 3
        a = 2
        b = 7
        expected_integral = 2685/4  # Solution for the definite integral
        integral, error = Gauss_Legendre(f, stopnja, x, a, b)
        self.assertAlmostEqual(integral + error, expected_integral, places=5)






#--------------------------------TEST SESTAVLJENEGA PRAVILA----------------------------------------------------------

class Test_Trapezoidal_polynomial_1(unittest.TestCase):

    def test_polynomial_function_4(self):
        """Tests Trapezoid rule with a polynomial function."""
        # f(x) = x**4 + 3
        N = 13000
        a = 1
        b = 4
        expected_integral = 213.6  # Analytical solution for the definite integral
        integral, error = trapez_int(f_x4_3,a,b,N)
        self.assertAlmostEqual(integral + error, expected_integral, places=5)


class Test_Trapezoidal_polynomial_2(unittest.TestCase):

    def test_polynomial_function_5(self):
        """Tests Trapezoid rule with a polynomial function."""
        # f = x**3 + 15
        N = 10000
        a = 2
        b = 7
        expected_integral = 2685/4  # Analytical solution for the definite integral

        integral, error = trapez_int(f_x3_15,a,b,N)
        self.assertAlmostEqual(integral, expected_integral, places=5)



#--------------------------------TEST SESTAVLJENEGA PRAVILA sin(x) / x----------------------------------------------------------

class Test_Trapezoidal_polynomial_3(unittest.TestCase):

    def test_polynomial_function_6(self):
        """Tests Trapezoid rule with a polynomial function."""
        # f = sin(x)/x
        N = 10000
        a = 0
        b = 5
        expected_integral = 1.549931245  # Analytical solution for the definite integral

        integral, error = trapez_int_sin(sin_div_x,a,b,N)
        self.assertAlmostEqual(integral, expected_integral, places=5)






#--------------------------------TEST GAUSS-LEGENDREOVEGA ALGORITMA - SESTAVLJENO PRAVILO----------------------------------------------------------

class TestGaussLegendre_Composition_1(unittest.TestCase):

    def test_Gauss_Legendre_comp_1(self):
        """Tests Gauss-Legendre composition rule"""
        x = Symbol('x')
        f = sympify("x**4+3")
        stopnja = 4
        a = 1
        b = 4
        N = 100
        expected_integral = 213.6  # Solution for the definite integral
        integral, error1 = GL_composite_int(f, stopnja, x, a, b, N)
        self.assertAlmostEqual(integral , expected_integral, places=5)



class TestGaussLegendre_Composition_2(unittest.TestCase):

    def test_Gauss_Legendre_comp_2(self):
        """Tests Gauss-Legendre with a polynomial function."""
        x = Symbol('x')
        f = sin(x)/x
        stopnja = 0
        a = 0
        b = 5
        N = 100
        expected_integral = 1.549931245  # Analytical solution for the definite integral
        integral, error = GL_composite_int(f, stopnja, x, a, b, N)
        self.assertAlmostEqual(integral , expected_integral, places=5)



if __name__ == "__main__":
    unittest.main()