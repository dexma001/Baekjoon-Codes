# 1082

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

dp = list('0' for _ in range(m+1))

for i in range(m, -1, -1):
    for j in range(n):
        if i - arr[j] >= 0:
            dp[i-arr[j]] = str(max(int(dp[i-arr[j]]), int(dp[i]+str(j))))

answer = 0
for i in dp:
    answer = max(answer, int(i))

print(answer)
