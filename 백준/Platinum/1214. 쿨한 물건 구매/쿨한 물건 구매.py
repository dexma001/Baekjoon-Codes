#1214

import sys
import math
input = sys.stdin.readline

d, p, q = map(int, input().split())
if p >= q:
    t = p
    p = q
    q = t

answer = math.ceil(d/q) * q
temp = math.ceil(d/q) * q
cnt = math.ceil(d/q)

for i in range(1, cnt+1):
    if answer == d:
        break

    else:
        temp -= abs(q-p)
        while temp < d:
            temp += p
        answer = min(answer, temp)

print(answer)
