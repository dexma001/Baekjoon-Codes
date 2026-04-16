arr = list(map(str, input().strip()))
temp = [0, 0, 0]

for i in arr:
    if i == "U" or i == "C":
        temp[0] += 1

    else:
        temp[1] += 1
        temp[2] += 1

temp_max = max(temp[1], temp[2])
answer = ""
for i in range(3):
    if i == 0 and temp[i] > temp_max//2 + temp_max%2:
        answer += "U"
    
    if i == 1 and temp[i]:
        answer += "D"

    if i == 2 and temp[i]:
        answer += "P"

print(answer) if answer else print("C")