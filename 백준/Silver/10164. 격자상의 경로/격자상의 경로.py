# 10164

import sys
import math
input = sys.stdin.readline
fac = math.factorial

n, m, s = map(int, input().split())

if s == 0:
    print(int(fac(n+m-2) / fac(n-1) / fac(m-1)))
else:
    x = s//m + 1
    y = s % m
    print(int(fac(x+y-2) / fac(x-1) / fac(y-1)) *
          int(fac((n-x) + (m-y)) / fac((n-x)) / fac(m-y)))
