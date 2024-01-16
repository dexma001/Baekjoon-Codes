# 1799

'''
import sys
sys.setrecursionlimit(10**8)

n = int(input())
chess_plate = list()
for _ in range(n):
    chess_plate.append(list(map(int, input().split())))
answer = 0


def cross_delete_upper(a, b):
    x2 = a - 1
    y2 = b - 1
    if x2 < 0 or y2 < 0:
        return -1
    else:
        chess_plate[x2][y2] = 0
        cross_delete_upper(x2, y2)


def cross_delete_downer(c, d):
    x3 = c + 1
    y3 = d + 1
    if x3 >= n or y3 >= n:
        return -1
    else:
        chess_plate[x3][y3] = 0
        cross_delete_downer(x3, y3)


for i in range(2*n-1):
    if i < n:
        for j in range(0, i+1):
            if chess_plate[j][i-j] == 0:
                continue
            else:
                cross_delete_upper(j, i-j)
                cross_delete_downer(j, i-j)
                answer += 1
                break

    else:
        i1 = 2*(n-1)-i
        for l in range(n-1, (n-2)-i1, -1):
            if chess_plate[i-l][l] == 0:
                continue
            else:
                cross_delete_upper(i-l, l)
                cross_delete_downer(i-l, l)
                answer += 1
                break

print(answer)
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
chess_plate = list()
for _ in range(n):
    chess_plate.append(list(map(int, input().split())))

rd = {}
for i in range(-n+1, n):
    rd[i] = 0


def upper_bound(diag):
    able_row = 0
    for i in range(diag, 2*n-1):
        for y in range(i + 1):
            x = i - y
            if 0 <= x < n and 0 <= y < n and chess_plate[y][x] and rd[x-y] == 0:
                able_row += 1
                break
    return able_row


def bishop(row, cnt):
    global answer
    if row == 2*n:
        answer = max(answer, cnt)
        return

    ub = upper_bound(row)
    if ub+cnt <= answer:
        return

    for y in range(row+1):
        x = row - y
        if 0 <= x < n and 0 <= y < n and chess_plate[y][x] and rd[x-y] == 0:
            rd[x-y] = 1
            bishop(row+1, cnt+1)
            rd[x-y] = 0

    bishop(row+1, cnt)


answer = 0
bishop(0, 0)
print(answer)