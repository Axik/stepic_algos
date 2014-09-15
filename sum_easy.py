import sys


def sum_(x, y):
    return int(x) + int(y)

if __name__ == '__main__':
    inp = sys.stdin.readline().split(' ')
    print(sum_(*inp))
