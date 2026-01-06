a, p = map(int, input().split())
arr = list()
arr.append(a)

while True:
    temp = 0
    for i in str(arr[-1]):
        temp += int(i) ** p
        
    if temp in arr:
        arr.append(temp)
        break
    else:
        arr.append(temp)
    
for i in range(len(arr)):
    if arr[i] == arr[-1]:
        break
    
print(i)