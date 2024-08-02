# 4803

import sys
input = sys.stdin.readline


def dfs(i):
    global det, nodes
    visited[i] = 1
    for j in arr[i]:
        if not visited[j]:
            nodes += 1
            dfs(j)
        else:
            det += 1


cases = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    arr = list([] for _ in range(n+1))

    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    visited = list(0 for _ in range(n+1))

    answer = 0
    for i in range(1, n+1):
        if not visited[i]:
            det = 0
            nodes = 1
            dfs(i)
            if det <= nodes:
                answer += 1

    if answer == 0:
        print(f'Case {cases}: No trees.')
    elif answer == 1:
        print(f'Case {cases}: There is one tree.')
    else:
        print(f'Case {cases}: A forest of {answer} trees.')

    cases += 1
