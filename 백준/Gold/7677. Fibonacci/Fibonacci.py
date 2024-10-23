# 7677

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def matrix_mult(a, b):
    temp = [(a[0]*b[0]+a[1]*b[2]) % 10000, (a[0]*b[1]+a[1]*b[3]) % 10000,
            (a[2]*b[0]+a[3]*b[2]) % 10000, (a[2]*b[1]+a[3]*b[3]) % 10000]
    return temp


def matrix_pow(n, m):
    if n == 1:
        return m
    else:
        temp = matrix_pow(n//2, m)
        if n % 2 == 0:
            return matrix_mult(temp, temp)
        else:
            return matrix_mult(matrix_mult(temp, temp), m)


while True:
    a = [1, 1, 1, 0]
    k = int(input())
    if k == -1:
        break
    elif k == 0:
        print(0)
    else:
        print(matrix_pow(k, a)[1] % 10000)
