# 1021

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = deque(list(i for i in range(1, n+1)))

q_arr = list(map(int, input().split()))

answer = 0

for i in q_arr:
    temp = arr.index(i)

    if temp != 0:
        if temp <= (n-1)//2:
            while temp != 0:
                arr.rotate(-1)
                answer += 1
                temp -= 1
        else:
            while temp != 0:
                arr.rotate(1)
                answer += 1
                temp = (temp+1) % n

    arr.popleft()
    n -= 1

print(answer)
