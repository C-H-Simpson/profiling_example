"""In this example, we will do a numerical integration 3 times with the same method"""

# Setting up a function to be integrated
import numpy as np
from scipy import integrate
from numpy import polynomial
polynomial_coefficients = [1, 0, 1]
lims = (0, 1)


def function(x):
    """The function that will be integrated.
    Just a polynomial!
    """
    return polynomial.polynomial.polyval(x, polynomial_coefficients)


def true_integral():
    """The true integral of the function, based on it being a polynomial."""
    coeffs = polynomial.polynomial.polyint(polynomial_coefficients)
    y = polynomial.polynomial.polyval(lims, coeffs)
    return y[1] - y[0]


@profile
def integration_01(func, lims, n_points):
    """Integration using the trapezium rule.
    input: func, the function to be integrated
    lims: tuple of limits to integrate between
    n_points: number of points to use for integration

    The algorithm is implemented from scratch, and vectorization is not used.
    It is a little badly written on purpose!
    """
    h = (lims[1] - lims[0]) / (n_points - 1)
    x_points = []
    y_points = []

    running_total = 0

    for i in range(n_points):
        x = lims[0] + h*i
        x_points.append(x)
        y_points.append(func(x))

    for i in range(1, n_points-1):
        running_total += y_points[i]

    integral = 0.5 * h \
        * ((y_points[0] + y_points[-1]) + running_total * 2)

    return integral

@profile
def integration_02(func, lims, n_points):
    """Integration using the trapezium rule.
    input: func, the function to be integrated
    lims: tuple of limits to integrate between
    n_points: number of points to use for integration

    The algorithm is implemented from scratch, but vectorization is used.
    """
    h = (lims[1] - lims[0]) / (n_points - 1)
    x_points = np.linspace(lims[0], lims[1], n_points)
    y_points = func(x_points)

    running_total = np.sum(y_points[1:-1])

    integral = 0.5 * h \
        * ((y_points[0] + y_points[-1]) + running_total * 2)
    return integral

@profile
def integration_03(func, lims, n_points):
    """Integration using the trapezium rule.
    input: func, the function to be integrated
    lims: tuple of limits to integrate between
    n_points: number of points to use for integration

    The algorithm is taken from the scipy library.
    """
    x_points = np.linspace(lims[0], lims[1], n_points)
    y_points = func(x_points)
    integral = np.trapz(y_points, x_points)
    return integral

@profile
def integration_04(func, lims, n_points):
    """Integration using the trapezium rule.
    input: func, the function to be integrated
    lims: tuple of limits to integrate between
    n_points: number of points to use for integration

    The algorithm is taken from the scipy library.
    """
    integral = integrate.quad(func, lims[0], lims[1])
    return integral

n_points = 100000
print("True answer:", true_integral())
print("Integration 1:", integration_01(function, lims, n_points))
print("Integration 2:", integration_02(function, lims, n_points))
print("Integration 3:", integration_03(function, lims, n_points))
print("Integration 4:", integration_04(function, lims, n_points))
