import sys
input = sys.stdin.readline

arr = list()
for i in range(8):
    temp = list(map(str, input().strip()))
    for j in range(8):
        if temp[j] == "*":
            arr.append([i, j])
         
t = len(arr)
answer = 1
if t != 8:
    answer = 0

for i in range(t-1):
    if answer == 0:
        break
    for j in range(i+1, t):
        if arr[i][0] == arr[j][0]:
            answer = 0
        elif arr[i][1] == arr[j][1]:
            answer = 0
        elif abs(arr[i][1] - arr[j][1]) == abs(arr[i][0] - arr[j][0]):
            answer = 0
        else:
            continue
        
if answer == 0:
    print('invalid')
else:
    print('valid')