import sys
input = sys.stdin.readline

n = int(input())
arr =list(map(str, input().strip()))
dp = list(1e9 for _ in range(n))
dp[0] = 0

for i in range(n):
    if arr[i] == 'B':
        for j in range(i-1, -1, -1):
            if arr[j] == 'J':
                dp[i] = min(dp[i], dp[j] + (i-j)**2)
    elif arr[i] == 'O':
        for j in range(i-1, -1, -1):
            if arr[j] == 'B':
                dp[i] = min(dp[i], dp[j] + (i-j)**2)
    else:
        for j in range(i-1, -1, -1):
            if arr[j] == 'O':
                dp[i] = min(dp[i], dp[j] + (i-j)**2)
                
print(dp[-1]) if dp[-1] != 1e9 else print(-1)