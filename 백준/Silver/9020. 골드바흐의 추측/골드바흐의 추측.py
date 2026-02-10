arr = list(i for i in range(10001))
arr[0] = -1
arr[1] = -1

for i in range(2, 10001):
    if arr[i] == -1:
        continue
    else:
        for j in range(2, 10000//i + 1):
            arr[i*j] = -1
            
for _ in range(int(input())):
    temp = int(input())
    p = list()
    for i in range(2, temp//2+1):
        if arr[i] != -1 and arr[temp - i] != -1:
            p = [i, temp-i]
    print(*p)