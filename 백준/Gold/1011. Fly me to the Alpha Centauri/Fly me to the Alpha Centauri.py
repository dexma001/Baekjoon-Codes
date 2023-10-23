import sys
import math

n = int(input())


def sqr(a, b):
    c = b - a
    if float(math.sqrt(c)).is_integer() == True:
        print(int(2*int(math.sqrt(c)) - 1))
    else:
        p = int(math.sqrt(c))
        q = p + 1

        if p**2 < c <= (int((p**2+q**2)/2)):
            print(int(2*p))
        elif (int(p**2+q**2)/2) < c < q**2:
            print(int(2*q-1))


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    sqr(a, b)
