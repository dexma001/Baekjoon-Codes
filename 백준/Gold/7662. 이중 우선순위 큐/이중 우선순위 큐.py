# 7662

import sys
import heapq
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())

    arr = list()
    minus_arr = list()
    visited = [False] * n

    for m in range(n):
        a, b = map(str, input().split())
        b = int(b)

        if a == 'I':
            heapq.heappush(arr, (b, m))
            heapq.heappush(minus_arr, (-b, b, m))
            visited[m] = True
        else:
            if arr != list():
                if b == -1:
                    while arr and not visited[arr[0][1]]:
                        heapq.heappop(arr)
                    if arr:
                        visited[arr[0][1]] = False
                        heapq.heappop(arr)

                else:
                    while minus_arr and not visited[minus_arr[0][2]]:
                        heapq.heappop(minus_arr)
                    if minus_arr:
                        visited[minus_arr[0][2]] = False
                        heapq.heappop(minus_arr)

    while minus_arr and not visited[minus_arr[0][2]]:
        heapq.heappop(minus_arr)
    while arr and not visited[arr[0][1]]:
        heapq.heappop(arr)

    if arr == list():
        print('EMPTY')
        continue

    else:
        print(minus_arr[0][1], arr[0][0])
