#18405
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()

queue = list()
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            queue.append([temp[j], i, j])
    arr.append(temp)

s, Y, X = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

queue.sort()
for _ in range(s):
    for _ in range(len(queue)):
        value, a, b = queue.pop(0)
        for i in range(4):
            y = a + dy[i]
            x = b + dx[i]
            if 0<=y<n and 0<=x<n:
                if arr[y][x] != 0:
                    continue
                else:
                    arr[y][x] = value
                    queue.append([value, y, x])
    if queue:
        queue.sort()

print(arr[Y-1][X-1])