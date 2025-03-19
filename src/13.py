
import random

def get_random_code():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operators = ["+", "-", "*", "/"]
    variables = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    code = ""
    for i in range(0, 5):
        code += variables[random.randint(0, 24)] + operators[random.randint(0, 3)] + numbers[random.randint(0, 8)] + "=" + numbers[random.randint(0, 8)]
    return code