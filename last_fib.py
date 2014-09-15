import sys


def fib(n):
    a, b = 1, 1
    n = int(n)
    if n >= 2:
        yield a
        yield b
        for _ in range(2, n):
            summator = a + b
            yield int(str(summator)[-1])
            a = int(str(b)[-1])
            b = int(str(summator)[-1])
    else:
        yield a


if __name__ == '__main__':
    inp = sys.stdin.readline()
    print(list(fib(inp))[-1])
