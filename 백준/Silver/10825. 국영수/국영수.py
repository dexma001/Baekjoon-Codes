#10825

import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    temp = list(map(str, input().split()))
    for i in range(1, 4):
        temp[i] = int(temp[i])
    arr.append(temp)

arr.sort(key=lambda x:[-x[1], x[2], -x[3], x[0]])

for i in range(n):
    print(arr[i][0])