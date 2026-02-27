import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = deque([])

for _ in range(n):
    arr.append(list(map(str, input().split())))
    
while len(arr) > 1:
    a, b = arr.popleft()
    for _ in range(int(b)-1):
        arr.rotate(-1)
    arr.popleft()
    
    
print(arr[0][0])