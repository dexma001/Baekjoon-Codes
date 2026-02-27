import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = list(list(0 for _ in range(m+1)) for _ in range(n+1))
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
#왼, 위, 대
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = arr[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]
        
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    
    print(dp[c][d] - dp[c][b-1] - dp[a-1][d] + dp[a-1][b-1])