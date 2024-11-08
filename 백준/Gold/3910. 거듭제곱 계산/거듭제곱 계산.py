# 3910
import sys
input = sys.stdin.readline
dp = list(0 for _ in range(1024))
for i in range(2, 1024):
    temp = list(j for j in list(map(str, bin(i)[2:])))
    dp[i] = len(temp) + temp.count('1') - 2
exp = list(i for i in range(21))
exp[0] = 1
def dfs(d, MAX_D, MAX_N, exp):
    if d > MAX_D:
        return

    for i in range(d+1):
        exp[d+1] = exp[i] + exp[d]
        if exp[d+1] < MAX_N and dp[exp[d+1]] >= d+1:
            dp[exp[d+1]] = d+1
            dfs(d+1, MAX_D, MAX_N, exp)

        exp[d+1] = exp[d] - exp[i]
        if exp[d+1] > 0 and dp[exp[d+1]] >= d+1:
            dp[exp[d+1]] = d+1
            dfs(d+1, MAX_D, MAX_N, exp)
dfs(0, 20, 1024, exp)
for _ in range(int(input())):
    print(dp[int(input())])
