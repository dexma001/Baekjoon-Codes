import math

a, b = map(int, input().split())

p = int(-a + math.sqrt(a ** 2-b))
q = int(-a - math.sqrt(a ** 2 - b))

if p == q:
    print(p)
else:
    if p > q:
        p, q = q, p
        print(p, q)
