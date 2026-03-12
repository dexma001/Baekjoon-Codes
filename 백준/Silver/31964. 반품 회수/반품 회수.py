#31964

import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
t = list(map(int, input().split()))

visited = list(0 for _ in range(n))
answer = 0
curr_loc = 0

for i in range(n):
    if x[i] >= t[i]:
        visited[i] = 1
        curr_loc = x[i]

answer += curr_loc

for i in range(n-1, -1, -1):
    if visited[i]:
        continue

    answer += max(abs(curr_loc - x[i]), abs(t[i] - answer))
    curr_loc = x[i]
    visited[i] = 1

answer += curr_loc
print(answer)