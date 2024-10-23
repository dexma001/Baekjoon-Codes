# 18138

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list() for _ in range(n+1))
shirt = [0]
for _ in range(n):
    shirt.append(int(input()))

for j in range(m):
    w = int(input())
    for i in range(1, n+1):
        if shirt[i]*0.5 <= w <= shirt[i]*0.75 or shirt[i] <= w <= shirt[i]*1.25:
            arr[i].append(j+1)

to_use = list(-1 for _ in range(m+1))


def bimatch(i):
    if visited[i]:
        return False
    visited[i] = 1

    for j in arr[i]:
        if to_use[j] == -1 or bimatch(to_use[j]):
            to_use[j] = i
            return True
    return False


for i in range(1, n+1):
    visited = list(0 for _ in range(n+1))
    bimatch(i)

print(m+1 - to_use.count(-1))
