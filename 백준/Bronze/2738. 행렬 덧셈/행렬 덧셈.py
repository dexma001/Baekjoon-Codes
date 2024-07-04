a, b = map(int, input().split())

arr1 = list()
arr2 = list()

for _ in range(a):
    arr1.append(list(map(int, input().split())))

for _ in range(a):
    arr2.append(list(map(int, input().split())))

answer = list(list(0 for _ in range(b)) for _ in range(a))

for i in range(a):
    for j in range(b):
        answer[i][j] = arr1[i][j] + arr2[i][j]

for k in range(a):
    print(*answer[k])
