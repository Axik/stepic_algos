import sys


def fib(n):
    a, b = 1, 1
    n = int(n)
    if n >= 2:
        yield a
        yield b
        for _ in range(2, n):
            summator = a + b
            yield summator
            a = b
            b = summator
    else:
        yield a


if __name__ == '__main__':
    inp = sys.stdin.readline()
    print(list(fib(inp))[-1])
