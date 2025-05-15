# 1726

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = list(list([0, 0, 0, 0, 0] for _ in range(m))
               for _ in range(n))  # 동, 서, 남, 북

start_y, start_x, start_loc = map(int, input().split())
start_y -= 1
start_x -= 1
end_y, end_x, end_loc = map(int, input().split())
end_y -= 1
end_x -= 1

visited[start_y][start_x][start_loc] = 1
answer = 0
queue = deque([])
queue.append([start_y, start_x, start_loc])

while queue:
    for _ in range(len(queue)):
        y, x, l = queue.popleft()
        if y == end_y and x == end_x and l == end_loc:
            print(answer)
            quit()
        if l == 1 or l == 2:
            if visited[y][x][3] != 1:
                visited[y][x][3] = 1
                queue.append([y, x, 3])
            if visited[y][x][4] != 1:
                visited[y][x][4] = 1
                queue.append([y, x, 4])
            if l == 1:
                for i in range(1, 4):
                    dy = y
                    dx = x + i
                    if 0 <= dy < n and 0 <= dx < m and arr[dy][dx] != 1:
                        if visited[dy][dx][l] != 1:
                            visited[dy][dx][l] = 1
                            queue.append([dy, dx, l])
                    else:
                        break
            else:
                for i in range(-1, -4, -1):
                    dy = y
                    dx = x + i
                    if 0 <= dy < n and 0 <= dx < m and arr[dy][dx] != 1:
                        if visited[dy][dx][l] != 1:
                            visited[dy][dx][l] = 1
                            queue.append([dy, dx, l])
                    else:
                        break
        else:
            if visited[y][x][1] != 1:
                visited[y][x][1] = 1
                queue.append([y, x, 1])
            if visited[y][x][2] != 1:
                visited[y][x][2] = 1
                queue.append([y, x, 2])
            if l == 3:
                for i in range(1, 4):
                    dy = y + i
                    dx = x
                    if 0 <= dy < n and 0 <= dx < m and arr[dy][dx] != 1:
                        if visited[dy][dx][l] != 1:
                            visited[dy][dx][l] = 1
                            queue.append([dy, dx, l])
                    else:
                        break
            else:
                for i in range(-1, -4, -1):
                    dy = y + i
                    dx = x
                    if 0 <= dy < n and 0 <= dx < m and arr[dy][dx] != 1:
                        if visited[dy][dx][l] != 1:
                            visited[dy][dx][l] = 1
                            queue.append([dy, dx, l])
                    else:
                        break
    answer += 1
