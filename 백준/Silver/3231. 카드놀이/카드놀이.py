n = int(input())
arr = list(0 for _ in range(n+1))

for i in range(n):
    temp = int(input())
    arr[temp] = i + 1
    
answer = 0

for i in range(1, n):
    if arr[i] > arr[i+1]:
        answer += 1
        
print(answer)