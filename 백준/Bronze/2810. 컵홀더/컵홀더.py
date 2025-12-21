n = int(input())
arr = list(map(str, input().strip()))

answer = 1
temp = 0

for i in range(n):
    if arr[i] == 'S':
        answer += 1
    else:
        if temp == 1:
            answer += 1
            temp = 0
        else:
            temp = 1
            
if answer > n:
    answer = n
print(answer)
        