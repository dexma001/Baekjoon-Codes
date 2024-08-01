# 1406

import sys
input = sys.stdin.readline

answer = list(map(str, input().rstrip()))
temp = list()

for _ in range(int(input())):
    command = list(map(str, input().split()))

    if command[0] == 'L':
        if answer:
            temp.append(answer.pop())
    elif command[0] == 'D':
        if temp:
            answer.append(temp.pop())
    elif command[0] == 'B':
        if answer:
            answer.pop()
    else:
        answer.append(command[1])

temp.reverse()
answer.extend(temp)
print(''.join(answer))
