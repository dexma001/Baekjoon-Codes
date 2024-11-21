arr = list()
for _ in range(5):
    temp = int(input())
    if temp in arr:
        arr.remove(temp)
    else:
        arr.append(temp)

print(*arr)
