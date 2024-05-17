# 12852

import sys
sys.setrecursionlimit(10**8)

n = int(input())
cnt = [0, 0, 1, 1] + [0] * (n-3)
dp = [[] for _ in range(n+1)]
dp[1] = [1]


if n == 1:
    print(cnt[n])
    print(*dp[n])

else:
    for i in range(2, n+1):
        cnt[i] = cnt[i-1] + 1
        dp[i] = dp[i-1] + [i]

        if i % 3 == 0 and cnt[i//3]+1 < cnt[i]:
            cnt[i] = cnt[i//3] + 1
            dp[i] = dp[i//3] + [i]
        if i % 2 == 0 and cnt[i//2]+1 < cnt[i]:
            cnt[i] = cnt[i//2] + 1
            dp[i] = dp[i//2] + [i]

    print(cnt[n])
    dp[n].reverse()
    print(*dp[n])
