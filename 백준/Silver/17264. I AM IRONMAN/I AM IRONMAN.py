# 17264

import sys
input = sys.stdin.readline

n, p = map(int, input().split())
w, l, g = map(int, input().split())

win_lose = dict()
win_lose['W'] = list()
win_lose['L'] = list()

for _ in range(p):
    x, y = map(str, input().split())
    if y == 'W':
        win_lose['W'].append(x)
    else:
        win_lose['L'].append(x)

trig = 0
point = 0
for _ in range(n):
    temp = str(input().rstrip())
    if trig == 1:
        continue

    if temp in win_lose['W']:
        point += w
    else:
        point -= l
        if point < 0:
            point = 0

    if point >= g:
        trig = 1


if trig == 1:
    print('I AM NOT IRONMAN!!')
else:
    print('I AM IRONMAN!!')
