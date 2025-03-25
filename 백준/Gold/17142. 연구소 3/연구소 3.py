# 17142

import itertools
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tot_wall = 0
tot_empty = 0
unactive_virus = list()

arr = list()
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 2:
            unactive_virus.append([i, j])
        elif temp[j] == 1:
            tot_wall += 1
        elif temp[j] == 0:
            tot_empty += 1

    arr.append(temp)

answer = 10e9

if tot_empty == 0:
    print(0)
    quit()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(stack, visited,  temp_answer, tot_empty):
    while stack:
        temp_answer += 1
        is_move_to_empty = 0
        for _ in range(len(stack)):
            p, q = stack.popleft()
            for i in range(4):
                y = p + dy[i]
                x = q + dx[i]
                if 0 <= y < n and 0 <= x < n:
                    if visited[y][x]:
                        continue
                    elif arr[y][x] == 1:
                        visited[y][x] = 1
                    else:
                        visited[y][x] = 1
                        stack.append([y, x])
                        if arr[y][x] == 0:
                            tot_empty -= 1
                            is_move_to_empty += 1
                        elif arr[y][x] == 2:
                            is_move_to_empty += 1
        if not is_move_to_empty:
            temp_answer -= 1

        if tot_empty == 0:
            return temp_answer, tot_empty
    return temp_answer, tot_empty


temp = list(itertools.combinations(unactive_virus, m))
for i in temp:
    stack_ = deque([])
    stack_.extend(i)
    visited_ = list(list(0 for _ in range(n)) for _ in range(n))
    for u, v in stack_:
        visited_[u][v] = 1
    r, s = bfs(stack_, visited_, 0, tot_empty)
    if s == 0:
        answer = min(answer, r)

print(answer) if answer != 10e9 else print(-1)
