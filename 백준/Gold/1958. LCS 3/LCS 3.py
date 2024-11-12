# 1958

import sys
input = sys.stdin.readline

a = str(input().strip())
b = str(input().strip())
c = str(input().strip())


dp = list(list(list(0 for _ in range(101))
          for _ in range(101)) for _ in range(101))

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            if a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(a)][len(b)][len(c)])
