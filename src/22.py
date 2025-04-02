def find_gcd(a: int, b: int) -> int:
    """
    Find the greatest common divisor of two integers.
    
    Parameters:
        a (int): The first integer.
        b (int): The second integer.
        
    Returns:
        int: The greatest common divisor of a and b.
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return abs(a)

def gcd(a: int, b: int) -> int:
    return find_gcd(a, b)
