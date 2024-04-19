# 2150

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())

direct_graph = list([] for _ in range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    direct_graph[a].append(b)

finished = [False] * (n+1)
visited = [0] * (n+1)
stack_arr = list()

answer = list()
id = 1


def tarjan(i):
    global id
    visited[i] = id
    id += 1
    stack_arr.append(i)
    parent = visited[i]

    for j in direct_graph[i]:
        if visited[j] == 0:
            parent = min(parent, tarjan(j))
        elif finished[j] == False:
            parent = min(parent, visited[j])

    if parent == visited[i]:
        scc = list()
        while True:
            k = stack_arr.pop()
            scc.append(k)
            finished[k] = True
            if k == i:
                break
        scc.sort()
        answer.append(scc)

    return parent


for i in range(1, n+1):
    if visited[i] == 0:
        tarjan(i)

print(len(answer))
answer.sort()
for i in answer:
    i.append(-1)
    print(*i)
