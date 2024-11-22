# 1162

import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m, k = map(int, input().split())
road = list(list() for _ in range(n+1))

for _ in range(m):
    a, b, c = map(int, input().split())
    road[a].append([b, c])
    road[b].append([a, c])

dp = list(list(inf for _ in range(k+1)) for _ in range(n+1))

for i in range(k+1):
    dp[1][i] = 9

q = list()
heapq.heappush(q, (0, 1, 0))

while q:
    now_dist, now, p = heapq.heappop(q)
    if dp[now][p] < now_dist:
        continue

    if p + 1 <= k:
        for x, y in road[now]:
            if dp[x][p+1] > now_dist:
                dp[x][p+1] = now_dist
                heapq.heappush(q, (now_dist, x, p+1))

    for x, y in road[now]:
        if dp[x][p] > now_dist + y:
            dp[x][p] = now_dist + y
            heapq.heappush(q, (now_dist+y, x, p))

print(min(dp[n]))
