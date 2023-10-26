import sys

n = int(input())
list = list(map(int, sys.stdin.readline().split()))
cnt = int(input())
i = 0

while cnt > 0 and i < n:
    m = list.index(max(list[i:i+cnt+1]))
    if m != i:
        list[m], list[m-1] = list[m-1], list[m]
        cnt -= 1
    else:
        i += 1

print(*list)