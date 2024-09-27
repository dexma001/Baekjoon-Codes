# 17387

import sys
input = sys.stdin.readline

a1, a2, b1, b2 = map(int, input().split())
c1, c2, d1, d2 = map(int, input().split())

p1, p2 = [a1, a2], [b1, b2]
p3, p4 = [c1, c2], [d1, d2]


def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - \
        (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])


p12 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
p34 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if p12 == 0 and p34 == 0:
    if min(a1, b1) <= max(c1, d1) and min(c1, d1) <= max(a1, b1) and min(a2, b2) <= max(c2, d2) and min(c2, d2) <= max(a2, b2):
        print(1)
    else:
        print(0)
elif p12 <= 0 and p34 <= 0:
    print(1)
else:
    print(0)
