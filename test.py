import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

x = sp.symbols('x')

f1 = "x**2 + 2*x + 1"

f1 = parse_expr(f1)
f1_diff = sp.diff(f1, x)
f1_n_diff = sp.diff(f1, x, 10)
f1_integral = sp.integrate(f1, x)

print("Original function: ", f1)
print("First derivative: ", f1_diff)
print("Nth derivative: ", f1_n_diff)
print("Integral: ", f1_integral)

