# 17218

import sys
input = sys.stdin.readline

n = [''] + list(map(str, input().rstrip()))
m = [''] + list(map(str, input().rstrip()))

len_n = len(n)-1
len_m = len(m)-1

dp = list(list(0 for _ in range(len_n+1)) for _ in range(len_m+1))
backTrack = list(list(0 for _ in range(len_n+1)) for _ in range(len_m+1))

for i in range(1, len_m+1):
    for j in range(1, len_n+1):
        if m[i] == n[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            backTrack[i][j] = 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            backTrack[i][j] = 2 if dp[i-1][j] > dp[i][j-1] else 3

result = ""

i == len_m
j == len_n

while i > 0 and j > 0:
    if backTrack[i][j] == 1:
        result += n[j]
        i, j = i-1, j-1
    elif backTrack[i][j] == 2:
        i -= 1
    else:
        j -= 1

print(result[::-1])
