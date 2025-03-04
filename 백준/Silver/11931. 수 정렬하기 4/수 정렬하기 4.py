arr = list()

for _ in range(int(input())):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i)
