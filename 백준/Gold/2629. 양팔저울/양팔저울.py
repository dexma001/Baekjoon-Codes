# 2629

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = list()
dp.append(arr[1])

for i in range(2, n+1):
    for j in range(len(dp)):
        k = dp[j]
        if abs(k+arr[i]) <= 15000 and abs(k+arr[i]) not in dp:
            dp.append(abs(k+arr[i]))
        if abs(k-arr[i]) > 0 and abs(k-arr[i]) not in dp:
            dp.append(abs(k-arr[i]))
    if arr[i] not in dp:
        dp.append(arr[i])

m = int(input())
temp = [0] + list(map(int, input().split()))
answer = list()


for i in range(1, m+1):
    if temp[i] in dp:
        answer.append('Y')
    else:
        answer.append('N')

print(*answer)
