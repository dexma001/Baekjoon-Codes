# 1135

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tree = list([] for _ in range(n))
for i in range(1, n):
    tree[arr[i]].append(i)

dp = list(0 for _ in range(n))


def treedp(i):
    if tree[i]:
        under_tree = sorted(list(treedp(j) for j in tree[i]), reverse=True)
        dp[i] = max(list(j+1+under_tree[j] for j in range(len(tree[i]))))
    return dp[i]


treedp(0)
print(dp[0])
