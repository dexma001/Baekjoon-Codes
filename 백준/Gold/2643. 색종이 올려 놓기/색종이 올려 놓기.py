#2643

import sys
input = sys.stdin.readline

arr = list()
n = int(input())
for _ in range(n):
    temp= list(map(int, input().split()))
    temp.sort()
    arr.append(temp)
    
arr.sort(key=lambda x:[x[0], x[1]])
dp = list(0 for _ in range(n))
dp[0] = 1

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if arr[i][0] >= arr[j][0] and arr[i][1] >= arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] == 0:
        dp[i] = 1

print(max(dp))