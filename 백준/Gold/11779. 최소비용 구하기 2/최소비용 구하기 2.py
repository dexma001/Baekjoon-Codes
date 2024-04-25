# 11779

import sys
import heapq
import copy
input = sys.stdin.readline
INF = 10**8

n = int(input())
dist = [INF] * (n+1)
dist_way = [[]for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
dist[start] = 0

while q:
    distance, node = heapq.heappop(q)
    if distance > dist[node]:
        continue

    for n in graph[node]:
        new_dist = n[0] + dist[node]
        new_dist_way = list(i for i in dist_way[node])
        new_dist_way.append(node)
        if new_dist < dist[n[1]]:
            dist[n[1]] = new_dist
            dist_way[n[1]] = new_dist_way
            heapq.heappush(q, (new_dist, n[1]))

print(dist[end])
dist_way[end].append(end)
print(len(dist_way[end]))
print(*dist_way[end])
