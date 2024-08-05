# 2346

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = deque(list(map(int, input().split())))
num_list = deque(list(i for i in range(1, n+1)))

answer = list()

while arr:
    temp = arr.popleft()
    answer.append(num_list.popleft())

    if temp > 0:
        arr.rotate(-temp+1)
        num_list.rotate(-temp+1)
    else:
        arr.rotate(-temp)
        num_list.rotate(-temp)

print(*answer)
