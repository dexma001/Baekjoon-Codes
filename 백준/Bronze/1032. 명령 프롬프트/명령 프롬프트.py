# 1032

import sys
input = sys.stdin.readline

n = int(input())
answer = list(map(str, input().rstrip()))

for _ in range(n-1):
    temp = list(map(str, input().rstrip()))
    for i in range(len(temp)):
        if answer[i] != temp[i]:
            answer[i] = '?'

print(''.join(answer))
