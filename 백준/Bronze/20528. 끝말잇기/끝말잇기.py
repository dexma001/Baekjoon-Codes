n = int(input())
arr = list(map(str, input().split()))

k = arr[0][0]

for i in arr:
    if i[0] != k or i[-1] != k:
        print(0)
        quit()
else:
    print(1)
