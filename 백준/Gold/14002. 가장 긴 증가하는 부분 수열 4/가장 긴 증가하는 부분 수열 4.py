import sys
from collections import deque

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

inc = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            inc[i] = max(inc[i], inc[j]+1)

print(max(inc))

arr = []
k = max(inc)

for i in range(n-1, -1, -1):
    if inc[i] == k:
        arr.append(li[i])
        k -= 1

arr.reverse()
print(*arr)
