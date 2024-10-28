# 27466

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(str, input().strip()))

answer = list()

mom = ['a', 'e', 'i', 'o', 'u']

while s:
    i = s.pop()
    if i in mom:
        continue
    else:
        answer.append(i)
        break

while s:
    j = s.pop()
    if j == 'A':
        answer.append(j)

    if len(answer) == 3:
        break

if len(s) < m-3:
    print('NO')
else:
    for _ in range(m-3):
        answer.append(s.pop())
    print('YES')
    print(''.join(answer[::-1]))
