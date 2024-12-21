# 1749

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))


ans = 0

for i in range(n):
    p = list(0 for _ in range(m))
    for j in range(i, n):
        t = list(0 for _ in range(m))
        for k in range(m):
            p[k] += arr[j][k]
            if k == 0:
                t[k] = p[k]
            else:
                t[k] = max(t[k-1]+p[k], p[k])
            ans = max(ans, t[k])


print(ans)
