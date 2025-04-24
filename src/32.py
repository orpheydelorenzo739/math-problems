import sympy as sp
from sympy import symbols

x = symbols('x')
expression = x**3 - 2*x + 1
solution = sp.solve(expression, x)
print(solution)
