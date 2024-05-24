# 5582

import sys
input = sys.stdin.readline

str1 = [0] + list(map(str, input().rstrip()))
str2 = [0] + list(map(str, input().rstrip()))
n = len(str1)-1
m = len(str2)-1

dp = list([0] * (len(str2)+1) for _ in range(len(str1)+1))

answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            continue
    answer = max(answer, max(dp[i]))

print(answer)
