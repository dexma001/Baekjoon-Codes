# 25577
# 순열 사이클 + 좌표압축

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
input_arr = list(map(int, input().split()))

arr = list()
numbers = set()

for i in range(n):
    arr.append([i, input_arr[i]])
    numbers.add(input_arr[i])

numbers = deque(sorted(numbers))

arr.sort(key=lambda x: x[1])

index = 0
for i in range(n):
    while arr[i][1] != numbers[0]:
        numbers.popleft()
        index += 1
    arr[i][1] = index

arr.sort()

answer = 0

locate = list(0 for _ in range(n))
visited = list(0 for _ in range(n))

for i in range(n):
    locate[arr[i][1]] = i

for i in range(n):
    if visited[i]:
        continue

    temp_answer = 0
    last = i

    while visited[last] == 0:
        visited[last] = 1
        last = locate[last]
        temp_answer += 1

    answer += (temp_answer-1)

print(answer)
