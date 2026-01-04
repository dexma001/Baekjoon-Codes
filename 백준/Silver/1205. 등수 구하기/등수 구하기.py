n, t, p = map(int, input().split())
if n == 0:
    print(1)
else:
    arr = list(map(int, input().split()))

    if arr[-1] >= t:
        if n == p:
            print(-1)
            quit()

    for i in range(n):
        if arr[i] > t:
            continue
        else:
                print(i+1)
                break            

    else:
        print(n+1)
        