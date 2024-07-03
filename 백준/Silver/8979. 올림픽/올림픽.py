# 8979

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[1], x[2], x[3]])

answer = 0
for i in range(n):
    if arr[i][0] == k:
        break
    answer += 1

print(answer)
