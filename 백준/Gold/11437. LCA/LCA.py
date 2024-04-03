# 11437(11439 배낌)

import sys
import math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
tree_level = [0] * (n+1)
tree_level_check = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def cnt_tree_level(x, level):
    tree_level_check[x] = True
    tree_level[x] = level
    for i in graph[x]:
        if tree_level_check[i] == True:
            continue
        parent[i] = x
        cnt_tree_level(i, level + 1)


cnt_tree_level(1, 1)

Sparse_table = list()
Sparse_table.append(parent)
level = math.ceil(math.log(max(tree_level), 2))
for i in range(level-1):
    Sparse_table.append([0] * (n+1))
    for j in range(n):
        Sparse_table[i+1][j+1] = Sparse_table[i][Sparse_table[i][j+1]]

m = int(input())
for _ in range(m):
    c, d = map(int, input().split())
    if tree_level[c] < tree_level[d]:
        c, d = d, c
    while tree_level[c] != tree_level[d]:
        for i in range(level-1, -1, -1):
            if tree_level[Sparse_table[i][c]] < tree_level[d]:
                continue
            else:
                c = Sparse_table[i][c]

    if c == d:
        print(d)
    else:
        for i in range(level-1, -1, -1):
            if Sparse_table[i][c] != 0 and Sparse_table[i][c] != Sparse_table[i][d]:
                c = Sparse_table[i][c]
                d = Sparse_table[i][d]
        print(Sparse_table[0][c])