import sys
import time
from functools import lru_cache


@lru_cache(maxsize=4096)
def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a * d + b * e, a * e + b * f, b * e + c * f


@lru_cache(maxsize=4096)
def _pow(A, n):
    if n == 1:
        return A
    if n & 1 == 0:
        return _pow(mul(A, A), n // 2)
    else:
        return mul(A, _pow(mul(A, A), (n - 1) // 2))


@lru_cache(maxsize=4096)
def fib(n):
    if n < 2:
        return n
    return _pow((1, 1, 0), n - 1)[0]


if __name__ == '__main__':
    inp = sys.stdin.readline()
    t = time.time()
    print(fib(int(inp)))
    print(t - time.time())
