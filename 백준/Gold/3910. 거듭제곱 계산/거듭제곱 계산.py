# 3910

import time
import sys
input = sys.stdin.readline

dp = list(0 for _ in range(1024))

for i in range(2, 1024):
    temp = str(bin(i)[2:])
    dp[i] = len(temp) + temp.count('1') - 2

exp = list(0 for _ in range(19))
exp[0] = 1


def dfs(d, Max_D, Max_N, exp):
    if d >= Max_D:
        return

    for i in range(d+1):
        exp[d+1] = exp[d] + exp[i]
        if exp[d+1] < Max_N and dp[exp[d+1]] >= d+1:
            dp[exp[d+1]] = d + 1
            dfs(d+1, Max_D, Max_N, exp)

        exp[d+1] = exp[d] - exp[i]
        if exp[d+1] > 0 and dp[exp[d+1]] >= d+1:
            dp[exp[d+1]] = d+1
            dfs(d+1, Max_D, Max_N, exp)


dfs(0, 18, 1024, exp)

for _ in range(int(input())):
    print(dp[int(input())])
