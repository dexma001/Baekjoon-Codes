# 11048

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
maze = [[0] * (m+1)]
for i in range(n):
    maze.append([0] + list(map(int, input().split())))

dp = list([0] * (m+1) for _ in range(n+1))
dp[1][1] = maze[1][1]

for i in range(2, m+1):
    dp[1][i] = dp[1][i-1] + maze[1][i]

for i in range(2, n+1):
    for j in range(1, m+1):
        if j == 1:
            dp[i][j] = dp[i-1][j] + maze[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i][j]

print(dp[n][m])
