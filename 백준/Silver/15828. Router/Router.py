# 15828

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
answer = deque([])
len_answer = 0

while True:
    temp = int(input())
    if temp == -1:
        break

    elif temp == 0:
        answer.popleft()
        len_answer -= 1
    else:
        if len_answer < n:
            answer.append(temp)
            len_answer += 1
if not answer:
    print('empty')
else:
    print(*answer)
