# 2559

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
temp = deque([])
temp_sum = 0
for i in range(k):
    temp.append(arr[i])
    temp_sum += arr[i]
answer = temp_sum

for i in range(k, n):
    q = temp.popleft()
    temp.append(arr[i])
    temp_sum += (arr[i] - q)
    answer = max(answer, temp_sum)

print(answer)