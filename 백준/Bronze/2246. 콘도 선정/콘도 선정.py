arr = list()
n = int(input())

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
arr.sort(key=lambda x:[x[0], -x[1]])

answer = 0
for i in range(n):
    trig = 0
    for j in range(n):
        if trig == 1:
            break
        if i == j:
            continue
        if arr[i][0] > arr[j][0] and arr[i][1] >= arr[j][1]:
            trig = 1
        if arr[i][1] > arr[j][1] and arr[i][0] >= arr[j][0]:
            trig = 1
            
    if trig == 0:
        answer += 1
        
print(answer)