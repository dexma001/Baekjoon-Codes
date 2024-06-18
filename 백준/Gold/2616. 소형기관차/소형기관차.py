# 2616
# 기관차는 모두 3대

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]+list(map(int, input().split()))
carry = int(input())

perfix_sum = list(0 for _ in range(n-carry+2))
perfix_sum[1] = sum(arr[1:carry+1])
for i in range(2, n-carry+2):
    perfix_sum[i] = perfix_sum[i-1] - arr[i-1] + arr[i+carry-1]

dp = list([0]*(n-carry+2) for _ in range(4))

dp[3][n-carry+1] = perfix_sum[-1]
for i in range(n-carry, 0, -1):
    dp[3][i] = max(dp[3][i+1], perfix_sum[i])

dp[2][n-carry*2+1] = perfix_sum[n-carry*2+1] + dp[3][-1]
for i in range(n-carry*2, 0, -1):
    dp[2][i] = max(dp[2][i+1], dp[3][i+carry] + perfix_sum[i])


dp[1][n-carry*3+1] = perfix_sum[n-carry*3+1] + dp[2][n-carry*2+1]
for i in range(n-carry*3, 0, -1):
    dp[1][i] = max(dp[1][i+1], dp[2][i+carry] + perfix_sum[i])


print(dp[1][1])
