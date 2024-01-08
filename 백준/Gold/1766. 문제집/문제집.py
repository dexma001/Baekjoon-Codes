# 1766

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
input_arr = list([] for _ in range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    input_arr[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = list()
    q = list()

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        node = heapq.heappop(q)
        result.append(node)
        for j in input_arr[node]:
            indegree[j] -= 1
            if indegree[j] == 0:
                heapq.heappush(q, j)

    print(*result)


topology_sort()
