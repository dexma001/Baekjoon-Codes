# 11376

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
people = list(list() for _ in range(2*n+1))
for i in range(n):
    temp = list(map(int, input().split()))
    temp.pop(0)
    people[i+1].extend(temp)
    people[n+i+1].extend(temp)

work = [0]*(m+1)


def bimatch(i):
    if visited[i]:
        return False
    visited[i] = True

    for j in people[i]:
        if work[j] == 0 or bimatch(work[j]):
            work[j] = i
            return True
    return False


for i in range(2*n):
    visited = [False] * (2*n+1)
    bimatch(i+1)

print(m - work.count(0) + 1)
