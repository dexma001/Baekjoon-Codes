arr = list(map(str, input().strip()))

answer = ""
answer += arr[0]

for i in range(1, len(arr)):
    if arr[i-1] == '-':
        answer += arr[i]
        
print(answer)