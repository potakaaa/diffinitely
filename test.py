import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, integrate

def plot_definite_integral():
    x = symbols('x')
    
    f_expr = 8*x - 2*x**2
    
    f = lambdify(x, f_expr, modules=['numpy'])

    a, b = 0, 4 

    x_vals = np.linspace(a, b, 500)

    y_vals = f(x_vals)

    integral_value = integrate(f_expr, (x, a, b))

    mask = y_vals >= 0
    x_shade = x_vals[mask]
    y_shade = y_vals[mask]

    plt.plot(x_vals, y_vals, label="f(x) = 8x - 2x²")
    
    plt.fill_between(x_shade, y_shade, 0, where=mask, alpha=0.4, color='orange', label=f"Area under curve: {integral_value}")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.title(f"Definite Integral: ∫[{a}, {b}] f(x) dx")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    plt.show()


plot_definite_integral()
