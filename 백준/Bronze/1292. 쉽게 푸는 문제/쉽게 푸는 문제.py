a, b = map(int, input().split())

arr = list()

for i in range(1, 51):
    for j in range(i):
        arr.append(i)
        
print(sum(arr[a-1:b]))