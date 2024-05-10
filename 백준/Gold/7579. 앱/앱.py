#7579

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bites = [0] + list(map(int, input().split()))
unactive = [0] + list(map(int, input().split()))
dp = list([0]*(sum(unactive)+1) for _ in range(n+1))

answer = 10**8
for i in range(1, n+1):
    x, y = bites[i], unactive[i]

    for j in range(1, sum(unactive) + 1):
        dp[i][j] = dp[i-1][j]
    for j in range(y, sum(unactive)+1):
        dp[i][j] = max(dp[i][j], x + dp[i-1][j-y])
        if dp[i][j] >= m:
            answer = min(answer, j)

if m != 0:
    print(answer)
else:       
    print(0)