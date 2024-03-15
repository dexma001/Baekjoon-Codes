# 9019

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):

    start, end = map(int, input().split())
    arr = deque([])
    arr.append((start, 'F'))
    visited = dict()

    trig = 0
    while arr:
        x, y = arr.popleft()

        for i in range(4):
            if i == 0:
                n = (x * 2) % 10000
                if n not in visited.keys():
                    arr.append((n, y+'D'))
                    visited[n] = 1
            elif i == 1:
                if x == 0:
                    n = 9999
                else:
                    n = x - 1
                if n not in visited.keys():
                    arr.append((n, y+'S'))
                    visited[n] = 1
            elif i == 2:
                a = x//1000
                b = (x-(a*1000))//100
                c = (x-(a*1000)-(b*100))//10
                d = (x-(a*1000)-(b*100)-(c*10))
                n = b*1000 + c*100 + d*10 + a
                if n not in visited.keys():
                    arr.append((n, y+'L'))
                    visited[n] = 1
            else:
                a = x//1000
                b = (x-(a*1000))//100
                c = (x-(a*1000)-(b*100))//10
                d = (x-(a*1000)-(b*100)-(c*10))
                n = d*1000 + a*100 + b*10 + c
                if n not in visited.keys():
                    arr.append((n, y+'R'))
                    visited[n] = 1

            if n == end:
                print((arr[-1][1])[1:])
                trig = 1
                break

        if trig == 1:
            break
