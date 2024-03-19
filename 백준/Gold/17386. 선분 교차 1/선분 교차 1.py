# 17386 - 선분 교차 1

import sys
input = sys.stdin.readline

a1, a2, b1, b2 = map(int, input().split())
c1, c2, d1, d2 = map(int, input().split())

if (a1*b2+b1*c2+c1*a2 - (a1*c2+c1*b2+b1*a2)) * (a1*b2+b1*d2+d1*a2 - (a1*d2+d1*b2+b1*a2)) <= 0 \
        and (c1*d2+d1*a2+a1*c2 - (c1*a2+a1*d2+d1*c2)) * (c1*d2+d1*b2+b1*c2 - (c1*b2+b1*d2+d1*c2)) <= 0:
    print(1)
else:
    print(0)
