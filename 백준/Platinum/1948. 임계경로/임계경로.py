# 1948

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

city = int(input())
road = int(input())
road_arr = list([] for _ in range(city+1))
reverse_road_arr = list([] for _ in range(city+1))
edge_cnt = list(0 for _ in range(city+1))

for _ in range(road):
    a, b, c = map(int, input().split())
    road_arr[a].append((b, c))
    reverse_road_arr[b].append((a, c))
    edge_cnt[b] += 1

start, end = map(int, input().split())
start_to_end_arr = [0] * (city+1)

stack = deque([])
stack.append(1)

while stack:
    x = stack.popleft()
    for a, b in road_arr[x]:
        start_to_end_arr[a] = max(start_to_end_arr[a], start_to_end_arr[x] + b)
        edge_cnt[a] -= 1
        if edge_cnt[a] == 0:
            stack.append(a)

max_edge = start_to_end_arr[end]
print(max_edge)

answer = 0
visited = [False] * (city+1)


def back_tracking(a):
    global answer
    visited[a] = True
    for i, j in reverse_road_arr[a]:
        if start_to_end_arr[a] == start_to_end_arr[i] + j:
            answer += 1
            if visited[i] != True:
                back_tracking(i)


back_tracking(end)
print(answer)
