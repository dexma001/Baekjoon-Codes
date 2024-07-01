# 7568

import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for i in range(n):
    arr.append(list(map(int, input().split())))

answer = [0] * (n)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                answer[i] += 1
    answer[i] += 1

print(*answer)
