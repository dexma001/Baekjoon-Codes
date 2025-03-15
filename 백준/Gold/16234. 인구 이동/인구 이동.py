#16234

import time
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())

arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
answer = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while True:
    to_break = 0
    visited = list(list(0 for _ in range(n)) for _ in range(n))    
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            
            temp = deque([])
            temp.append([i, j]) #bfs
            visited[i][j]= 1
            temp_sum = 0 # 배분
            to_move = list() #배분할 list
            to_move.append([i, j])
            
            while temp:
                p, q = temp.popleft()
                temp_sum += arr[p][q]
                for k in range(4):
                    y = p + dy[k]
                    x = q + dx[k]
                    if 0<=y<n and 0<=x<n:
                        if l<= abs(arr[p][q] - arr[y][x])<=r and not visited[y][x]:
                            temp.append([y,x])
                            to_move.append([y,x])
                            visited[y][x] = 1
            
            if len(to_move) > 1:
                for v, w in to_move:
                    arr[v][w] = temp_sum//len(to_move)
                to_break = 1

    if to_break == 1:
        answer += 1
    
    else:
        break
    
print(answer)