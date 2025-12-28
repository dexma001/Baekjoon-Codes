n = int(input())
temp = list(map(int, input().split()))
arr = list()

for i in range(n):
    t = temp[i]
    arr.append([i+1, t])
    
arr.sort(key=lambda x:[x[1], x[0]])

answer = list()

for i in range(n):
    if arr[i][1] == 0:
        answer.append(arr[i][0])
    else:
        temp = 0
        for j in range(len(answer)):
            if answer[j] > arr[i][0] and temp != arr[i][1]:
                temp += 1
                continue
                
            if temp == arr[i][1]:
                if answer[j] < arr[i][0]:
                    continue
                else:
                    if j == len(answer):
                        answer.append(arr[i][0])
                    else:
                        answer.insert(j, arr[i][0])    
                    break
        else:
            answer.append(arr[i][0])

print(*answer)