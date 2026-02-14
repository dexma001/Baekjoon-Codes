arr = list()
for _ in range(8):
    arr.append(list(map(str, input().strip())))
    
answer = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and arr[i][j] == "F":
            answer += 1
        
        if i % 2 != 0 and j % 2 != 0 and arr[i][j] == "F":
            answer += 1
            
print(answer)