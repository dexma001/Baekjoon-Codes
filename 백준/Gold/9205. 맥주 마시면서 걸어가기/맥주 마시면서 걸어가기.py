# 9205

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    home = list()
    store = list()
    festival = list()

    for i in range(n+2):
        if i == 0:
            home.append(list(map(int, input().split())))
        elif i == n+1:
            festival.append(list(map(int, input().split())))
        else:
            store.append(list(map(int, input().split())))

    store.sort(key=lambda x: [x[0], x[1]])
    for i in range(n):
        store[i].insert(0, i)

    answer = 0

    arr = deque([])
    arr.append(home[0])
    visited = list(0 for _ in range(n))

    while arr:
        i, j = arr.popleft()
        if (abs(i-festival[0][0]) + abs(j-festival[0][1])) <= 1000:
            answer = 1
            break

        for k in store:
            if visited[k[0]]:
                continue

            elif (abs(i-k[1]) + abs(j-k[2])) <= 1000:
                arr.append([k[1], k[2]])
                visited[k[0]] = 1

    if answer:
        print('happy')
    else:
        print('sad')
