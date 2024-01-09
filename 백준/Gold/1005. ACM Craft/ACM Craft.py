# 1005

import sys
from collections import deque
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    time_list = [0] + list(map(int, input().split()))
    a_b = list([] for _ in range(n+1))
    b_a = list([] for _ in range(n+1))
    indegree = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        a_b[a].append(b)
        b_a[b].append(a)
        indegree[b] += 1

    ans_building = int(input())

    def topology_sort():
        result = list(0 for i in range(n+1))
        q = deque([])

        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            k = q.popleft()
            if b_a[k] == []:
                result[k] = time_list[k]
            else:
                result[k] = time_list[k] + \
                    max(result[l] for l in b_a[k])
            for j in a_b[k]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        print(result[ans_building])

    topology_sort()
