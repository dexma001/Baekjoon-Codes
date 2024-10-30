# 4233

import math
import sys
input = sys.stdin.readline


def power(a, b, mod):
    result = 1
    while b:
        if b & 1:
            result *= a
            result %= mod
        a *= a % mod
        b = b >> 1
    return result


def prime(a):
    for i in range(2, math.floor(math.sqrt(a))):
        if a % i == 0:
            return False
    else:
        return True


while True:
    a, b = map(int, input().split())
    mod = a
    if a == 0 and b == 0:
        break
    if prime(a):
        print('no')
    else:
        temp = power(b, a, mod)
        if temp == b:
            print('yes')
        else:
            print('no')
