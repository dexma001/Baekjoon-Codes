import copy

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = copy.deepcopy(arr1)

answer1 = 0
answer2 = 0

for i in range(n):
    for j in range(n-i-1):
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
            answer1 += 1

for i in range(n):
    for j in range(n-i-1):
        if arr2[j] < arr2[j+1]:
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
            answer2 += 1

print(min(answer1, answer2+1))