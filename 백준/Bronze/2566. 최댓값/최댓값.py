# 2566

import sys
input = sys.stdin.readline

arr = [[0]*10]
for _ in range(9):
    arr.append([0] + list(map(int, input().split())))

answer = -1
a, b = 0, 0

for i in range(1, 10):
    for j in range(1, 10):
        if arr[i][j] > answer:
            answer = arr[i][j]
            a, b = i, j

print(answer)
print(a, b)
