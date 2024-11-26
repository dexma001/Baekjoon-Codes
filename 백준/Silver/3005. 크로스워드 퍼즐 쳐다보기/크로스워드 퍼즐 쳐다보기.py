# 3005

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = list()

for _ in range(r):
    arr.append(list(map(str, input().strip())))

answer = 'zzzzzzzzzzzzzzzzzzzzz'


def dfs_down(i, j, temp_answer):
    if i < r and arr[i][j] != '#':
        temp_answer += arr[i][j]
        return dfs_down(i+1, j, temp_answer)
    else:
        if len(temp_answer) >= 2:
            return temp_answer
        else:
            return 'zzzzzzzzzzzzzzzzzzzzz'


def dfs_right(i, j, temp_answer):
    if j < c and arr[i][j] != '#':
        temp_answer += arr[i][j]
        return dfs_right(i, j+1, temp_answer)
    else:
        if len(temp_answer) >= 2:
            return temp_answer
        else:
            return 'zzzzzzzzzzzzzzzzzzzzz'


for i in range(r):
    for j in range(c):
        if arr[i][j] == '#':
            continue
        if i == 0:
            answer = min(answer, dfs_down(i, j, ''))
        if j == 0:
            answer = min(answer, dfs_right(i, j, ''))
        if i-1 >= 0 and arr[i-1][j] == '#':
            answer = min(answer, dfs_down(i, j, ''))
        if j-1 >= 0 and arr[i][j-1] == '#':
            answer = min(answer, dfs_right(i, j, ''))

print(answer)
