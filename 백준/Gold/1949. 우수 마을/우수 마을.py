# 1949

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
people = [0] + list(map(int, input().split()))

tree = list(list() for _ in range(n+1))
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in tree:
    i.sort()

# 0번째 라인은 우수마을일 때 / 1번째 마을은 우수마을 아닐때
dp = list(list(0 for _ in range(n+1))for _ in range(2))
visited = list(0 for _ in range(n+1))


def dfs(i):
    visited[i] = 1
    for j in tree[i]:
        if visited[j]:
            continue
        else:
            dfs(j)
            dp[0][i] = dp[0][i]+dp[1][j]
            dp[1][i] += max(dp[0][j], dp[1][j])

    dp[0][i] += people[i]


dfs(1)
print(max(max(dp[0]), max(dp[1])))
