# 18115

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
temp_skills = list(map(int, input().split()))
temp_skills.reverse()
skills = [0] + temp_skills

answer = deque([])
for i in range(1, n+1):
    if skills[i] == 1:
        answer.append(i)
    elif skills[i] == 2:
        answer.insert(-1, i)
    else:
        answer.appendleft(i)

answer.reverse()
print(*answer)
