from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split())
    arr = list()
    for _ in range(h):
        arr.append(list(map(str, input().strip())))
    visited = list(list(0 for _ in range(w)) for _ in range(h))
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    answer = 0
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1 or arr[i][j] == '.':
                continue
            bfs = deque([])
            bfs.append([i, j])
            while bfs:
                p, q = bfs.popleft()
                for k in range(4):
                        y = p + dy[k]
                        x = q + dx[k]
                        if 0<=y<h and 0<=x<w:
                            if arr[y][x] == '.':
                                continue
                            else:
                                if visited[y][x]:
                                    continue
                                else:
                                    visited[y][x] = 1
                                    bfs.append([y, x])
            answer += 1
            
    print(answer)