# 1788

import sys
input = sys.stdin.readline

n = int(input())
if n > 0:
    print(1)
    if n < 3:
        print(1)
    else:
        a = 1
        b = 1
        for _ in range(n-2):
            c = a+b
            a = b
            b = c
        print(c % 1000000000)

elif n == 0:
    print(0)
    print(0)
else:
    if n == -1:
        print(1)
        print(1)
    elif n == -2:
        print(-1)
        print(1)
    else:
        a = 1  # -1
        b = -1  # -2
        for _ in range(abs(n)-2):
            c = a - b
            a = b
            b = c
        if c > 0:
            print(1)
            print(abs(c) % 1000000000)
        elif c == 0:
            print(0)
            print(0)
        else:
            print(-1)
            print(abs(c) % 1000000000)
