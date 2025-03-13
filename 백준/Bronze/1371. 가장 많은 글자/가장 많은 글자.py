
from collections import defaultdict

arr = defaultdict(int)
answer = ''

while True:
    try:
        temp = list(map(str, input().strip()))
    except:
        break
    
    for i in temp:
        if i != ' ':
            arr[i] += 1
            
temp = list(arr.items())
temp.sort(key=lambda x:[-x[1], x[0]])

for i, j in temp:
    if j == temp[0][1]:
        answer += i
    else:
        break
    
print(answer)