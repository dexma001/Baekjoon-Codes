# 16161

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
temp_arr = list(map(int, input().split()))
arr = list()
for i in range(n):
    arr.append(0)
    arr.append(temp_arr[i])
arr.append(0)

dp = list(0 for _ in range(2*n+1))
r, p = 0, 0

for i in range(2*n+1):
    if i <= r:
        dp[i] = min(dp[2*p-i], r-i)
    else:
        pass

    temp = arr[i]
    while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < 2*n+1 and arr[i - dp[i] - 1] == arr[i + dp[i] + 1]:
        if temp == 0:
            temp = arr[i-dp[i]-1]
            dp[i] += 1
        else:
            if arr[i-dp[i] - 1] == 0:
                dp[i] += 1
            else:
                if arr[i - dp[i] - 1] >= temp:
                    break
                temp = arr[i-dp[i] - 1]
                dp[i] += 1

    if r < i + dp[i]:
        p = i
        r = p + dp[p]

print(max(dp))
