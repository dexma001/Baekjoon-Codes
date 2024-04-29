# 2533

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visit = [0] * (n+1)
dp = [[0, 0] for _ in range(n+1)]


def find(i):
    dp[i][0] = 1
    visit[i] = 1
    for j in tree[i]:
        if visit[j] == 1:
            continue
        find(j)
        dp[i][1] += dp[j][0]
        dp[i][0] += min(dp[j][1], dp[j][0])


find(1)
print(min(dp[1]))
