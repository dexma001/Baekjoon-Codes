#17836

import sys
from collections import deque
input = sys.stdin.readline

n, m , t = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
        
stack = deque([])
stack.append([0, 0, 0])
answer = 10001

visited = list(list(0 for _ in range(m)) for _ in range(n))
visited[0][0]= 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while stack:
    i, j, k = stack.popleft()
    
    for l in range(4):
        y = i + dy[l]
        x = j + dx[l]
        
        if 0<=y<n and 0<=x<m:
            if visited[y][x] or arr[y][x] == 1:
                continue
    
            if y == n-1 and x == m-1:
                answer = min(answer, k+1)
            elif arr[y][x] == 2:
                answer = min(answer, k + abs(n-y) + abs(m-x) -1) 
            else:
                stack.append([y, x, k+1])
                visited[y][x] = 1

print(answer) if answer <= t else print('Fail')