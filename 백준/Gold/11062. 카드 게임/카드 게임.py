#11062

import sys
input = sys.stdin.readline

def solve(left, right, turn):
        if left > right:
            return 0
        
        if dp[left][right]:
            return dp[left][right]
        
        if turn == 1:
            dp[left][right] = max(arr[left] + solve(left+1, right, 0), arr[right] + solve(left, right-1, 0))
            return dp[left][right]
        
        else:
            dp[left][right] = min(solve(left, right-1, 1), solve(left+1, right, 1))
            return dp[left][right]
for _ in range(int(input())):
    leng = int(input())
    arr = [0] + list(map(int, input().split()))
    
    dp = list(list(0 for _ in range(leng +1)) for _ in range(leng+1))
    solve(1, leng, 1)
    print(dp[1][leng])
    
    