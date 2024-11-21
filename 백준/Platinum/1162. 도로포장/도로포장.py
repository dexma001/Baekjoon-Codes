# 1162

import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
road = list(list() for _ in range(n+1))
for _ in range(m):
    a, b, c = map(int, input().split())
    road[a].append([b, c])
    road[b].append([a, c])
inf = sys.maxsize

dp = list(list(inf for _ in range(n+1)) for _ in range(k+1))

for i in range(k+1):
    dp[i][1] = 0

q = list()
heapq.heappush(q, (0, 1, 0))

while q:
    now_dist, now, p = heapq.heappop(q)
    if dp[p][now] < now_dist:
        continue

    if p + 1 <= k:
        for x, y in road[now]:
            if dp[p+1][x] > now_dist:
                dp[p+1][x] = now_dist
                heapq.heappush(q, (now_dist, x, p+1))

    for x, y in road[now]:
        if dp[p][x] > now_dist + y:
            dp[p][x] = now_dist + y
            heapq.heappush(q, (dp[p][x], x, p))

ans = inf
for i in range(k+1):
    ans = min(ans, dp[i][-1])

print(ans)
