# 1306 - Internet

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = list()
temp = deque([])

for i in range(2*m-1):
    while temp and temp[-1][1] < arr[i]:
        temp.pop()
    temp.append([i, arr[i]])
answer.append(temp[0][1])

for i in range(2*m-1, n):
    while temp and temp[-1][1] < arr[i]:
        temp.pop()
    while temp and temp[0][0] <= i - (2*m)+1:
        temp.popleft()
    temp.append([i, arr[i]])
    answer.append(temp[0][1])

print(*answer)
