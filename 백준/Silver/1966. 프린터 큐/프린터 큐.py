# 1966

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, temp = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    for i in range(n):
        arr[i] = [i, arr[i]]

    answer = 1

    while True:
        trig = 0
        if n == 1:
            print(answer)
            break

        for i in range(1, n):
            if arr[i][1] > arr[0][1]:
                arr.rotate(-1)
                trig = 1
                break

        if trig == 0:
            if arr[0][0] == temp:
                print(answer)
                break
            else:
                arr.popleft()
                answer += 1
                n -= 1
