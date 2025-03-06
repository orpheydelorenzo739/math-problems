
import random

def get_random_code(length):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([alphabet[random.randint(0, len(alphabet) - 1)] for i in range(length)])

get_random_code(5)