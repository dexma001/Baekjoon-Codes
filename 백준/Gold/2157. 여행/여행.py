# 2157

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

dp = list(list(0 for _ in range(n+1)) for _ in range(m+1))

line = list()
for _ in range(k):
    a, b, c = map(int, input().split())
    if a > b:
        continue
    line.append([a, b, c])

line.sort(key=lambda x: [x[0], x[1], -x[2]])
visited = list(0 for _ in range(n+1))

for i, j, k in line:
    if i == 1:
        for p in range(m):
            dp[p+1][j] = max(dp[p+1][j], k)
    else:
        for p in range(m):
            if dp[p][i]:
                dp[p+1][j] = max(dp[p+1][j], dp[p][i] + k)
            else:
                if visited[i]:
                    dp[p+1][j] = max(dp[p+1][j], k)

answer = 0
for p in range(m):
    answer = max(answer, dp[p][-1])

print(answer)
