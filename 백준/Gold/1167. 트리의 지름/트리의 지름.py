# 1167

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2**31-1)

n = int(input())
tree = list([] for _ in range(n+1))

for i in range(n):
    arr = deque(list(map(int, input().split())))
    temp = arr.popleft()
    arr.pop()

    while arr:
        a = arr.popleft()
        b = arr.popleft()
        tree[temp].append([a, b])

answer = [0, 0]

visited = list(False for _ in range(n+1))


def dfs(node, value):
    global answer
    visited[node] = True
    for i, j in tree[node]:
        if not visited[i]:
            dfs(i, value+j)
    else:
        if value > answer[1]:
            answer = [node, value]

    return


dfs(1, 0)

visited = list(False for _ in range(n+1))
temp = answer[0]
answer = [0, 0]
dfs(temp, 0)

print(answer[1])
