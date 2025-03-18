import random

def get_random_code():
    # Generate a random number between 1 and 10
    x = random.randint(1, 10)
    # Generate a random operation (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])
    # Generate a random number between 1 and 10
    y = random.randint(1, 10)
    # Evaluate the expression
    z = eval(f"{x}{op}{y}")
    return f"{x} {op} {y} = {z}"