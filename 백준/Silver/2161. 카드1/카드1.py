# 2161

from collections import deque

n = int(input())
arr = deque(list(i for i in range(1, n+1)))

answer = list()

for _ in range(n-1):
    answer.append(arr.popleft())
    arr.rotate(-1)

answer.append(arr[0])

print(*answer)
