#1006

import sys
input = sys.stdin.readline

def get_dp(start):
    for i in range(start, n):
        dp[i+1][2] = min(dp[i][0] + 1, dp[i][1] + 1)
        
        if arr[0][i] + arr[1][i] <= w:
            dp[i+1][2] = min(dp[i+1][2], dp[i][2] + 1)
        
        if i>0 and arr[0][i-1] + arr[0][i] <= w and arr[1][i-1] + arr[1][i] <= w:
            dp[i+1][2] = min(dp[i+1][2], dp[i-1][2] + 2)
        
        if i == n-1:
            continue
        
        dp[i+1][0] = dp[i+1][2] + 1
        dp[i+1][1] = dp[i+1][2] + 1
        
        if arr[0][i] + arr[0][i+1] <= w:
            dp[i+1][0] = min(dp[i+1][0], dp[i][1] + 1)
        if arr[1][i] + arr[1][i+1] <= w:
            dp[i+1][1] = min(dp[i+1][1], dp[i][0] + 1)
        
        

for _ in range(int(input())):
    n, w = map(int, input().split())
    arr = list()
    for _ in range(2):
        arr.append(list(map(int, input().split())))
        
    dp = list(list(0 for _ in range(3)) for _ in range(n+1))
    dp[0][0] = 1
    dp[0][1] = 1
    get_dp(0)
    
    answer = dp[n][2]
    if n >= 2:
        if arr[0][0] + arr[0][-1] <= w:
            dp[1][2] = 1
            dp[1][0] = 2
            dp[1][1] = 1 if arr[1][0] + arr[1][1]<=w else 2
            get_dp(1)
            answer = min(answer, dp[n-1][1] + 1)
        if arr[1][0] + arr[1][-1] <= w:
            dp[1][2] = 1
            dp[1][0] = 1 if arr[0][0] + arr[0][1]<=w else 2
            dp[1][1] = 2
            get_dp(1)
            answer = min(answer, dp[n-1][0] + 1)
        if arr[1][0] + arr[1][-1] <= w and arr[0][0] + arr[0][-1] <= w:
            dp[1][2] = 0
            dp[1][0] = 1
            dp[1][1] = 1
            get_dp(1)
            answer = min(answer, dp[n-1][2] + 2)
    print(answer)
    
   