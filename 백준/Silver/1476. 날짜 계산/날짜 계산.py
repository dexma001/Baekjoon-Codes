arr = list(map(int, input().split()))
answer = 1

temp = [1, 1, 1]

while arr != temp:
    temp[0] = (temp[0] % 15) + 1
    temp[1] = (temp[1] % 28) + 1
    temp[2] = (temp[2] % 19) + 1
    answer += 1
    
print(answer)