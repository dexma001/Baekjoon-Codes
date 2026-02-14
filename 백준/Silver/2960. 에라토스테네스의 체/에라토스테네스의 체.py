n, k = map(int, input().split())

arr = list(i for i in range(n+1))
count = 0

for i in range(2, n+1):
    if arr[i] == -1:
        continue
    else:
        count += 1
        if count == k:
            print(i)
            quit()
        arr[i] = -1
        for j in range(2, n//i + 1):
            
            if arr[i*j] == -1:
                continue

            count += 1
            if count == k:
                print(i*j)
                quit()
            arr[i * j] = -1


    