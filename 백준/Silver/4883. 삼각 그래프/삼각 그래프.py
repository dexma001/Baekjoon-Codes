# 4883

import sys
input = sys.stdin.readline

j = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr = list(map(int, input().split()))
        dp = [10**10, arr[1], arr[1]+arr[2]]

        for _ in range(n-1):
            arr = list(map(int, input().split()))
            temp_dp = [0, 0, 0]
            temp_dp[0] = min(dp[0], dp[1]) + arr[0]
            temp_dp[1] = min(dp[0], dp[1], dp[2], temp_dp[0]) + arr[1]
            temp_dp[2] = min(dp[1], dp[2], temp_dp[1]) + arr[2]

            dp = temp_dp

        print('{}. {}'.format(j, dp[1]))
        j += 1
