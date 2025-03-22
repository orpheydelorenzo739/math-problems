import numpy as np

def calculate_sums(a):
    """
    This function takes an array 'a' and returns a list of sums.
    
    Example usage:
    >>> calculate_sums([1, 2, 3, 4])
    [6, 9, 12]
    >>> calculate_sums([5, -1, 0, 7])
    [0, 5, 7]
    """
    sums = []
    for i in a:
        sums.append(i + i)
    return sums

# Example usage
a = np.array([1, 2, 3, 4])
result = calculate_sums(a)
print(result)
