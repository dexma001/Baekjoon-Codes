# 1516

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = [0] * (n+1)
to_build = [[] for _ in range(n+1)]
to_build_cnt = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    arr[i] = temp[0]
    for j in range(1, len(temp)-1):
        to_build[temp[j]].append(i)
        to_build_cnt[i] += 1

stack = deque()
for i in range(1, n+1):
    if to_build_cnt[i] == 0:
        stack.append(i)

while stack:
    tem = stack.popleft()
    dp[tem] += arr[tem]
    for i in to_build[tem]:
        to_build_cnt[i] -= 1
        dp[i] = max(dp[i], dp[tem])
        if to_build_cnt[i] == 0:
            stack.append(i)

for i in range(1, n+1):
    print(dp[i])
