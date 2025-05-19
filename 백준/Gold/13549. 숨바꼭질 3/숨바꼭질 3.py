# 13549

import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n >= k:
    print(n-k)
else:
    dp = list(10**9 for _ in range(100001))
    arr = list()
    heapq.heappush(arr, (0, n))

    while arr:
        a, b = heapq.heappop(arr)
        if dp[b] != 10**9:
            continue
        dp[b] = a
        if 0 <= b+1 <= 100000:
            heapq.heappush(arr, (a+1, b+1))
        if 0 <= b-1 <= 100000:
            heapq.heappush(arr, (a+1, b-1))
        if 0 <= b*2 <= 100000:
            heapq.heappush(arr, (a, b*2))

    print(dp[k])
