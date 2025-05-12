# 13705

from decimal import *
import sys
input = sys.stdin.readline
getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP

a, b, c = map(Decimal, map(int, input().split()))
pi = Decimal('3.14159265358979323846264338327950288419716939937510')


def sin(x):
    x = x % (2*pi)
    getcontext().prec += 2
    i, last, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != last:
        last = s
        i += 2
        fact *= i * (i-1)
        num *= x*x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


low = (c-b)/a
high = (c+b)/a


while high - low > Decimal(1e-30):
    mid = (high+low)/2
    if a*mid + b*sin(mid) < c:
        low = mid
    else:
        high = mid

print(round(high, 6))
