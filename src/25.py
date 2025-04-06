def sum_series(n):
    if n <= 1:
        return n
    else:
        return n + sum_series(n - 1)
