# 2666

import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
s = int(input())
todo = list(int(input()) for _ in range(s))

dp = list(list(list(-1 for _ in range(n+1))
          for _ in range(n+1)) for _ in range(s))


def solve(idx, a, b):
    if idx == s:
        return 0
    if dp[idx][a][b] != -1:
        return dp[idx][a][b]

    c1 = solve(idx+1, todo[idx], b) + abs(todo[idx] - a)
    c2 = solve(idx+1, a, todo[idx]) + abs(todo[idx] - b)

    dp[idx][a][b] = min(c1, c2)

    return dp[idx][a][b]


print(solve(0, a, b))
