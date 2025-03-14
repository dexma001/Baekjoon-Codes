for _ in range(int(input())):
    arr = list(map(str, input().split()))
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    print(*arr)