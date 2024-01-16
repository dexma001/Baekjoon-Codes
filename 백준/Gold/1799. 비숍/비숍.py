# 1799

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
