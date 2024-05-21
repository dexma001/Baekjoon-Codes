# 2011

import sys
input = sys.stdin.readline

arr = [0] + list(map(int, list(input().rstrip())))
dp = list([0] * (len(arr)) for _ in range(2))

if arr[1] == 0:
    print(0)
    quit()

if len(arr) == 2:
    print(1)
    quit()

dp[0][1] = 1
dp[1][1] = 0

if arr[2] == 0:
    dp[0][2] = 0
else:
    dp[0][2] = 1

if 1 <= int(str(arr[1]) + str(arr[2])) <= 26:
    dp[1][2] = 1
else:
    dp[1][2] = 0

for i in range(3, len(arr)):
    if arr[i] == 0:
        dp[0][i] = 0
        if 1 <= int(str(arr[i-1]) + str(arr[i])) <= 26 and int(str(arr[i-1]) + str(arr[i])) != arr[i]:
            dp[1][i] = (dp[0][i-2] + dp[1][i-2]) % 1000000
        else:
            dp[1][i] = 0
    else:
        dp[0][i] = (dp[0][i-1] + dp[1][i-1]) % 1000000
        if 1 <= int(str(arr[i-1]) + str(arr[i])) <= 26 and int(str(arr[i-1]) + str(arr[i])) != arr[i]:
            dp[1][i] = (dp[0][i-2] + dp[1][i-2]) % 1000000
        else:
            dp[1][i] = 0

print((dp[0][-1] + dp[1][-1]) % 1000000)
