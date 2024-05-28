# 2563

import sys
input = sys.stdin.readline

answer = 0

dp = list([0] * 100 for _ in range(100))

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a-1, a+9):
        for j in range(b-1, b+9):
            if dp[i][j] == 0:
                dp[i][j] = 1
                answer += 1

print(answer)
