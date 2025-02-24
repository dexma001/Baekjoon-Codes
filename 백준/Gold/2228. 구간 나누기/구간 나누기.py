#2228

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(int(input()))
    
if n == 1 or n == 2:
    print(max(arr))

else:    
    dp = list(list(-2000000 for _ in range(n)) for _ in range(m))
    dp[0][0] = arr[0]

    for i in range(1, n):
        for j in range(min(math.ceil((i-1)/2), m-1)+1):
            if j == 0:
                dp[j][i] = max(arr[i], dp[j][i-1] + arr[i])
            else:
                for k in range(i-1):
                    dp[j][i] = max(dp[j][i], dp[j-1][k] + arr[i])
                dp[j][i] = max(dp[j][i], dp[j][i-1] + arr[i])
                
    print(max(dp[-1]))