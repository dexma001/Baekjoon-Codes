# 1986

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list(0 for _ in range(m+1)) for _ in range(n+1))

queen = deque(list(map(int, input().split()))[1:])
knight = deque(list(map(int, input().split()))[1:])
pawn = deque(list(map(int, input().split()))[1:])

answer = 0

while queen:
    i = queen.popleft()
    j = queen.popleft()
    arr[i][j] = 'Q'
    answer += 1

while knight:
    p = knight.popleft()
    q = knight.popleft()
    arr[p][q] = 'K'
    answer += 1
while pawn:
    x = pawn.popleft()
    y = pawn.popleft()
    arr[x][y] = 'P'
    answer += 1

knight_y = [2, 1, -1, -2, -2, -1, 1, 2]
knight_x = [1, 2, 2, 1, -1, -2, -2, -1]

queen_y = [1, 1, 0, -1, -1, -1, 0, 1]
queen_x = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j] == 'K':
            for k in range(8):
                y = i + knight_y[k]
                x = j + knight_x[k]
                if 1 <= y <= n and 1 <= x <= m and not arr[y][x]:
                    arr[y][x] = 1
                    answer += 1
        elif arr[i][j] == 'Q':
            for k in range(8):
                mul = 1
                while True:
                    y = i + queen_y[k]*mul
                    x = j + queen_x[k] * mul
                    mul += 1
                    if 1 <= y <= n and 1 <= x <= m:
                        if arr[y][x] == 'Q' or arr[y][x] == 'K' or arr[y][x] == 'P':
                            break
                        elif arr[y][x]:
                            continue
                        else:
                            arr[y][x] = 1
                            answer += 1
                    else:
                        break
        else:
            continue

print(n*m-answer)
