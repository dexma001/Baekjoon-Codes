# 18291

import sys
input = sys.stdin.readline
mod = 10**9 + 7
sys.setrecursionlimit(10**9)


def power(a, b):
    result = 1
    while b:
        if b & 1:
            result *= a
            result %= mod
        a = (a*a) % mod
        b = b >> 1
    return result


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(power(2, n-2))
