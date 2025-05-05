arr = str(input().strip())
answer = 0

for _ in range(int(input())):
    temp = str(input().strip())
    if arr[0:5] == temp[0:5]:
        answer += 1
        
print(answer)