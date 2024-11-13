# 1446

import sys
input = sys.stdin.readline

n, d = map(int, input().split())
shortcut = list()
for _ in range(n):
    shortcut.append(list(map(int, input().split())))
shortcut.sort(key=lambda x: (x[0], x[1], x[2]))

dijk = list(i for i in range(d+1))

for i, j, k in shortcut:
    if i <= d and j <= d:
        dijk[j] = min(dijk[j], dijk[i] + k)
        for p in range(j+1, d+1):
            dijk[p] = min(dijk[p], dijk[p-1] + 1)

print(dijk[d])
