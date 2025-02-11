#1577

import sys
input = sys.stdin.readline

n,m=map(int, input().split())
dp = list(list([0, 0] for _ in range(m+1)) for _ in range(n+1))
dp[0][0] = [1, 0]

for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    
    if a>c or b>d:
        x,y=c,d
        c,d=a,b
        a,b=x,y
        
    if c >a:
        dp[c][d][1] = -1
    else:
        dp[c][d][0] = -1
        

for i in range(n+1):
    for j in range(m+1):
        if dp[i][j][0] != -1:
            dp[i][j][0] += sum(dp[i][j-1]) + dp[i][j-1].count(-1)
        if dp[i][j][1] != -1:
            dp[i][j][1] += sum(dp[i-1][j]) + dp[i-1][j].count(-1)
            
            
print(sum(dp[n][m]) + dp[n][m].count(-1))