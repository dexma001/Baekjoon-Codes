# 6064

import sys
input = sys.stdin.readline


def num(n, m, x, y):
    while x <= n*m:
        if (x-y) % m == 0:
            return x
        x += n
    return -1


for _ in range(int(input())):
    n, m, x, y = list(map(int, input().split()))
    print(num(n, m, x, y))
