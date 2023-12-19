import sys
input = sys.stdin.readline


def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1

    for i in range(1, n):
        a, b = b, a+b

    return a


n = int(input())
for i in range(n):
    m = int(input())
    if m == 0:
        print(1, 0)
    elif m == 1:
        print(0, 1)
    else:
        print(fib(m-1), fib(m))
