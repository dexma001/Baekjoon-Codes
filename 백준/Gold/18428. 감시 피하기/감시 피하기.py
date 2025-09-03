# 18428

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = list()

teacher = list()
student = list()
empty = list()

for i in range(n):
    temp = list(map(str, input().split()))

    for j in range(n):
        if temp[j] == 'X':
            empty.append([i, j])
        elif temp[j] == 'S':
            student.append([i, j])
        else:
            teacher.append([i, j])

    arr.append(temp)

possible = list(list(i) for i in combinations(empty, 3))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
answer = 'NO'

for i in range(len(possible)):
    if answer == 'YES':
        break

    obstacle = possible[i]

    capture = 0
    for j in range(len(teacher)):
        y, x = teacher[j][0], teacher[j][1]
        for k in range(4):
            p, q = y+1-1, x + 1 - 1
            while True:
                p += dy[k]
                q += dx[k]

                if 0 <= p < n and 0 <= q < n:
                    if [p, q] in obstacle:
                        break

                    if arr[p][q] == 'S':
                        capture += 1
                else:
                    break

    if not capture:
        answer = 'YES'

print(answer)
