# 1389

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list() for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = [0, 10**9]

for i in range(1, n+1):
    visited = list(0 for _ in range(n+1))
    visited[i] = 1
    stack = deque()
    temp_answer = 0

    for j in arr[i]:
        if not visited[j]:
            visited[j] = 1
            stack.append(j)

    u = 1
    while stack:
        for _ in range(len(stack)):
            a = stack.popleft()
            temp_answer += u

            for b in arr[a]:
                if not visited[b]:
                    visited[b] = 1
                    stack.append(b)

        u += 1

    if temp_answer < answer[1]:
        answer = [i, temp_answer]

print(answer[0])
