# 1931

import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

arr.sort(key=lambda x: [x[1], x[0]])
lasttime = arr[0][1]

answer = 1
for i in range(1, n):
    if arr[i][0] < lasttime:
        continue
    lasttime = arr[i][1]
    answer += 1

print(answer)
