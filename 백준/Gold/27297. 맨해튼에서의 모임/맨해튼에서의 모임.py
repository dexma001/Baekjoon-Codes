# 27297

import sys
input = sys.stdin.readline

dim, cnt = map(int, input().split())
arr = list([] for _ in range(dim))

for _ in range(cnt):
    temp = list(map(int, input().split()))
    for i in range(dim):
        arr[i].append(temp[i])

for i in range(dim):
    arr[i].sort()

answer = 0
answer_arr = list(0 for _ in range(dim))

for i in range(dim):
    if len(arr[i]) % 2 == 0:
        answer_arr[i] = (arr[i][len(arr[i])//2] +
                         arr[i][(len(arr[i])//2)-1]) // 2
    else:
        answer_arr[i] = arr[i][(len(arr[i])-1)//2]

answer = 0

for i in range(dim):
    temp_answer = 0
    for j in range(cnt):
        temp_answer += abs(arr[i][j] - answer_arr[i])
    answer += temp_answer

print(answer)
print(*answer_arr)
