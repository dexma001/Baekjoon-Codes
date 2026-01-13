import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(int(input()))

arr.sort()
arr = arr[:4]
    
temp_answer = list()

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        else:
            temp_answer.append(int(str(arr[i]) + str(arr[j])))
            
temp_answer.sort()
print(temp_answer[2])