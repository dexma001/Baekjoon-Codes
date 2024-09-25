# 24542

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list([] for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = 1
visited = list(False for _ in range(n+1))
for i in range(1, n+1):
    if visited[i]:
        continue
    else:
        stack = deque([])
        stack.append(i)
        visited[i] = True
        len = 1
        while stack:
            k = stack.popleft()
            for j in arr[k]:
                if not visited[j]:
                    visited[j] = True
                    stack.append(j)
                    len += 1
    answer *= len
    answer %= 1000000007

print(answer)
