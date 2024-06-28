# 17485

import sys
input = sys.stdin.readline
INF = 10**10

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = list(list([INF, INF, INF] for _ in range(m)) for _ in range(n))

for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j] = [arr[i][j], arr[i][j], arr[i][j]]
        else:
            for k in range(3):
                if j == 0 and k == 0:
                    continue
                elif j == m-1 and k == 2:
                    continue
                else:
                    dp[i][j][k] = min(dp[i-1][j+(-1+k)][(k+1) %
                                                        3], dp[i-1][j+(-1+k)][(k+2) % 3]) + arr[i][j]

answer = INF
for i in dp[-1]:
    answer = min(answer, i[0], i[1], i[2])

print(answer)
