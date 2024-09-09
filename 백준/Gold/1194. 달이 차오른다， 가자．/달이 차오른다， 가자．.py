# 1194

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()

door = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f'}
bits = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32}

stack = deque([])

for i in range(n):
    temp = list(map(str, input().rstrip()))
    if not stack and '0' in temp:
        stack.append([i, temp.index('0'), 0, 0])
    arr.append(temp)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

nevervisited = list(list(True for _ in range(m)) for _ in range(n))
lastvisited = list(list(list(0 for _ in range(m))
                   for _ in range(n)) for _ in range(64))

nevervisited[stack[0][0]][stack[0][1]] = False

while stack:
    p, q, keys, cnt = stack.popleft()
    for i in range(4):
        y = p + dy[i]
        x = q + dx[i]

        if 0 <= y < n and 0 <= x < m:
            if arr[y][x] == '#':
                continue

            if lastvisited[keys][y][x] != keys or nevervisited[y][x]:
                if arr[y][x] == '.' or arr[y][x] == '0':
                    stack.append([y, x, keys, cnt+1])
                    nevervisited[y][x] = False
                    lastvisited[keys][y][x] = keys

                elif arr[y][x] in door and bits[door[arr[y][x]]] & keys != 0:
                    if keys > lastvisited[keys][y][x]:
                        stack.append([y, x, keys, cnt+1])
                        nevervisited[y][x] = False
                        lastvisited[keys][y][x] = keys

                elif arr[y][x] in bits:
                    newkey = keys | bits[arr[y][x]]
                    stack.append([y, x, newkey, cnt+1])
                    nevervisited[y][x] = False
                    lastvisited[newkey][y][x] = newkey

                elif arr[y][x] == '1':
                    print(cnt+1)
                    quit()
else:
    print(-1)
