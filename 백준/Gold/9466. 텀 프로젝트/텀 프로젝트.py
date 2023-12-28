# ChatGPT가 쓴 9466번

import sys
sys.setrecursionlimit(10**8)


def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    number = numbers[v]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False] * n
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))
