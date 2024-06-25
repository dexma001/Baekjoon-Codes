# 25644

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

if n == 1:
    print(0)
else:
    dp = list(0 for _ in range(n+1))
    dp[1] = 0
    temp = arr[1]
    answer = 0

    for i in range(2, n+1):
        if arr[i] >= temp:
            dp[i] = arr[i] - temp
            answer = max(answer, dp[i])
        else:
            temp = arr[i]

    print(answer)
