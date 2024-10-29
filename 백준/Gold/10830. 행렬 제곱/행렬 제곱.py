# 10830

import sys
input = sys.stdin.readline

n, b = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))


def matrix_mult(a, b):
    temp = list(list(0 for _ in range(n)) for _ in range(n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][k] += a[i][j] * b[j][k]
                temp[i][k] %= 1000
    return temp


def matrix_pow(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        temp = matrix_pow(a, n//2)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(a, n-1)
        return matrix_mult(temp, a)


answer = matrix_pow(arr, b)
for i in range(n):
    for j in range(n):
        answer[i][j] %= 1000

for i in answer:
    print(*i)
