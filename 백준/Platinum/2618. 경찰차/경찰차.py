# 2618

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
case = int(input())
case_list = [[1, 1], [n, n]]
for i in range(case):
    case_list.append(list(map(int, input().split())))

dp = list([0 for _ in range(case+2)] for _ in range(case+2))
dp_trace = list([0 for _ in range(case+2)] for _ in range(case+2))


def distance(a, b):
    return abs(case_list[a][0] - case_list[b][0]) + abs(case_list[a][1] - case_list[b][1])


def solve(m, n):
    next = max(m, n) + 1

    if next == case +2:
        return 0

    if dp[m][n] != 0:
        return dp[m][n]

    pol1 = solve(next, n) + distance(m, next)
    pol2 = solve(m, next) + distance(next, n)
    if pol1 < pol2:
        dp_trace[m][n] = 1
        dp[m][n] = pol1
    else:
        dp_trace[m][n] = 2
        dp[m][n] = pol2

    return dp[m][n]


print(solve(0, 1))

m, n = 0, 1
for i in range(2, case+2):
    print(dp_trace[m][n])
    if dp_trace[m][n] == 1:
        m = i
    else:
        n = i
