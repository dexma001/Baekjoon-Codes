# 2470

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)

answer = 3000000000
answer_arr = [0, 0]
while n >= 2:
    temp = (arr[0] + arr[-1])
    if abs(temp) < answer:
        answer = abs(temp)
        answer_arr = [arr[0], arr[-1]]

    if temp >= 0:
        arr.pop()
    else:
        arr.popleft()
    n -= 1

print(*answer_arr)
