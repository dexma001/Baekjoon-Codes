arr = list(map(str, input().strip()))

temp = ["U", "C", "P", "C"]
temp_idx = 0

for i in arr:
    if temp_idx >= 4:
        break
    if i == temp[temp_idx]:
        temp_idx += 1

print("I love UCPC") if temp_idx == 4 else print('I hate UCPC')