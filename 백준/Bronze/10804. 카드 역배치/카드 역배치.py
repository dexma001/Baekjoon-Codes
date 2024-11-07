# 10804

arr = list(i for i in range(21))

for _ in range(10):
    a, b = map(int, input().split())
    temp = arr[a:b+1]
    temp.reverse()
    arr[a:b+1] = temp
print(*arr[1:])