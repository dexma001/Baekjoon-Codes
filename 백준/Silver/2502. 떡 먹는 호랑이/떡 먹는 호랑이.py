# 2502

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = 1
b = 1

for _ in range(n-3):
    c = a+b
    a = b
    b = c

for i in range(1, m//a+1):
    if (m - (i*a)) % b == 0:
        print(i)
        print((m-(i*a)) // b)
        break
