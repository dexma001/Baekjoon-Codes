# 2637

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = list([0] * (n+1) for _ in range(n+1))
visited = [False] * (n+1)

arr = list([] for _ in range(n+1))
topo_edge = list(0 for _ in range(n+1))

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[b].append((a, c))
    topo_edge[a] += 1

temp = list()
for i in range(1, n+1):
    if topo_edge[i] == 0:
        temp.append(i)

while temp:
    r = temp.pop(0)
    for p, q in arr[r]:
        if dp[r].count(0) == n+1:
            dp[p][r] += q
        else:
            for i in range(1, n+1):
                dp[p][i] += dp[r][i] * q

        topo_edge[p] -= 1
        if topo_edge[p] == 0:
            temp.append(p)

for i in range(1, n+1):
    if dp[n][i] != 0:
        print(i, dp[n][i])
