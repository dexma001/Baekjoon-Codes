# 12920

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()

for _ in range(n):
    i, j, k = map(int, input().split())
    idx = 1
    while k > 0:
        temp = min(idx, k)
        arr.append([i*temp, j*temp])
        idx *= 2
        k -= temp

table = list(0 for _ in range(m+1))
for w, v in arr:
    if w > m:
        continue
    for j in range(m, 0, -1):
        if j + w <= m and table[j] != 0:
            table[j+w] = max(table[j+w], table[j] + v)
    table[w] = max(table[w], v)

print(max(table))
