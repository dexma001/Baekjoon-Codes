# 15828

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
answer = deque([])

while True:
    temp = int(input())
    if temp == -1:
        break

    elif temp == 0:
        answer.popleft()

    else:
        answer.append(temp)

if not answer:
    print('empty')
else:
    print(*answer)
