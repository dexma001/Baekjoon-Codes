import sys
import copy
from collections import deque

n = int(input())
graph = list(list(map(str, sys.stdin.readline().strip())) for _ in range(n))
graph_rg = copy.deepcopy(graph)
g_c = graph_rg.count('G')
r_c = graph_rg.count('R')
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque([])

for i in range(n):
    for j in range(n):
        if g_c < r_c:
            if graph_rg[i][j] == 'G':
                graph_rg[i][j] = 'R'
        else:
            if graph_rg[i][j] == 'R':
                graph_rg[i][j] = 'G'


def count_area(m, arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0:
                queue.append([i, j])  # 1
                store = arr[i][j]
                arr[i][j] == 0
                while queue:
                    a, b = queue.popleft()
                    for k in range(4):
                        x = a+dx[k]
                        y = b+dy[k]

                        if -1 < x < len(arr) and -1 < y < len(arr) and arr[x][y] == store:
                            queue.append([x, y])
                            arr[x][y] = 0
                m += 1
            else:
                continue
    return m


print(count_area(0, graph), count_area(0, graph_rg))
