import sys
from functools import lru_cache


@lru_cache(maxsize=1024)
def fib_mod_large_(n, m):
    """Compute the nth Fibonacci number mod m."""
    n, m = int(n), int(m)
    if n <= 3:
        return (0, 1, 1, 2)[n] % m
    elif n % 2 == 0:
        a = fib_mod_large_(n // 2 - 1, m)
        b = fib_mod_large_(n // 2, m)
        return ((2 * a + b) * b) % m
    else:
        a = fib_mod_large_(n // 2, m)
        b = fib_mod_large_(n // 2 + 1, m)
        return (a * a + b * b) % m

if __name__ == '__main__':
    inp = sys.stdin.readline().split(' ')
    print(fib_mod_large_(*inp))
