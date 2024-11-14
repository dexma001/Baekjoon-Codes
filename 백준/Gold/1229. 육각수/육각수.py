# 1229

import sys
input = sys.stdin.readline

hex = 1
ap = 1

dp = list(0 for _ in range(1000001))
dp[1] = 1


def get_hex(limit):
    n = 1
    cur = 0
    ans = list()
    while cur <= limit:
        cur = n*(2*n-1)
        ans.append(cur)
        n += 1
    return ans[:-1]


def solution():
    n = int(input())

    hex = get_hex(n)
    for i in range(2, n+1):
        min_val = 10**9
        for h in hex:
            if h > i:
                break
            min_val = min(min_val, dp[i-h])
        dp[i] = min_val+1

    print(dp[n])


solution()
