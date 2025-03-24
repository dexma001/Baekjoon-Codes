# 7570

import sys
input = sys.stdin.readline

n = int(input())
ori_arr = list(map(int, input().split()))
my_arr = list()
my_arr.append([0, -1])
for i in range(n):
    my_arr.append([ori_arr[i], i])
my_arr.sort()


dp = list(0 for _ in range(n+1))
dp[ori_arr[-1]] = 1

for i in range(n-1, -1, -1):
    if ori_arr[i] == n:
        dp[ori_arr[i]] = 1
        continue
    if my_arr[ori_arr[i]+1][1] > i:
        dp[ori_arr[i]] = dp[ori_arr[i]+1] + 1
    else:
        dp[ori_arr[i]] = 1

print(n - max(dp))