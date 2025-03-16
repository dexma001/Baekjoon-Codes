answer = 0

arr = str(input())
for i in range(len(arr)-4+1):
    if arr[i:i+4] == 'DKSH':
        answer +=   1
        
print(answer)