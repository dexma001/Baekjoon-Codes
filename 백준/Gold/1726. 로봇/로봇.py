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

location_change = [1, 2, 3]
x_w = [0, 0, 0, 1, 2, 3, -1, -2, -3, 0, 0, 0, 0, 0, 0]
y_w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, -1, -2, -3]

while queue:
    for _ in range(len(queue)):
        y, x, l = queue.popleft()
        if y == end_y and x == end_x and l == end_loc:
            print(answer)
            quit()

        for i in range((l % 2), (l % 2) + 2):
            changed_location = (l+location_change[i]) % 4
            if not changed_location:
                changed_location = 4

            if visited[y][x][changed_location] != 1:
                visited[y][x][changed_location] = 1
                queue.append([y, x, changed_location])

        for j in range(l*3, l*3+3):
            dy = y + y_w[j]
            dx = x + x_w[j]
            if 0 <= dy < n and 0 <= dx < m and arr[dy][dx] != 1:
                if visited[dy][dx][l] != 1:
                    visited[dy][dx][l] = 1
                    queue.append([dy, dx, l])
            else:
                break

    answer += 1
