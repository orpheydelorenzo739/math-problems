def solve_math_problems():
    # Example of solving a simple algebraic equation
    import sympy as sp
    x = sp.symbols('x')
    equation = sp.Eq(x**2 - 4*x + 3, 0)
    solution = sp.solve(equation, x)
    print(solution)

solve_math_problems()
