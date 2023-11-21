# 11444

import sys
sys.setrecursionlimit(10**7)

x = int(sys.stdin.readline().strip())


def matrix_mult(a, b):
    temp = [(a[0]*b[0]+a[1]*b[2]) % 1000000007, (a[0]*b[1]+a[1]*b[3]) % 1000000007,
            (a[2]*b[0]+a[3]*b[2]) % 1000000007, (a[2]*b[1]+a[3]*b[3]) % 1000000007]
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


a = [1, 1, 1, 0]

print(matrix_pow(x, a)[1])
