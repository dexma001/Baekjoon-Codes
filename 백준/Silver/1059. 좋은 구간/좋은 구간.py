l = int(input())
arr = list(map(int, input().split()))
arr.sort()
n = int(input())

answer = -1
answer_left = 0
answer_right = 0

for i in range(l-1):
    if answer != -1:
        break
    if arr[i] == n or arr[i+1] == n:
        answer = 0
        break
    if arr[i] < n and arr[i+1] > n:
        answer_left = arr[i] + 1
        answer_right = arr[i+1] - 1
        break
    
if arr[0] > n:
    answer_left = 1
    answer_right = arr[0]-1
    

if answer == 0:
    print(answer)
else:
    answer = 0
    for i in range(answer_left, n+1):
        for j in range(n, answer_right+1):
            if i == j:
                continue
            else:
                answer += 1
                
    print(answer)
        
