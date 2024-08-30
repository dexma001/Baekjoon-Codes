# 2550

import bisect
import sys
input = sys.stdin.readline

n = int(input())
larr = list(map(int, input().split()))
rarr = list(map(int, input().split()))

d = list(0 for _ in range(n+1))

for i, v in enumerate(rarr):
    d[v] = i+1

lis = list()
idx = list()

for i in larr:
    temp = d[i]

    if len(lis) == 0 or lis[-1] < temp:
        idx.append(len(lis))
        lis.append(temp)

    else:
        index = bisect.bisect_left(lis, temp)
        if len(lis) == index:
            lis.append(temp)
        else:
            lis[index] = temp
        idx.append(index)

print(len(lis))

answer = list()
pos = max(idx)

for j in idx[::-1]:
    n -= 1
    if pos == j:
        answer.append(larr[n])
        pos -= 1

print(*sorted(answer))
