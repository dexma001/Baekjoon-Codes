# 4781

import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if n == 0:
        break
    m = m * 100 + 0.5
    n = int(n)
    m = int(m)

    arr = list()
    for _ in range(n):
        a, b = map(float, input().split())
        b = b*100 + 0.5
        arr.append([int(a), int(b)])
    arr.sort(reverse=True)

    dp = list(0 for _ in range(m+1))
    for i in range(1, n+1):
        for j in range(arr[i-1][1], m+1):
            dp[j] = max(dp[j], arr[i-1][0] + dp
                        [j-arr[i-1][1]])

    print(dp[m])
