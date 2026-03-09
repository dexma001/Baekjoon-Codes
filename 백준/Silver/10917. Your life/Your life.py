import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list() for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

temp = deque([])
temp.append(1)
visited = list(0 for _ in range(n+1))
visited[1] = 1
answer = 0
solved = 0

while temp:
    for _ in range(len(temp)):
        t = temp.popleft()
        if t == n:
            solved = 1
            break
        for i in arr[t]:
            if not visited[i]:
                visited[i] = 1
                temp.append(i)

    if not solved:
        answer += 1

if solved and answer <= m:
    print(answer)
else:
    print(-1)