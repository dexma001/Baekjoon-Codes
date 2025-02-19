n,m = map(int, input().split())

arr = list()

i = 1
for _ in range(n):
    temp = list()
    for _ in range(m):
        temp.append(i)
        i += 1
    arr.append(temp)
    
for i in arr:
    print(*i)