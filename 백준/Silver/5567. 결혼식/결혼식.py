import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

arr = list(list() for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
answer = 0
visited = list(0 for _ in range(n+1))
visited[1] = 1

for i in arr[1]:
    if not visited[i]:
        visited[i] = 1
        answer += 1
    for j in arr[i]:
        if not visited[j]:
                visited[j] = 1
                answer += 1
                
print(answer)