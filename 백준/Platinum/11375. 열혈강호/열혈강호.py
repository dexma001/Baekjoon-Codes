# 11375

import sys
input = sys.stdin.readline

people, work = map(int, input().split())
people_can_work = list([] for _ in range(people+1))
for i in range(people):
    temp_arr = list(map(int, input().split()))
    temp_arr.pop(0)
    people_can_work[i+1].extend(temp_arr)

used = [-1] * (work+1)


def bimatch(i):
    if visited[i]:
        return False
    visited[i] = True

    for num in people_can_work[i]:
        if used[num] == -1 or bimatch(used[num]):
            used[num] = i
            return True
    return False


for i in range(people):
    visited = [False] * (people + 1)
    bimatch(i+1)

print(work - used.count(-1)+1)
