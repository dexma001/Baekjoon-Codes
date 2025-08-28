# 3190

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
table = list(list(0 for _ in range(n+1)) for _ in range(n+1))

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    table[a][b] = 1


l = int(input())
rotate_list = deque([])
for _ in range(l):
    rotate_list.append(list(map(str, input().split())))

answer = 0
locate = deque([])
locate.append([1, 1])

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
idx = 0

answer = 0
while True:
    if rotate_list:
        temp = [locate[-1][0] + dy[idx],
                locate[-1][1] + dx[idx]]
        answer += 1
        if temp in locate or n+1 in temp or 0 in temp:
            break
        elif table[temp[0]][temp[1]] == 1:
            locate.append(temp)
            table[temp[0]][temp[1]] = 0
        else:
            locate.append(temp)
            locate.popleft()

        if answer == int(rotate_list[0][0]):
            if rotate_list[0][1] == 'L':
                idx += 3
                idx %= 4
                rotate_list.popleft()
            else:
                idx += 1
                idx %= 4
                rotate_list.popleft()
    else:
        temp = [locate[-1][0] + dy[idx],
                locate[-1][1] + dx[idx]]
        answer += 1
        if temp in locate or n+1 in temp or 0 in temp:
            break
        elif table[temp[0]][temp[1]] == 1:
            locate.append(temp)
            table[temp[0]][temp[1]] = 0
        else:
            locate.append(temp)
            locate.popleft()

print(answer)
