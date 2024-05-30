import unittest
import numpy as np
from sympy import Symbol, sympify  # Assuming you use SymPy for symbolic expressions
import sympy as sy 
import sys

sys.path.append('.')
from src.Gauss_Legendre import Gauss_Legendre
from src.Trapez_integration import trapez_int, trapez_int_sin, sin_div_x


# The function to be integrated: x**4 + 3
def f_x4_3(x):
    return x**4 + 3


def f_x3_15(x):
    return x**3 + 15



#--------------------------------TEST GAUSS-LEGENDOVEGA ALGORITMA----------------------------------------------------------

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

    def test_polynomial_function_3(self):
        """Tests Trapezoid rule with a polynomial function."""
        # f(x) = x**4 + 3
        N = 13000
        a = 1
        b = 4
        expected_integral = 213.6  # Analytical solution for the definite integral
        integral, error = trapez_int(f_x4_3,a,b,N)
        self.assertAlmostEqual(integral + error, expected_integral, places=5)


class Test_Trapezoidal_polynomial_2(unittest.TestCase):

    def test_polynomial_function_3(self):
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

    def test_polynomial_function_3(self):
        """Tests Trapezoid rule with a polynomial function."""
        # f = sin(x)/x
        N = 10000
        a = 0
        b = 5
        expected_integral = 1.549931245  # Analytical solution for the definite integral

        integral, error = trapez_int_sin(sin_div_x,a,b,N)
        self.assertAlmostEqual(integral, expected_integral, places=5)



if __name__ == "__main__":
    unittest.main()