# 2616

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
max_carry = int(input())

perfix_sum = list(0 for _ in range(n-max_carry+2))
perfix_sum[1] = sum(arr[1:max_carry+1])
for i in range(2, n-max_carry+2):
    perfix_sum[i] = perfix_sum[i-1] - arr[i-1] + arr[i+max_carry-1]

dp = list([0] * (n-max_carry+2) for _ in range(4))

for i in range(3, 0, -1):
    if i == 3:
        dp[i][n-(max_carry*(4-i))+1] = perfix_sum[-1]
    else:
        dp[i][n-(max_carry*(4-i))+1] = perfix_sum[n -
                                                  (max_carry*(4-i))+1] + dp[i+1][n-max_carry*(3-i)+1]
    for j in range(n-(max_carry)*(4-i), 0, -1):
        if i == 3:
            dp[i][j] = max(dp[i][j+1], perfix_sum[j])
        else:
            dp[i][j] = max(dp[i][j+1], dp[i+1][j+max_carry] + perfix_sum[j])

print(dp[1][1])
