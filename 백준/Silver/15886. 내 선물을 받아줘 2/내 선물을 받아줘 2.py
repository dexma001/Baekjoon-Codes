n = int(input())
arr = list(map(str, input().strip()))

temp = 0
answer = 0
for i in range(1, n):
    if arr[i] == arr[i-1]:
        continue
    else:
        if temp == 0:
            temp = 1
        else:
            answer += 1
            temp = 0
         
if temp == 1:
    answer += 1
       
print(answer)
    