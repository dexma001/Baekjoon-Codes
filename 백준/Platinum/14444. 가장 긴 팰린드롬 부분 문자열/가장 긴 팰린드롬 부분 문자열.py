# 14444

import sys
input = sys.stdin.readline

s = str(input())
arr = list()
for i in range(len(s)):
    arr.append('#')
    arr.append(s[i])
arr.append('#')

length = len(arr)
dp = list(0 for _ in range(length))
middle, radius = 0, 0

for i in range(length):
    if i <= radius:
        dp[i] = min(dp[2*middle - i], radius - i)

    while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < length and arr[i - dp[i] - 1] == arr[i + dp[i] + 1]:
        dp[i] += 1

    if radius < i + dp[i]:
        middle = i
        radius = middle + dp[middle]

print(max(dp))
