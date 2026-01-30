arr = list(map(str, input().strip()))

answer = len(arr)-1
for i in range(len(arr)//2):
    if arr[i] != arr[len(arr)-1-i]:
        answer = len(arr)

if len(set(arr)) <= 1:
    answer = -1
    
print(answer)