  import random

def get_random_code():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    op = ["+", "-", "*", "/"][random.randint(0, 3)]
    return f"{x} {op} {y}"