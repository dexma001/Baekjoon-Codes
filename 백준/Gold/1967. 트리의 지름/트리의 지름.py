# 1967

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

node = int(input())

node_arr = list([] for _ in range(node+1))
for _ in range(node-1):
    a, b, c = map(int, input().split())
    node_arr[a].append((b, c))
    node_arr[b].append((a, c))

node_level = list(0 for _ in range(node+1))
node_level[1] = 1
node_length = list(0 for _ in range(node+1))
node_parent = list(0 for _ in range(node+1))


def dfs(x, y, z, level):
    visited[x] = True
    node_level[y] = level
    node_parent[y] = x
    node_length[y] = node_length[x] + z
    for i, j in node_arr[y]:
        if visited[i] != True:
            dfs(y, i, j, level+1)


visited = [False] * (node+1)
for i, j in node_arr[1]:
    dfs(1, i, j, 2)

max_length = max(node_length)
max_index = node_length.index(max_length)


node_length_1 = list(0 for _ in range(node+1))


def dfs1(i, j, k):
    visited_1[i] = True
    node_length_1[j] = node_length_1[i] + k
    for p, q in node_arr[j]:
        if visited_1[p] != True:
            dfs1(j, p, q)


visited_1 = [False] * (node+1)
for x, y in node_arr[max_index]:
    dfs1(max_index, x, y)

print(max(node_length_1))
