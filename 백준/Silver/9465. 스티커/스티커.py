#9465

import sys
input = sys.stdin.readline

for _ in range (int(input())):
    m = int(input())
    arr = list()
    
    for _ in range(2):
        arr.append(list(map(int, input().split())))
        
    dp = list(list(0 for _ in range(m)) for _ in range(2))
    
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if m == 1:
        print(max(arr[0][0], arr[1][0]))    
        continue
    
    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]    
    if m == 2:
        print(max(dp[0][1], dp[1][1]))
        continue
    
    else:
        for i in range(2, m):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2] )+ arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
            
    print(max(dp[0][m-1], dp[1][m-1]))