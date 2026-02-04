import sys
input = sys.stdin.readline
from collections import deque

arr = deque(list(map(str, input().strip())))

answer = 0

for _ in range(len(arr)):
    answer += int(''.join(arr))
    arr.rotate(1)
    
print(answer)

