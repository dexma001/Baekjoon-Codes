# 2668

import copy
import sys
input = sys.stdin.readline

n = int(input())
arr = list(list() for _ in range(n+1))

for i in range(1, n+1):
    arr[int(input())].append(i)

answer_arr = list()


def dfs(i, temp):
    temp.add(i)
    visited[i] = 1
    for j in arr[i]:
        if j not in temp:
            dfs(j, copy.deepcopy(temp))
        else:
            answer_arr.extend(temp)
            return


visited = list(0 for _ in range(n+1))
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = 1
        dfs(i, set([i]))

answer_arr.sort()
print(len(answer_arr))
for i in answer_arr:
    print(i)
