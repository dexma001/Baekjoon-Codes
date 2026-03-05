#22116

import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = list(list(10e9+7 for _ in range(n)) for _ in range(n))

q = list()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

heapq.heappush(q, (0, 0, 0))
visited[0][0] = 0
while q:
    height, i, j = heapq.heappop(q)
    if visited[i][j] < height:
        continue

    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if 0<=y<n and 0<=x<n:
            temp_height = max(height, abs(arr[i][j] - arr[y][x]))
            if visited[y][x] > temp_height:
                visited[y][x] = temp_height
                heapq.heappush(q, (temp_height, y, x))

print(visited[-1][-1])