# 1916

import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = list(10e9 for _ in range(n+1))
graph = list([] for _ in range(n+1))

for _ in range(m):
    a, b, i = map(int, input().split())
    graph[a].append([b, i])


def dijkstra(start):
    q = list()
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, node = heapq.heappop(q)
        if distance > dist[node]:
            continue

        for n in graph[node]:
            new_value = n[1]+dist[node]
            if new_value < dist[n[0]]:
                dist[n[0]] = new_value
                heapq.heappush(q, (new_value, n[0]))


u, v = map(int, input().split())
dijkstra(u)
print(dist[v])
