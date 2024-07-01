# 4153

import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b

    if a**2 == (b**2 + c**2):
        print('right')
    else:
        print('wrong')
