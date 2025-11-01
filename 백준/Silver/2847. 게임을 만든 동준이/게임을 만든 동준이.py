#2847

import sys
input = sys.stdin.readline

n = int(input())
answer = 0
arr = list()

arr.append(int(input()))

for i in range(n-1):
    temp = int(input())
    if temp <= arr[-1]:
        arr.append(temp)
        for j in range(len(arr)-2, -1, -1):
            while arr[j] >= arr[j+1]:
                answer += 1
                arr[j] -= 1
    else:
        arr.append(temp)

print(answer)